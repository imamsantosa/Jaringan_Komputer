from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind(('', serverPort))

database = {
	'145150201111170': 'Moch Wahyu Imam Santosa',
	'145150201111171': 'Moch Wahyu Imam Santosa1',
	'145150201111172': 'Moch Wahyu Imam Santosa2',
	'145150201111173': 'Moch Wahyu Imam Santosa3',
	'145150201111174': 'Moch Wahyu Imam Santosa4'
}

print "The server is ready to receive"
while 1:
	nim, clientAddress = serverSocket.recvfrom(2048) 
	message = 'Anda tidak dikenal'
	for index, key in enumerate(database):
		if key == nim:
			message = "Nama anda adalah "+ database[key]
			break
	serverSocket.sendto(message, clientAddress)
	