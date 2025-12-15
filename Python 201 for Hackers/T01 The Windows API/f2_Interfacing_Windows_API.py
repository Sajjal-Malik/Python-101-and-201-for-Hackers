import sys
import ctypes
from ctypes import windll, wintypes, byref, create_string_buffer


print("-------------------------------------------------")
print("Working with MessageBox function (winuser.h) from MSDN or Now Microsoft Learn")
print("-------------------------------------------------")

# --- 1. Define Aliases for common Windows Types for clarity ---
HWND = wintypes.HWND
LPCSTR = wintypes.LPCSTR
UINT = wintypes.UINT
INT = wintypes.INT

# --- 2. Define the functions ---

# A. Define FindWindow (using the Unicode version 'W' is recommended)
#    It takes two LPCWSTR (wide string pointers) and returns an HWND
FindWindow = windll.user32.FindWindowW
FindWindow.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR]
FindWindow.restype = HWND

# B. Define MessageBoxA (uses ASCII/byte strings)
MessageBoxA = windll.user32.MessageBoxA
MessageBoxA.argtypes = (HWND, LPCSTR, LPCSTR, UINT)
MessageBoxA.restype = INT
# print(MessageBoxA) # Keep this commented out for production

# --- 3. Execute the logic ---

# Try to find the *existing* window handle
window_title_to_find = "Honor Window of Message Box"
hWnd = FindWindow(None, window_title_to_find)

if hWnd == 0:
    print(f"Error: Could not find window with title '{window_title_to_find}'")
    print("Ensure the window is open and the title matches exactly.")
else:
    print(f"Found window handle: {hWnd}")
    # Prepare the strings for MessageBoxA (must be encoded as bytes/ASCII)
    lpText = b"Hello World inside BOX"
    lpCaption = b"Title Text of BOX"
    MB_OK = 0x00000000

    # Call MessageBoxA, linking it to the found window (hWnd)
    result = MessageBoxA(hWnd, lpText, lpCaption, MB_OK)
    print(f"MessageBox result code: {result}")


print("-------------------------------------------------")
print("Working with GetUserNameA function (winbase.h) from MSDN or Now Microsoft Learn")
print("-------------------------------------------------")


# --- 1. Define Aliases for common Windows Types ---
# BOOL, DWORD, etc. are defined in wintypes for clarity
BOOL = wintypes.BOOL
DWORD = wintypes.DWORD
LPSTR = wintypes.LPSTR  # Pointer to a string (ANSI version)

# Define the maximum possible username length (UNLEN is 256 in C headers, +1 for null terminator)
MAX_USERNAME_LEN = 256 + 1

# --- 2. Define the GetUserNameA function signature ---
# It takes a buffer pointer (LPSTR) and a pointer to the buffer size (LPDWORD/DWORD)
# It returns a non-zero BOOL (True/False) upon success
GetUserNameA = windll.advapi32.GetUserNameA
GetUserNameA.argtypes = [LPSTR, wintypes.LPDWORD]
GetUserNameA.restype = BOOL

# --- 3. Call the function ---

# Create a mutable buffer to hold the returned username (must be byte string compatible for GetUserNameA)
buffer = create_string_buffer(MAX_USERNAME_LEN)

# Create a variable to hold the size of the buffer, passed as a pointer (byref)
size = DWORD(MAX_USERNAME_LEN)

# Call the function. It returns a boolean (True if successful)
success = GetUserNameA(buffer, byref(size))

if success:
    # buffer.value returns the byte string up to the null terminator
    username_bytes = buffer.value
    # Decode the bytes to a standard Python string
    username_str = username_bytes.decode('ascii')
    print(f"Successfully retrieved username: {username_str}")
    print(
        f"Length of username (including null terminator in C terms): {size.value}")
else:
    # GetLastError provides more info on failure (e.g., ERROR_INSUFFICIENT_BUFFER)
    error_code = ctypes.get_last_error()
    print(f"Failed to retrieve username. Error code: {error_code}")
