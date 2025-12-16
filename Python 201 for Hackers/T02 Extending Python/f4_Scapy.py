from scapy.all import *

# =========================================================
# CONFIGURATION SECTION
# =========================================================

TARGET_DOMAIN = "247ctf.com"
TARGET_IP = "127.0.0.1"      # Use localhost or lab machine only
LOCAL_NETWORK = "192.168.10.0/24"

COMMON_PORTS = [22, 80, 139, 443, 445, 8080]

ICMP_TIMEOUT = 2
TCP_TIMEOUT = 1

# TCP FLAG VALUES (used internally by TCP)
TCP_SYN = 0x02
TCP_RST = 0x04
TCP_ACK = 0x10


# =========================================================
# 1️⃣ ICMP HOST DISCOVERY (PING)
# =========================================================
# Used to check if a host is alive
# Many firewalls block ICMP, so failure ≠ host down

print("\n[+] ICMP Host Discovery")

ip_layer = IP(dst=TARGET_DOMAIN)
icmp_echo_request = ICMP()

icmp_packet = ip_layer / icmp_echo_request

icmp_reply = sr1(
    icmp_packet,
    timeout=ICMP_TIMEOUT,
    verbose=False
)

if icmp_reply:
    print(f"[✔] Host {TARGET_DOMAIN} is alive (ICMP reply received)")
else:
    print(f"[✖] No ICMP reply (host may be blocking ICMP)")


# =========================================================
# 2️⃣ ARP SCAN (LOCAL NETWORK DISCOVERY)
# =========================================================
# ARP works only inside local networks
# This bypasses ICMP and finds live hosts reliably

print("\n[+] ARP Scan on Local Network")

ethernet_broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
arp_request = ARP(pdst=LOCAL_NETWORK)

arp_packet = ethernet_broadcast / arp_request

answered_packets, unanswered_packets = srp(
    arp_packet,
    timeout=3,
    verbose=False
)

if answered_packets:
    print("[✔] Live hosts discovered:")
    for sent_packet, received_packet in answered_packets:
        print(
            f"    IP Address: {received_packet.psrc} | "
            f"MAC Address: {received_packet.hwsrc}"
        )
else:
    print("[✖] No live hosts found (wrong network or isolation)")


# =========================================================
# 3️⃣ TCP SYN PORT SCAN (HALF-OPEN SCAN)
# =========================================================
# This is the same technique used by nmap -sS
# Only SYN is sent — no full TCP handshake

print("\n[+] TCP SYN Port Scan")

for target_port in COMMON_PORTS:

    # Create TCP SYN packet
    tcp_syn_packet = IP(dst=TARGET_IP) / TCP(
        sport=RandShort(),     # Random source port
        dport=target_port,     # Target port
        flags="S"              # SYN flag
    )

    tcp_response = sr1(
        tcp_syn_packet,
        timeout=TCP_TIMEOUT,
        verbose=False
    )

    if tcp_response and tcp_response.haslayer(TCP):

        response_flags = tcp_response[TCP].flags

        # SYN + ACK → Port is OPEN
        if response_flags == (TCP_SYN + TCP_ACK):
            print(f"[OPEN] Port {target_port}")

            # Send RST to close connection immediately
            tcp_rst_packet = IP(dst=TARGET_IP) / TCP(
                sport=RandShort(),
                dport=target_port,
                flags="R"
            )
            send(tcp_rst_packet, verbose=False)

        # RST + ACK → Port is CLOSED
        elif response_flags == (TCP_RST + TCP_ACK):
            print(f"[CLOSED] Port {target_port}")

    # No response → Firewall or filtered
    else:
        print(f"[FILTERED] Port {target_port}")


# =========================================================
# 4️⃣ UDP PORT PROBING (BASIC)
# =========================================================
# UDP is connectionless → no response usually means OPEN
# ICMP Port Unreachable → CLOSED

print("\n[+] UDP Port Probe (Basic)")

UDP_PORTS = [53, 67, 123]

for udp_port in UDP_PORTS:

    udp_packet = IP(dst=TARGET_IP) / UDP(dport=udp_port)

    udp_response = sr1(
        udp_packet,
        timeout=3,
        verbose=False
    )

    if udp_response is None:
        print(f"[OPEN | FILTERED] UDP Port {udp_port}")

    elif udp_response.haslayer(ICMP):
        icmp_type = udp_response[ICMP].type
        icmp_code = udp_response[ICMP].code

        # ICMP Type 3 Code 3 = Port Unreachable
        if icmp_type == 3 and icmp_code == 3:
            print(f"[CLOSED] UDP Port {udp_port}")

    else:
        print(f"[UNKNOWN] UDP Port {udp_port}")


# =========================================================
# 5️⃣ PACKET INSPECTION (LEARNING TOOL)
# =========================================================
# Shows how packets are built internally
# Extremely useful with Wireshark

print("\n[+] Packet Structure Example")

example_packet = IP(dst=TARGET_IP) / TCP(dport=80, flags="S")
example_packet.show()
