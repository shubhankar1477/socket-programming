import socket 
import time
HEADERSIZE = 10

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)





while True:
    clientsocket , adress = s.accept()
    print(f"connection from {adress} has been established")
    while True:
        time.sleep(3)
        msg = f"time is{time.time()}"
        msg = f"{len(msg):<{HEADERSIZE}}"+msg
        clientsocket.send(bytes(msg,"utf-8"))
    
     

