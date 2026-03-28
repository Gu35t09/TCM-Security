# Sockets - can be used to connect two nodes together

import socket

HOST = '127.0.0.1'
PORT = 7777

# AF_INET is IPv4
# SOCK_STREAM is the port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT)) # We are using a tuple (immutable value) with the brakets (HOST,PORT)
s.accept()