import sys
import socket
import time

host = sys.argv[1]
path = sys.argv[2] if len(sys.argv) > 2 else ""
enviar = "GET /"+path+" HTTP/1.1\nHost:"+host+"\n\n"
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(2)

s.connect((socket.gethostbyname(host),80))
time.sleep(0.5)
s.send(enviar.encode())
print("Conectado")

data =''
while 1:
    try:
        buf = s.recv(2000).decode()
        data+=buf
    except Exception as e:
        print(e)
        break
print(data)
