#!/usr/bin/env python3
"""
SentinelScan - Professional CEH Port Scanner
Author: Abang Ayoma
Purpose: Ethical Hacking | CEH | Kali Linux
"""

import socket
import sys
import threading
from queue import Queue
from datetime import datetime

# =======================
# CONFIGURATION
# =======================
THREADS = 100
TIMEOUT = 1
queue = Queue()
open_ports = []

# =======================
# BANNER
# =======================
def banner():
    print("""
 ███████╗███████╗███╗   ██╗████████╗██╗███╗   ██╗███████╗██╗     ███████╗ ██████╗ █████╗ ███╗   ██╗
 ██╔════╝██╔════╝████╗  ██║╚══██╔══╝██║████╗  ██║██╔════╝██║     ██╔════╝██╔════╝██╔══██╗████╗  ██║
 ███████╗█████╗  ██╔██╗ ██║   ██║   ██║██╔██╗ ██║█████╗  ██║     ███████╗██║     ███████║██╔██╗ ██║
 ╚════██║██╔══╝  ██║╚██╗██║   ██║   ██║██║╚██╗██║██╔══╝  ██║     ╚════██║██║     ██╔══██║██║╚██╗██║
 ███████║███████╗██║ ╚████║   ██║   ██║██║ ╚████║███████╗███████╗███████║╚██████╗██║  ██║██║ ╚████║
 ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝

        CEH | Kali Linux | Ethical Hacking Port Scanner
    """)

# =======================
# RECONNAISSANCE PHASE
# =======================
def resolve_target(target):
    try:
        ip = socket.gethostbyname(target)
        print(f"[+] Reconnaissance Phase")
        print(f"[+] Target Resolved: {target} → {ip}")
        return ip
    except socket.gaierror:
        print("[-] Failed to resolve target")
        sys.exit(1)

# =======================
# SCANNING PHASE
# =======================
def scan_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            print(f"[OPEN] Port {port:<5} Service: {service}")
        sock.close()
    except:
        pass

def threader(target_ip):
    while True:
        port = queue.get()
        scan_port(target_ip, port)
        queue.task_done()

# =======================
# MAIN LOGIC
# =======================
def main():
    banner()

    target = input("[?] Enter Target IP / Domain: ").strip()
    port_range = input("[?] Enter Port Range (e.g. 1-1024): ").strip()

    try:
        start_port, end_port = map(int, port_range.split("-"))
    except ValueError:
        print("[-] Invalid port range format")
        sys.exit(1)

    target_ip = resolve_target(target)

    print("\n[+] Scanning & Enumeration Phase")
    print(f"[+] Target IP : {target_ip}")
    print(f"[+] Port Range: {start_port}-{end_port}")
    print(f"[+] Scan Started at: {datetime.now()}\n")

    # Create threads
    for _ in range(THREADS):
        t = threading.Thread(target=threader, args=(target_ip,), daemon=True)
        t.start()

    # Fill the queue
    for port in range(start_port, end_port + 1):
        queue.put(port)

    queue.join()

    # =======================
    # RESULTS
    # =======================
    print("\n[✔] Scan Completed")
    print(f"[+] Open Ports Found: {len(open_ports)}")

    if open_ports:
        print("[+] Open Ports Summary:")
        for port in open_ports:
            print(f"    - Port {port}")
    else:
        print("[-] No open ports detected")

    print(f"\n[+] Scan Finished at: {datetime.now()}")
    print("[+] SentinelScan Execution Complete")

# =======================
# ENTRY POINT
# =======================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user")
        sys.exit(0)
