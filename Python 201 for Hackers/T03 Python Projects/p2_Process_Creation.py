"""
========================================================
Python Process Creation & In-Memory Execution (EDUCATIONAL)
========================================================

⚠️ ETHICAL NOTICE:
This script is for LEARNING PURPOSES ONLY.
It does NOT contain shellcode.
It does NOT exploit anything.
It does NOT inject into other processes.

The goal is to understand:
• How processes are created
• How memory is allocated
• How loaders conceptually work
"""

import subprocess
import ctypes
import sys
import os

# -------------------------------------------------------
# PART 1 — PROCESS CREATION (SAFE & LEGIT)
# -------------------------------------------------------

print("[+] Creating a child process using subprocess...")

# This creates a NEW operating system process
# Parent = Python
# Child  = system command
process = subprocess.Popen(
    ["whoami"],                  # Command to execute
    stdout=subprocess.PIPE,      # Capture output
    stderr=subprocess.PIPE,
    text=True
)

stdout, stderr = process.communicate()

print("[+] Child process output:")
print(stdout)

# What you learned:
# - How Python spawns a new OS process
# - Parent / child relationship
# - How red-team tools launch payloads (conceptually)


# -------------------------------------------------------
# PART 2 — RAW MEMORY ALLOCATION (FOUNDATION)
# -------------------------------------------------------

print("[+] Allocating raw memory in the current process...")

# ctypes lets Python talk directly to native memory
# This is the SAME mechanism used by loaders
buffer_size = 64

# Create a raw memory buffer (READ/WRITE)
memory_buffer = ctypes.create_string_buffer(buffer_size)

print(f"[+] Allocated {buffer_size} bytes of memory")
print(f"[+] Memory address: {ctypes.addressof(memory_buffer)}")

# -------------------------------------------------------
# PART 3 — WRITING RAW BYTES INTO MEMORY
# -------------------------------------------------------

print("[+] Writing raw bytes into allocated memory...")

# These bytes are NOT shellcode
# They are harmless placeholder bytes
# Real shellcode would be CPU instructions
raw_bytes = b"ETHICAL_HACKING_DEMO\x00"

ctypes.memmove(
    memory_buffer,      # Destination memory
    raw_bytes,          # Source bytes
    len(raw_bytes)      # Number of bytes
)

print("[+] Memory content written successfully")
print("[+] Buffer now contains:")
print(memory_buffer.raw)

# What you learned:
# - Shellcode is just BYTES
# - Loaders allocate memory
# - Loaders copy bytes into memory


# -------------------------------------------------------
# PART 4 — WHY EXECUTION IS POSSIBLE (THEORY)
# -------------------------------------------------------

"""
IMPORTANT THEORY (NO EXECUTION):

In real shellcode execution, the next steps would be:
1. Change memory permissions to EXECUTE
   - Windows: VirtualProtect / VirtualAlloc
   - Linux: mprotect / mmap

2. Jump to memory address
   - Using function pointers
   - Using assembly instructions

⚠️ We DO NOT do this here.

Why?
• Execution = weaponization
• Requires assembly-level control
• Not ethical outside a lab
"""

print("[+] Execution step intentionally skipped (ethical boundary)")

# -------------------------------------------------------
# PART 5 — SUMMARY
# -------------------------------------------------------

print("""
==================== SUMMARY ====================

You just learned:

✔ How Python creates OS processes
✔ How memory is allocated manually
✔ How raw bytes are written into memory
✔ How shellcode loaders work conceptually
✔ Where Python STOPS being suitable

REAL WORLD:
• Assembly  -> writes shellcode
• C/C++     -> executes shellcode
• Python    -> automates & loads (research)

=================================================
""")
