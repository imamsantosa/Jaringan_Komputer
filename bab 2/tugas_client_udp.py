from socket import *
serverName = "localhost"
serverPort = 12000
while 1:
	clientSocket = socket(AF_INET, SOCK_DGRAM)
	nim = raw_input("Input NIM:") 
	clientSocket.sendto(nim, (serverName, serverPort)) 
	message, serverAddress = clientSocket.recvfrom(2048) 
	print message
	clientSocket.close()