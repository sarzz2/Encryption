#Using this you can chat only on your LAN that is all the device connected to your router
#To run this got to your terminal change directory to the location this file is at and run: python server.py 192.168.29.xxx(ip address) 8080(port number)

import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))

while True:
    sockets_list = [sys.stdin, server]

    read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print(message)
        else:
            message = sys.stdin.readline()
            server.sendall(message.encode("utf-8"))
            sys.stdout.write("You:")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()
