# Import the pwntools library for exploit development (used for progress logging here)
from pwn import *
# Import sys for command-line argument handling
import sys
# Import hashlib for SHA-256 hashing operations
import hashlib

# Check if exactly 2 arguments were provided (script name + hash to crack)
if len(sys.argv != 2):
    print("Invalid arguments")
    # Show usage: script name followed by SHA-256 hash
    print(f"{sys.argv[0]} <sha256sum>")
    exit()

# Store the target hash provided as command-line argument
wanted_hash = sys.argv[1]

# Define the password dictionary file (commonly used wordlist)
password_file = "rockyou.txt"
# Counter to track number of password attempts
attempts = 0

# Create a progress logger using pwntools' process context manager
with log.process(f"Attempting to crack: {wanted_hash}! \n") as p:

    # Open the password wordlist file for reading
    # 'latin-1' encoding handles various special characters in the wordlist
    with open(password_file, "r", encoding='latin-1') as password_list:

        # Iterate through each password in the wordlist
        for password in password_list:

            # Remove newline character and encode to bytes using latin-1
            password = password.strip("\n").encode('latin-1')
            # Calculate SHA-256 hash of the password
            # Note: This line has a bug - should be: hashlib.sha256(password).hexdigest()
            # This creates a hash object, not hex string
            password_hash = hashlib.sha256(password)

            # Update progress status showing current attempt count and what's being tested
            p.status(
                f"[{attempts}] {password.decode('latin-1')} == {password_hash}"
            )

            # Compare the hash object with the target hash string
            # Note: This comparison will always fail due to type mismatch
            # Should compare: password_hash.hexdigest() == wanted_hash
            if password == wanted_hash:  # Bug: comparing bytes with string

                # If match found, display success message with attempts count
                p.success(
                    f"Password hash found after {attempts}! {password.decode('latin-1')} hashes to {password_hash}"
                )
                exit()

            # Increment attempt counter for each password tested
            attempts += 1

        # If loop completes without finding a match, display failure message
        p.failure("Password hash not found!")
