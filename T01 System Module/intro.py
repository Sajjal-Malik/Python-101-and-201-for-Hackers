import sys
import time

print(sys.version)
print(sys.executable)
print(sys.platform)


for i in range(1, 5):
    sys.stdout.write(str(i))
    sys.stdout.flush()

for i in range(1, 5):
    print(i)

for i in range(1, 51):
    time.sleep(0.1)
    sys.stdout.write(f"{i} [{'#'*i}{'.'*(50 - i)}]")
    sys.stdout.flush()
    sys.stdout.write("\n")

# if len(sys.argv) != 3:
#    print(f"[X] T run {sys.argv[0]} provoide 'Username' and 'Password' please.")


# username = sys.argv[1]
# password = sys.argv[2]

# print(f"You entered Username:{username} and Password: {password}")

# print(sys.stdin)


