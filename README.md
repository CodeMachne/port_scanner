
````md
# ⚔️ SentinelScan — CEH Port Scanner for Kali Linux

SentinelScan is a **professional-grade port scanning tool** designed for **Certified Ethical Hacker (CEH)** training, **Kali Linux penetration testing**, and **authorized security assessments**.

It assists security professionals in identifying exposed ports and services during the **early attack phases** of a penetration test.

---

## 📌 Overview

Port scanning is a foundational activity in offensive security.  
SentinelScan is built to simulate real-world reconnaissance and scanning techniques used by penetration testers before exploitation.

This tool is suitable for:
- CEH practical labs
- Kali Linux environments
- Capture The Flag (CTF) challenges
- Internal network security assessments

---

## 🧭 Attack Phase Mapping (CEH Methodology)

SentinelScan aligns with the **CEH Hacking Cycle**:

### 1️⃣ Reconnaissance (Information Gathering)
- Identifies live targets via reachable IP addresses
- Establishes network visibility

### 2️⃣ Scanning & Enumeration *(Primary Phase)*
- Detects open TCP ports
- Reveals exposed services
- Highlights potential entry points

### 3️⃣ Gaining Access *(Preparation Phase)*
- Scan results guide exploitation using tools like:
  - Metasploit
  - Hydra
  - SQLmap
  - Exploit-DB

⚠️ SentinelScan does **not** exploit systems — it prepares attackers and defenders with accurate intelligence.

---

## ⚙️ Core Features

- 🎯 Precision TCP port scanning
- 🔍 Custom port range targeting
- ⚡ Optimized socket-based engine
- 🧠 Clean, structured output
- 🐧 Native Kali Linux compatibility
- 📚 CEH-oriented learning design

---

## 🛠️ Technology Stack

- **Language:** Python 3  
- **Core Modules:** socket, sys  
- **Platform:** Kali Linux (fully cross-platform)  
- **Methodology:** CEH Scanning & Enumeration

---

## 🐧 Installation (Kali Linux)

Verify Python:

```bash
python3 --version
````

Clone the repository:

```bash
git clone https://github.com/codemachne/port_scanner.git
cd port_scanner
```

---

## ▶️ Usage

Execute the scanner:

```bash
python3 sentinelscan.py
```

Sample input:

```bash
Target IP: 192.168.56.101
Port Range: 1-1024
```

---

## 📡 Sample Output

```text
[+] SentinelScan Initializing...
[+] Target: 192.168.56.101
[+] Scan Phase: TCP Port Enumeration

[OPEN] 21   FTP
[OPEN] 22   SSH
[OPEN] 80   HTTP

[✔] Scan completed — 3 open ports identified
```

---

## 🧪 Professional Pentest Use Cases

* Initial attack surface discovery
* Verification of firewall exposure
* Baseline scans before exploitation
* Comparison with Nmap scan results
* Training students in real pentest workflows

---

## 🔐 Legal & Ethical Disclaimer

⚠️ **AUTHORIZED TESTING ONLY**

This tool is intended exclusively for:

* Ethical hacking labs
* Security research
* Systems owned by the user or tested with explicit permission

Unauthorized port scanning is illegal and punishable under cybersecurity laws.

---

## 🚀 Roadmap

* Multi-threaded scanning engine
* Service & version detection
* Banner grabbing
* Stealth scan techniques
* Report export (JSON / TXT)
* Nmap-style verbosity levels

---

## 👨‍💻 Author

**Abang Ayoma**
Cybersecurity Professional | CEH Instructor | Kali Linux Practitioner

---

## ⭐ Acknowledgment

If SentinelScan supports your ethical hacking journey:

* ⭐ Star the repository
* 🔐 Hack responsibly
* 📘 Keep sharpening your skills

```
