import socket
import os
from _thread import *
import sys
import random

PSEUDO=""

SSocket = socket.socket()
CSocket = socket.socket()

while True:
    Port = random.randint(1000, 10000)
    try:
        SSocket.bind(('localhost', Port))
        break
    except socket.error as e:
        print(str(e))
print('Port number: ', Port)
SSocket.listen(8)

def write_conn(conn):
    while True:
        COMM = input(">")
        conn.send(str.encode(COMM))
        instruction = COMM.split(" ")
        if(instruction[0]=="transfer"):
            transfer_receive(conn,instruction[1])

def transfer_sending(conn,filename):
    fileE = os.path.isfile(filename)
    print("[--] CHECKING IF FILE EXISTS OR NOT [--]")
    if fileE:
        print(":) File exists!!!")
    else:
        print(":( File doesn't exist!")
    try:
        file = open(filename,"rb")
        info = file.read()
        print(f"\r[UPLOAD] Uploading {filename}.")
        conn.send(info)
        file.close()
        print(f"\r[UPLOAD] Uploaded {filename}.\n>",end="")
    except Exception as e:
        conn.send("[E]".encode("utf-8"))
        conn.close()
        print("Error",e)
        print(":( File doesn't exist!")

def transfer_receive(conn,filename):
    print(f"\r[RECEIVE] Receiving {filename}.")
    file = open("new"+filename, "wb")
    info = b''
    while True:
        chunk = conn.recv(1024)
        info += chunk
        if len(chunk) < 1024:
            break
    file.write(info)
    file.close()
    print(f"\r[RECEIVE] Received {filename}.\n>",end="")

Conn_Port = int(input("Enter the port number of connection: "))
PSEUDO = str(input("Give a name to connection: "))
try:
    print('Connecting: ',PSEUDO,":",Conn_Port)
    CSocket.connect(('localhost',Conn_Port))
    print('Connected: ',PSEUDO,":",Conn_Port)
except Exception as E:
    print(':( Connection Failed!', E)

Sock, add = SSocket.accept()
print(':) Connection Successful! ' + add[0] + ':' + str(add[1]))

while True:
    PSEUDO = PSEUDO if PSEUDO!="" else str(Conn_Port)
    start_new_thread(write_conn, (Sock,))
    msg = CSocket.recv(1024).decode("utf-8")
    print(f"\rPORT {PSEUDO}: {msg}\n>",end="")
    instruction = msg.split(" ")
    if(instruction[0]=="transfer"):
        transfer_sending(CSocket,instruction[1])