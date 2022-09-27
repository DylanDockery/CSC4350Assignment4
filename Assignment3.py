#Dylan Dockery
#Server portion of client server spplication
#libraries needed : socket, argparse, datetime
#instructions: 
#Start via commandline. Commandline parameters are as follows: -t --- Communication protocol that can be set to either TCP or UDP. Default is TCP. 
#-p --- Port used for server. Default is 8000

from socket import *
import argparse
from datetime import datetime

#determines response to client
def response(requestedResource,HTTPVersion):
    print(requestedResource)
    if requestedResource == '/':
        requestedResource='/index.html'
    try:
        print(requestedResource)
        file1=open(requestedResource[1:],'r')
        HTTPReponse= HTTPVersion+' 200 OK\r\n'
        outputdata=[HTTPReponse]+file1.readlines()
    except:
        HTTPReponse= HTTPVersion+' 404 Not Found\r\n'
        outputdata=[HTTPReponse]

    print(outputdata)
    for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())


    
#command line argmuent declaration
parser = argparse.ArgumentParser(description='Server')
parser.add_argument('-p', type=int, default=8000,help='Port used for server. Required', required=True)
args = parser.parse_args()

serverPort=args.p

head=0
HTTPprotocol=0
requestedResource=1
HTTPVersion=2

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))  
print(serverSocket)  
serverSocket.listen(1)
print("The server is ready to receive")
while True:
        
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024).decode()
    request=message.split('\r\n')[0].split(' ')
    if(request[HTTPprotocol]=='GET'):
        response(request[requestedResource],request[HTTPVersion])
    connectionSocket.close()
