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


IP = input("Enter IP address(eg:11111111 10101010 00000000 00000000)")
IP_d = bin2dec(IP)
print(IP_d)
