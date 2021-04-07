import socket
import os
from _thread import *

ServerSocket = socket.socket()


# Get the assigned container IP Address
hostName = socket.gethostname()
ipAddress = socket.gethostbyname(hostName)
print('Container IP: ' + ipAddress)

host = input(
    "What is the Server IP Address or Hostname? (default: " + ipAddress + ") ") or ipAddress
port = int(input("What is the Server Port? (default: 1223) ") or "1223")

ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')

ServerSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode('Welcome to the Servern'))
    while True:
        data = connection.recv(2048)
        reply = 'Server Says: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()


while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
