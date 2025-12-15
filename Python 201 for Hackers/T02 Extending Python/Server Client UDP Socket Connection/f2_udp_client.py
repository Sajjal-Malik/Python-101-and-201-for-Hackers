import socket

# Create UDP socket (IPv4)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to server
client_socket.sendto(b"Hello from UDP client!", ("127.0.0.1", 9091))

# Receive response
data, server_address = client_socket.recvfrom(1024)
print("Received from server:", data.decode())

client_socket.close()
