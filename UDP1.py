import socket
localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
msgFromServer = "hello there"
bytesToSend = str.encode(msgFromServer)
# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server is up and running")
# Listen for incomind datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    ClientMsg = "Message from Client:{}".format(message)
    ClientIP = "Client IP Address:{}".format(address)
    print(ClientMsg)
    print(ClientIP)
    # Sending a reply to Client
    UDPServerSocket.sendto(bytesToSend, address)
