# The server needs to be running all the time to be able to chat
#Using this you can chat only on your LAN that is all the device connected to your router
#To run this got to your terminal chnage directory to the location this file is at and run: python server.py 192.168.29.xxx(ip address) 8080(port number)

import socket
import select
import sys
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
# checks whether sufficient argument has been provided
if len(sys.argv) != 3:
    print("Correct USage: script, IP address, port number")
    exit()
# takes the first command fromm terminal as IP address
ip_address = str(sys.argv[1])
# takes the first command fromm terminal as Port Number
port = int(sys.argv[2])
# binds the server to an entered IP address and at the specified port number
server.bind((ip_address, port))
server.listen(100)
list_of_clients = []
def client(conn, addr):
    conn.sendall("Welcome to the chatroom!".encode("utf-8"))
    while True:
        message = conn.recv(2048)
        msg = message.decode("utf-8")
        if message:
            # prints the message and address of the user who just sent the message on the server terminal
            print("<" + addr[0] + ">" + msg)
            message_to_send = "<" + addr[0] + ">" + msg
            broadcast(message_to_send, conn)
        else:
            remove(conn)
# send the message to all client's connected to the server
def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)
while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print(addr[0] + "connected")
    # creates new thread for every new user
    start_new_thread(client, (conn,addr))
conn.close()
server.close()
