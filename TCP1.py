import socket
import string

all_letters = string.ascii_letters

dict1 = {}
key = 4
for i in range(len(all_letters)):
    dict1[all_letters[i]] = all_letters[(i+key) % len(all_letters)]


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created")
s.bind(('localhost', 9999))
s.listen(3)
print("waiting for connection")
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    data = c.recv(1024).decode()
    plain_txt = data
    cipher_txt = []

    for char in plain_txt:
        if char in all_letters:
            temp = dict1[char]
            cipher_txt.append(temp)
        else:
            temp = char
            cipher_txt.append(temp)

    cipher_txt = "".join(cipher_txt)
    print(cipher_txt)
    msg = "This is text has been encrypted and decrpted using subsitution c."
    c.send(msg.encode())
    c.close()
