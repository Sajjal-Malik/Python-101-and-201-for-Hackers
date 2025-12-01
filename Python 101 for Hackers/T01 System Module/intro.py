import sys
import time

# Print Python version, executable path, and platform information
print(sys.version)
print(sys.executable)
print(sys.platform)

# Write numbers 1-4 to stdout without newlines and flush immediately
for i in range(1, 5):
    sys.stdout.write(str(i))
    sys.stdout.flush()

# Print numbers 1-4 (print adds newlines by default)
for i in range(1, 5):
    print(i)

# Create a progress bar visualization
for i in range(1, 51):
    time.sleep(0.1)  # Pause for 0.1 seconds between iterations
    # Write progress bar: number, followed by '#' for progress and '.' for remaining
    sys.stdout.write(f"{i} [{'#'*i}{'.'*(50 - i)}]")
    sys.stdout.flush()  # Force output to be displayed immediately
    sys.stdout.write("\n")  # Move to next line

# The following section demonstrates command-line argument handling
# It's currently commented out to prevent errors when no arguments are provided

# if len(sys.argv) != 3:
#    print(f"[X] T run {sys.argv[0]} provide 'Username' and 'Password' please.")
#    sys.exit(1)  # Added for completeness - exit with error code

# username = sys.argv[1]
# password = sys.argv[2]

# print(f"You entered Username:{username} and Password: {password}")

# Print stdin file object information
# print(sys.stdin)
