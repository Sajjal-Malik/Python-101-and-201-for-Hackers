from ctypes import *
from ctypes import wintypes

# Load the kernel32.dll library, which contains core Windows API functions
kernel32 = windll.kernel32
# Define a standard Windows type for sizes/counts (can be 32-bit or 64-bit depending on the OS)
SIZE_T = c_size_t

# --------------------------------------------------
# PART 1: Using VirtualAlloc (higher-level Windows API)
# --------------------------------------------------

# Get a reference to the VirtualAlloc function
VirtualAlloc = kernel32.VirtualAlloc
# Define the argument types for VirtualAlloc (matching the C function signature)
VirtualAlloc.argtypes = (wintypes.LPVOID, SIZE_T,
                         wintypes.DWORD, wintypes.DWORD)
# Define the return type of VirtualAlloc (a pointer to the allocated memory, or NULL on failure)
VirtualAlloc.restype = wintypes.LPVOID

# Define constants for memory allocation flags:
# Reserves a range of memory pages and makes them available for use
MEM_COMMIT = 0x00001000
# Reserves a range of the process's virtual address space without allocating physical storage
MEM_RESERVE = 0x00002000
# Sets memory permissions to allow execution, reading, and writing
PAGE_EXECUTE_READWRITE = 0x40

# Call VirtualAlloc to allocate memory:
# Args:
# 1. lpAddress (None/NULL): Let the OS decide where to allocate the memory
# 2. dwSize (1024 * 4 = 4KB): The size of the region to allocate
# 3. flAllocationType (MEM_COMMIT | MEM_RESERVE): Allocate and reserve the pages
# 4. flProtect (PAGE_EXECUTE_READWRITE): Set permissions to allow execution, read, and write
ptr = VirtualAlloc(None, 1024 * 4, MEM_COMMIT |
                   MEM_RESERVE, PAGE_EXECUTE_READWRITE)

# Check for errors using the Windows GetLastError function
error = GetLastError()

if error:
    print(error)
    # Print the specific Windows error message associated with the error code
    print(WinError(error))

print("VirtualAlloc:", hex(ptr))  # Print the address of the allocated memory


# --------------------------------------------------
# PART 2: Using NtAllocateVirtualMemory (Native API)
# --------------------------------------------------

# Load the ntdll.dll library, which contains the low-level Native API functions
nt = windll.ntdll
# Define the NTSTATUS type (a standard 32-bit integer used for Native API function return codes)
NTSTATUS = wintypes.DWORD

# Get a reference to the NtAllocateVirtualMemory function
NtAllocateVirtualMemory = nt.NtAllocateVirtualMemory
# Define the argument types for NtAllocateVirtualMemory (more complex C function signature)
NtAllocateVirtualMemory.argtypes = (wintypes.HANDLE, POINTER(
    wintypes.LPVOID), wintypes.ULONG, POINTER(wintypes.ULONG), wintypes.ULONG, wintypes.ULONG)
# Define the return type (NTSTATUS code)
NtAllocateVirtualMemory.restype = NTSTATUS

# Define variables and types to pass by reference to the function:
# Represents the current process handle (special value for 'CurrentProcess')
handle = 0xffffffffffffffff
# Pointer variable where the resulting address will be stored
base_address = wintypes.LPVOID(0x0)
zero_bits = wintypes.ULONG(0)       # Alignment requirement (usually 0)
size = wintypes.ULONG(1024 * 12)    # The requested size (12KB)

# Call NtAllocateVirtualMemory:
# This function modifies 'base_address' and 'size' in place (passed by reference using byref())
ptr2 = NtAllocateVirtualMemory(handle, byref(base_address), zero_bits, byref(
    size), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READWRITE)

# Check the return status code
if ptr2 != 0:
    print("error!")
    print(ptr2)  # A non-zero NTSTATUS code indicates an error

# Print the address stored in the base_address variable
print("NtAllocateVirtualMemory: ", hex(base_address.value))

# Keep the console window open until the user presses Enter
input()
