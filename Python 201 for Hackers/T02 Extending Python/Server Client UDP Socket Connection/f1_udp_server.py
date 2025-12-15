import socket

# Create UDP socket (IPv4)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to port
server_socket.bind(('', 9091))
print("UDP Server listening on port 9091...")

while True:
    # Receive data + client address
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received from {client_address}: {data.decode()}")

    # Send response back
    server_socket.sendto(b"Hello from UDP server!", client_address)
