import socket
import sys
from datetime import datetime
import threading


def handler(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))  # this will return a 1 on fail
    if result == 0:
        print("Port {} is Open".format(port))
    s.close()


# get target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # translate to IPv4
else:
    print("Invalid number of arguments")
    print("Syntax: python3 PortScanner.py <IPv4>")
    sys.exit()

# add a banner
print("-" * 50)
print("Scanning Target: " + target)
print("Started: " + str(datetime.now()))
print("-" * 50)

threads = 0

try:
    for port in range(1, 65535):
        threads += 1
        newThread = threading.Thread(target=handler(target, port), daemon=True)
        newThread.start()

except RuntimeError:
    print("{} threads created\n".format(threads))
except KeyboardInterrupt:
    print("\nQuitting Scan")
    sys.exit()
except socket.gaierror:
    print("HostName not resolved")
except socket.error:
    print("Couldn't connect Socket to server")
    sys.exit()

print("-" * 50)
print("Scanning Done: " + target)
print("Finished: " + str(datetime.now()))
print("-" * 50)
