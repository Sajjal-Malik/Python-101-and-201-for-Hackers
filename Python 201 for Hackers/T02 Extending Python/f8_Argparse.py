"""
Ethical Hacking Example:
Using argparse to build a professional command-line port scanner

Run example:
python ethical_port_scanner.py -t 127.0.0.1 -s 20 -e 100
"""

import argparse
import socket

# -------------------------------
# Function: Port Scanner
# -------------------------------


def scan_ports(target_ip, start_port, end_port):
    """
    Scans ports on a target IP within a given range
    """
    print(f"\n[+] Scanning Target: {target_ip}")
    print(f"[+] Port Range: {start_port} - {end_port}\n")

    for port in range(start_port, end_port + 1):
        try:
            # Create a TCP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Set timeout so script doesn't hang
            sock.settimeout(0.5)

            # Try connecting to target IP and port
            result = sock.connect_ex((target_ip, port))

            if result == 0:
                print(f"[OPEN] Port {port}")

            sock.close()

        except KeyboardInterrupt:
            print("\n[!] Scan interrupted by user")
            break

        except socket.error:
            print("[!] Could not connect to target")
            break


# -------------------------------
# argparse Setup
# -------------------------------
parser = argparse.ArgumentParser(
    description="Ethical Hacking Tool - Simple Port Scanner"
)

# Target IP argument
parser.add_argument(
    "-t", "--target",
    required=True,
    help="Target IP address or hostname"
)

# Start port argument
parser.add_argument(
    "-s", "--start-port",
    type=int,
    default=1,
    help="Starting port number (default: 1)"
)

# End port argument
parser.add_argument(
    "-e", "--end-port",
    type=int,
    default=1024,
    help="Ending port number (default: 1024)"
)

# Parse arguments from terminal
args = parser.parse_args()

# -------------------------------
# Run Scanner using parsed args
# -------------------------------
scan_ports(
    target_ip=args.target,
    start_port=args.start_port,
    end_port=args.end_port
)
