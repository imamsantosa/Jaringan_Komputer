from socket import *
serverPort = 9999
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.bind(('',serverPort)) 
serverSocket.listen(1)

database = {
	'145150201111170': 'Moch Wahyu Imam Santosa',
	'145150201111171': 'Moch Wahyu Imam Santosa1',
	'145150201111172': 'Moch Wahyu Imam Santosa2',
	'145150201111173': 'Moch Wahyu Imam Santosa3',
	'145150201111174': 'Moch Wahyu Imam Santosa4'
}

print 'the server is ready to receive'
while 1 :
	connectionSocket, addr = serverSocket.accept() 
	nim = connectionSocket.recv(1024) 
	message = 'Anda tidak dikenal'
	for index, key in enumerate(database):
		if key == nim:
			message = "Nama anda adalah "+ database[key]
			break

	connectionSocket.send(message) 
	connectionSocket.close()