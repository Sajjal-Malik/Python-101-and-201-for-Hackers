import subprocess
import sys

# --- UNSAFE EXAMPLES (Original Code - Do not run with untrusted input) ---
# These examples use shell=True, which is dangerous if untrusted input is used.
# They are commented out as a safety measure.

subprocess.call(["calc"], shell=True)

# Note: check_call raises an exception if the command fails (non-zero exit code).
try:
    # "asd" is not a valid command, so this would raise a CalledProcessError
    out = subprocess.check_call(["cmd", "/c", "asd"], shell=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with error: {e}")

out = subprocess.check_call(["cmd", "/c", "calc"], shell=True)
#
# This would print the username to standard output, but the print statement
# below it would fail because check_call returns an exit code (0 for success),
# not the actual output data.
try:
    output_exit_code = subprocess.check_call(
        ["cmd", "/c", "whoami"], shell=True)
    # This line would cause an AttributeError because output_exit_code is an int, not bytes
    # print(f"The output of the Above process call is: {output_exit_code.decode()}")
except subprocess.CalledProcessError as e:
    print(f"Command failed with error: {e}")


# --- SAFE AND RECOMMENDED PRACTICES ---

# 1. Use run() instead of call(), check_call(), or Popen() for most modern tasks.
# 2. Avoid shell=True. Pass commands as a list of arguments.
# 3. Use capture_output=True to get the output directly into a variable.
# 4. Use text=True (or encoding='utf-8') to get strings instead of bytes.

try:
    # Example 1: Safely run a command and capture its output
    # 'whoami' is used here as a standard utility that poses no direct security threat itself.
    # The output is captured into the 'completed_process' object.
    completed_process = subprocess.run(
        ["whoami"],
        capture_output=True,
        text=True,  # Decodes output from bytes to a string
        check=True  # Raises an exception if the command fails
    )

    # The actual output is in the .stdout attribute
    user_info_output = completed_process.stdout.strip()
    print(f"The output of the 'whoami' command is: {user_info_output}")

except FileNotFoundError:
    print("The 'whoami' command was not found. Are you on a different OS?")
except subprocess.CalledProcessError as e:
    print(f"Command failed with error code {e.returncode}. Stderr: {e.stderr}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("-" * 20)

# Example 2: Check if a command is available (like 'ls' or 'dir')
try:
    # We use 'ls' for Linux/macOS and 'dir' for Windows as potential examples
    command_to_check = [
        "ls", "-l"
    ] if sys.platform != "win32" else ["cmd", "/c", "dir"]

    # We don't need the output, just need to know if it ran successfully
    subprocess.run(
        command_to_check,
        check=True,
        stdout=subprocess.PIPE,  # Discard output to avoid cluttering terminal
        stderr=subprocess.PIPE
    )
    print(
        f"The command '{' '.join(command_to_check)}' is available and ran successfully.")

except FileNotFoundError:
    print(f"The command '{command_to_check[0]}' was not found on your system.")
except subprocess.CalledProcessError:
    print(
        f"The command '{' '.join(command_to_check)}' failed to execute correctly.")
