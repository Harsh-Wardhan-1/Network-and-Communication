def b2d(n):
    s = 0
    for i in range(len(n)):
        j = len(n)-i-1
        s = s + (2**i)*int(n[j])
    return s


def bin2dec(IP):
    l = IP.split()
    ip = ""
    c = 1
    for i in l:
        if c != 4:
            ip = ip + str(b2d(i))+"."
        else:
            ip = ip + str(b2d(i))
        c = c+1
    return ip


def IPclass(IP_d):
    l = IP_d.split('.')
    a = int(l[0])
    if a in range(0, 128):
        c = 'A'
    elif a in range(128, 192):
        c = 'B'
    elif a in range(192, 224):
        c = 'C'
    elif a in range(224, 240):
        c = 'D'
    elif a in range(240, 256):
        c = 'E'
    else:
        c = 'invalid'
    return c


def net_host_id(IP_d):
    l = IP_d.split('.')
    c = IPclass(IP_d)
    if c == 'A':
        print("Network id:", l[0])
        print("Host id:", l[1]+"."+l[2]+"."+l[3])
    elif c == 'B':
        print("Network id:", l[0]+"."+l[1])
        print("Host id:", l[2]+"."+l[3])
    elif c == 'C':
        print("Network id:", l[0]+"."+l[1]+"."+l[2])
        print("Host id:", l[3])
    else:
        print("In this Class, IP address is not divided into Network and Host ID")


IP = input("Enter IP address(eg:11111111 10101010 00000000 00000000)")
IP_d = bin2dec(IP)
address_class = IPclass(IP_d)
print("Class :", address_class)
net_host_id(IP_d)
