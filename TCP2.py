import socket
import string

all_letters = string.ascii_letters

dict1 = {}
key = 4
for i in range(len(all_letters)):
    dict1[all_letters[i]] = all_letters[(i+key) % len(all_letters)]


c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('localhost', 9999))
print("Connected to server")
n = "This is text has been encrypted and decrpted using subsitution cipher."
c.send(n.encode())
r = c.recv(1024).decode()

dict2 = {}
for i in range(len(all_letters)):
    dict2[all_letters[i]] = all_letters[(i-key) % (len(all_letters))]

decrypt_txt = []

for char in r:
    if char in all_letters:
        temp = dict2[char]
        decrypt_txt.append(temp)
    else:
        temp = char
        decrypt_txt.append(temp)

decrypt_txt = "".join(decrypt_txt)
print(decrypt_txt)
