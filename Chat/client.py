import socket 
import threading

#cerner_2^5_2019

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect(('IP FROM SERVER HERE', 64191))
user = input('Enter UserName: ')
client.send(bytes(user, 'utf-8'))

def recieve():
    while True:
        msg = client.recv(2048)
        if msg:
            print(msg.decode('utf-8'), flush = True)
            
def send():
    while True:
        msg = input()
        client.send(bytes(msg, 'utf-8'))
        print('<' + user + '> : ' + msg, flush = True)

t1 = threading.Thread(target = recieve)
t2 = threading.Thread(target = send)
t1.start()
t2.start()
