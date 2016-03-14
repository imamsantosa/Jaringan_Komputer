from socket import *
serverName = "localhost"
serverPort = 9999
while 1: 
	clientSocket = socket(AF_INET, SOCK_STREAM) 
	clientSocket.connect((serverName,serverPort)) 
	nim = raw_input('Input NIM:')
	clientSocket.send(nim)
	message = clientSocket.recv(1024) 
	print message
	clientSocket.close()