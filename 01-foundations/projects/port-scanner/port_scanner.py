"""
Simple TCP connect scanner, for learning.

Only scan hosts you own or have written permission to test.

Usage:
    python port_scanner.py 127.0.0.1 --ports 1-1024
"""
import argparse
import socket


def parse_ports(spec: str) -> list[int]:
    """Turn '22,80,8000-8010' into a list of port numbers."""
    ports = []
    for part in spec.split(","):
        if "-" in part:
            start, end = part.split("-")
            ports.extend(range(int(start), int(end) + 1))
        else:
            ports.append(int(part))
    return ports


def is_open(host: str, port: int, timeout: float = 0.5) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0


def main():
    parser = argparse.ArgumentParser(description="Learning TCP port scanner")
    parser.add_argument("host", help="Target you own, e.g. 127.0.0.1")
    parser.add_argument("--ports", default="1-1024", help="e.g. 22,80,443 or 1-1024")
    args = parser.parse_args()

    ip = socket.gethostbyname(args.host)
    print(f"Scanning {args.host} ({ip})")

    open_ports = [p for p in parse_ports(args.ports) if is_open(ip, p)]

    for p in open_ports:
        print(f"  {p}/tcp open")
    print(f"Done. {len(open_ports)} open port(s).")

    # TODO: --timeout flag, threading, service names, JSON output


if __name__ == "__main__":
    main()
