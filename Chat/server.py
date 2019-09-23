import socket, threading

#cerner_2^5_2019

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.bind(('Your IP here', 64191))
s.listen(5)
client_dict = {}

def handler(clientsocket, address):
    print(f'Connection from {address} has been established')
    msg = 'Welcome to Cerner Chat!'
    clientsocket.send(bytes(msg,'utf-8'))
    user_name = clientsocket.recv(64)
    
    if user_name:
        user_name = user_name.decode('utf-8')
        client_dict[clientsocket] = user_name
    
    while True:
        try:
            msg = clientsocket.recv(2048)
            if msg:
                send_msg = f'<{client_dict[clientsocket]}> : {msg.decode("utf-8")}'
                print(send_msg)
                broadcast(send_msg, clientsocket)
            else: client_dict.pop(client, None)
        except: continue

def broadcast(msg, clientsocket):
    for client in list(client_dict):
        if client != clientsocket: 
            try: client.send(bytes(msg, 'utf-8')) 
            except: 
                client.close()  
                client_dict.pop(client, None) 

while True:
    clientsocket, address = s.accept()
    threading.Thread(target = handler, args = (clientsocket, address)).start()
