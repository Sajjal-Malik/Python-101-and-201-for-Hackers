from ctypes import *
from ctypes import wintypes

SIZE_T = c_size_t
NTSTATUS = wintypes.DWORD

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_EXECUTE_READWRITE = 0x40

# --- Error Handling ---


def verify(x):
    if not x:
        # Raises an appropriate Windows error description if an API call fails
        raise WinError()


# --- 1. Define the Machine Code (Shellcode) ---
# This shellcode simply moves the value 5 into the EAX register and returns.
buffer = create_string_buffer(b"\xb8\x05\x00\x00\x00\xc3")
buffer_address = addressof(buffer)
print(f"Buffer address: {hex(buffer_address)}")

# --- 2. Define the VirtualProtect function from kernel32.dll ---
VirtualProtect = windll.kernel32.VirtualProtect
VirtualProtect.argtypes = (wintypes.LPVOID, SIZE_T,
                           wintypes.DWORD, wintypes.LPDWORD)
VirtualProtect.restype = wintypes.INT

# --- 3. Change Memory Permissions ---
old_protection = wintypes.DWORD(0)  # Initialize old_protection variable
protect_success = VirtualProtect(buffer_address, len(
    buffer), PAGE_EXECUTE_READWRITE, byref(old_protection))

verify(protect_success)
print(
    f"Memory protection changed successfully. Old protection was: {hex(old_protection.value)}")

# --- 4. Execute the shellcode ---

# Cast the buffer address into a Python function pointer type (CFUNCTYPE)
# Since our simple shellcode takes no arguments and returns a value (in EAX),
# we define the function signature as CFUNCTYPE(return_type)
# The return type for a simple int return is c_int.

shellcode_function = CFUNCTYPE(c_int)(buffer_address)

print("\n--- Executing shellcode now ---")
# Call the function pointer:
result = shellcode_function()
print(
    f"Shellcode execution finished. The returned value (from EAX register) is: {result}")

input("Press Enter to exit...")
