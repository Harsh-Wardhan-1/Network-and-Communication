import socket
msgFromClient = "Hi this is UDP Server"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024
# Creating udp socket AT Client
udpClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# send to server using udp created address
udpClientSocket.sendto(bytesToSend, serverAddressPort)
# receive the data from the server
msgFromServer = udpClientSocket.recvfrom(bufferSize)
print(msgFromServer)
