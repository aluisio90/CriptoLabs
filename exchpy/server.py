import socket
from random import *
listen = socket.socket()
destination = input('Pleas insert dest. host IP: ')
#listen.connect( (destination,  1999) )
#Questa forse dovrebbe essere utilizzata dal client
print(listen)

key = open('pub_k.txt', 'w')
key.write(randint(1,100) )
key.close()
message = key

listen.send(key.encode())
listen.close()
print(listen)
