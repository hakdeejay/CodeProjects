### get the connection library
import socket

# setup the connection socket
# AR_INET = use IPV4
# SOCK_STREAM = Use TCP
# SOCK_DGRAM = Use UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## connect to a port
## Double brackets indicate a tuple (constant)
client_socket.connect(('127.0.0.1', 1337))

## send some data
## send the string as binary 'b' indicate
client_socket.send(b"Do you want to play a game?\n")

## wait for data back and print it
received = client_socket.recv(1024)
print(received)

## be tidy and close socket connection
client_socket.close()