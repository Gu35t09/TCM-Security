import sys
import socket
from datetime import datetime
import threading

# Function to scan a port
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port)) # error indictor - if 0, port is open
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    except socket.error as e:
        print(f"Socket error on port {port}: {e}")
    except Exception as e:
        print(f"Unexpected error on port {port}: {e}")

# Main function - argument validation and target definition
# Script command example --> python.exe scanner.py 192.168.1.1
# There are 2 arguments, 0 - scanner.py, 1 - 192.168.1.1
def main():
    if len(sys.argv) == 2: # If we have 2 arguments, the 1 (second) will be the target host
        target = sys.argv[1] 
    else:
        print("Invalid number of arguments!")
        print("Usage: python.exe scanner.py <target>")
        sys.exit(1) # 1 is for not clean exit

    # Resolve the target hostname to an IP address
    try:
        target_ip = socket.gethostbyname (target)
    except socket.gaierror:
        print(f"Error: Unable to resolve hostname {target}")
        sys.exit(1)

    # Add a pretty banner
    print("-" * 50)
    print(f"Scanning target {target_ip}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    try:
        # Use multithreading to scan port concurrently
        threads = [] 
        for port in range(1,65536): #65536 to stop at 65535
            # thread is a like a separate flow of execution
            # target = the function we want the thread to execute, in this case scan_port
            # args = the parameters need by the the function we are calling
            thread = threading.Thread(target=scan_port, args=(target_ip, port))
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join() # Wait the thread complete

    except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit(0)
    except socket.error as e:
        print(f"Socket error: {e}")
        sys.exit(1)

    print("\nScan completed!")

# Best practies 
# If we are not running the script directly this script won't work
# if for example we do import scanner.py in another script, the __name__ variable would container "scanner"
if __name__ == "__main__":
    main()