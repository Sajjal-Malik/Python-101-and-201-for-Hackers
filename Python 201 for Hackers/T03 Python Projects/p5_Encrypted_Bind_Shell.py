"""
=====================================================
Encrypted Command Server (Educational Lab)
=====================================================

This script demonstrates:
- Binding to a TCP port
- TLS encryption
- Password authentication
- Secure command handling
- No shell spawning
- Whitelisted commands only

This is NOT a backdoor or shell.
It is a learning lab for secure channels.

Author: Ethical Hacking Lab
=====================================================
"""

import socket
import ssl
import subprocess
import logging

# -------------------------------
# Configuration
# -------------------------------

HOST = "0.0.0.0"          # Bind to all interfaces
PORT = 8443               # Listening port
PASSWORD = "labpass123"   # Simple authentication (lab only)

CERT_FILE = "server.crt"
KEY_FILE = "server.key"

# Allowed commands (VERY IMPORTANT)
ALLOWED_COMMANDS = {
    "whoami": ["whoami"],
    "date": ["date"],
    "uptime": ["uptime"],
    "hostname": ["hostname"]
}

# -------------------------------
# Logging Setup
# -------------------------------

logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# -------------------------------
# TLS Context
# -------------------------------

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

# -------------------------------
# Server Setup
# -------------------------------


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)

        print(f"[+] Encrypted server listening on {PORT}")

        with context.wrap_socket(server_socket, server_side=True) as tls_socket:
            conn, addr = tls_socket.accept()
            print(f"[+] Connection from {addr}")
            logging.info(f"Connection from {addr}")

            handle_client(conn)

# -------------------------------
# Client Handler
# -------------------------------


def handle_client(conn):
    try:
        conn.send(b"Password: ")
        received_password = conn.recv(1024).decode().strip()

        if received_password != PASSWORD:
            conn.send(b"Authentication failed.\n")
            logging.warning("Failed authentication attempt")
            return

        conn.send(
            b"Authenticated.\nAvailable commands: whoami, date, uptime, hostname\n")

        while True:
            conn.send(b"\ncommand> ")
            command = conn.recv(1024).decode().strip()

            if command == "exit":
                conn.send(b"Goodbye.\n")
                break

            if command not in ALLOWED_COMMANDS:
                conn.send(b"Command not allowed.\n")
                continue

            # Execute allowed command safely
            result = subprocess.run(
                ALLOWED_COMMANDS[command],
                capture_output=True,
                text=True
            )

            output = result.stdout + result.stderr
            conn.send(output.encode())

            logging.info(f"Executed command: {command}")

    except Exception as e:
        logging.error(f"Error: {e}")

    finally:
        conn.close()
        logging.info("Connection closed")

# -------------------------------
# Entry Point
# -------------------------------


if __name__ == "__main__":
    start_server()
