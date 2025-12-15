# Import the entire ctypes library
from ctypes import *

# Access the 'msvcrt' (Microsoft Visual C Runtime) DLL using the 'windll'
# loader. 'windll' assumes the standard C calling convention (__stdcall).
# Note: For cross-platform compatibility, you might use 'cdll' for __cdecl
# functions common in C/C++ libraries.
# On non-Windows systems, this part would need adjustment (e.g., using cdll.LoadLibrary("libc.so.6")).

# Call the 'time' function from msvcrt.
# time(None) passes a NULL pointer (equivalent to a C NULL or 0)
# to get the current system time as a POSIX timestamp.
print(windll.msvcrt.time(None))

# Call the 'puts' function to print a string to standard output.
# Python bytes objects (b"...") are automatically converted by ctypes
# to a C-style char* pointer (null-terminated string).
windll.msvcrt.puts(b"print this!")

# Create a mutable buffer of 10 bytes initialized with null bytes.
# This acts as a C-style char array.
mut_str = create_string_buffer(10)

# Print the initial raw content of the buffer (10 null bytes).
print(mut_str.raw)

# Assign a new value to the buffer.
# The .value property handles conversion and ensures null termination within the buffer limit.
# The buffer now holds b"AAAAA\x00\x00\x00\x00\x00"
mut_str.value = b"AAAAA"

# Print the raw content again (now contains "AAAAA").
print(mut_str.raw)

# --- Demonstrating a C function call to modify the buffer in-place ---

# Call the 'memset' function:
# 1. Destination pointer: mut_str
# 2. Value to set (as a c_char type representing 'X'): c_char(b"X")
# 3. Number of bytes to set: 5
# This overwrites the first 5 characters of 'AAAAA' with 'XXXXX'.
windll.msvcrt.memset(mut_str, c_char(b"X"), 5)

# Use 'puts' again to print the modified string (now "XXXXX").
# The C function modified the Python object's underlying buffer.
windll.msvcrt.puts(mut_str)

# Print the final raw content of the buffer.
print(mut_str.raw)
