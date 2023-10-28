import socket


def scan_port(target_host, target_port):
    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set a timeout to handle unresponsive ports
    socket.setdefaulttimeout(1)

    try:
        # Attempt to connect to the target host and port
        client.connect((target_host, target_port))
        print(f"[+] Port {target_port} is open")
    except Exception as e:
        # Print an error message if the connection fails
        pass
    finally:
        # Close the socket connection
        client.close()


def scan_range(target_host, start_port, end_port):
    print(f"Scanning ports on {target_host}...")
    for port in range(start_port, end_port + 1):
        scan_port(target_host, port)


if __name__ == "__main__":
    target_host = input("Enter target host: ")
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    scan_range(target_host, start_port, end_port)
