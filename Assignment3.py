#Dylan Dockery
#Server to process HTTP GET requests
#libraries needed : socket, argparse
#instructions: 
#Start via commandline. Commandline parameters are as follows:
#-p --- Port used for server. Required 

from socket import *
import argparse


#determines response to client
def response(requestedResource,HTTPVersion):

    #if no resource requested return index.html
    if requestedResource == '/':
        requestedResource='/index.html'

    #attempts to locate the requested resource if succesful it returns 200 and the resource and if not 404
    try:
        file1=open(requestedResource[1:],'r')
        HTTPReponse= HTTPVersion+' 200 OK\r\n'
        outputdata=[HTTPReponse]+file1.readlines()
    except:
        HTTPReponse= HTTPVersion+' 404 Not Found\r\n'
        outputdata=[HTTPReponse]

    #sends resource over connection
    for i in range(0, len(outputdata)):
        connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())


#command line argmuent declaration
parser = argparse.ArgumentParser(description='Server')
parser.add_argument('-p', type=int, default=8000,help='Port used for server. Required', required=True)
args = parser.parse_args()

#port for the server to use
serverPort=args.p

#indices for parsing the incoming GET request
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
    
    #opens socket and processes incoming HTTP requests
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024).decode()
    request=message.split('\r\n')[0].split(' ')
    if(request[HTTPprotocol]=='GET'):
        response(request[requestedResource],request[HTTPVersion])
    connectionSocket.close()