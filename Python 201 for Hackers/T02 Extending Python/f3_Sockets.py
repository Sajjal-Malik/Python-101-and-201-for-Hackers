import socket

# -------------------------------
# STEP 1: DNS RESOLUTION
# -------------------------------

# Convert domain name to IP address
host = "247ctf.com"
ip = socket.gethostbyname(host)

print(f"Resolved IP: {ip}")
print(f"IP type: {type(ip)}")

# -------------------------------
# STEP 2: CREATE A SOCKET
# -------------------------------

# AF_INET  -> IPv4
# SOCK_STREAM -> TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set timeout so program doesn't hang forever
client_socket.settimeout(5)

try:
    # -------------------------------
    # STEP 3: CONNECT TO SERVER
    # -------------------------------
    client_socket.connect((host, 80))
    print("Connected to server")

    # -------------------------------
    # STEP 4: SEND DATA
    # -------------------------------

    # HTTP request must be in bytes
    http_request = (
        "HEAD / HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        "Connection: close\r\n"
        "\r\n"
    )

    client_socket.sendall(http_request.encode())
    print("Request sent")

    # -------------------------------
    # STEP 5: RECEIVE DATA
    # -------------------------------

    response = b""

    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        response += chunk

    print("\n--- Server Response ---")
    print(response.decode(errors="ignore"))

except socket.timeout:
    print("Connection timed out")

except socket.error as e:
    print("Socket error:", e)

finally:
    # -------------------------------
    # STEP 6: CLOSE SOCKET
    # -------------------------------
    client_socket.close()
    print("Socket closed")
