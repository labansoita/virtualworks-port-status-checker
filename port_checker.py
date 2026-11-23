
import socket

print("=" * 45)
print("          PORT STATUS CHECKER")
print("=" * 45)

# Get the target system
host = input("Enter IP address or hostname: ").strip()

# Get the port number
try:
    port = int(input("Enter port number (1-65535): "))

    if not 1 <= port <= 65535:
        print("Error: Port must be between 1 and 65535.")
        raise SystemExit

except ValueError:
    print("Error: Please enter a valid port number.")
    raise SystemExit

# Check the port
print(f"\nChecking {host} on port {port}...")

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(3)
        result = sock.connect_ex((host, port))

    print("\n" + "=" * 45)

    if result == 0:
        print(f"PORT {port}: OPEN")
    else:
        print(f"PORT {port}: CLOSED or FILTERED")

    print("=" * 45)

except socket.gaierror:
    print("Error: Could not resolve the hostname.")

except OSError as error:
    print(f"Network error: {error}")
