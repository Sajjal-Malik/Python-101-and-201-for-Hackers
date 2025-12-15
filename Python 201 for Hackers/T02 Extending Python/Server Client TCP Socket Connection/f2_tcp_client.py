import socket

# Create TCP socket (IPv4)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(("127.0.0.1", 9090))
print("Connected to TCP server")

# Send message
client_socket.sendall(b"Hello from TCP client!")

# Receive response
response = client_socket.recv(1024)
print("Received from server:", response.decode())

# Close socket
client_socket.close()
