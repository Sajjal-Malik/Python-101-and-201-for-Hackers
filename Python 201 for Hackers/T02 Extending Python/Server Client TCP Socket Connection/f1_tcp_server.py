import socket

# Create TCP socket (IPv4)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to IP and port
# '' means accept connections from any network interface
server_socket.bind(('', 9090))

# Listen for incoming connections
server_socket.listen(1)
print("TCP Server listening on port 9090...")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Connected to client: {client_address}")

# Receive data from client
data = client_socket.recv(1024)
print("Received from client:", data.decode())

# Send response to client
client_socket.sendall(b"Hello from TCP server!")

# Close connections
client_socket.close()
server_socket.close()
