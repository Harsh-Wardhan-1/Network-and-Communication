def b2d(n):
    s = 0
    for i in range(len(n)):
        j = len(n)-i-1
        s = s + (2**i)*int(n[j])
    return s


def bNOT(B):
    B1 = ''
    for i in B:
        if i == '0':
            B1 = B1+'1'
        else:
            B1 = B1+'0'
    return B1


def AND(b1, b2):
    if b1 == '1' and b2 == '1':
        return '1'
    else:
        return '0'


def OR(b1, b2):
    if b1 == '0' and b2 == '0':
        return '0'
    else:
        return '1'


def bAND(B1, B2):
    ans = ''
    for i in range(len(B1)):
        ans = ans + AND(B1[i], B2[i])
    return ans


def bOR(B1, B2):
    ans = ''
    for i in range(len(B1)):
        ans = ans + OR(B1[i], B2[i])
    return ans


def a_c():
    IP = input("Enter IP address in binary:")
    MASK = input("Mask in binary:")
    l1 = IP.split()
    l2 = MASK.split()
    mask = ''
    for m in l2:
        mask = mask + m
    print("Number of addressses:", b2d(bNOT(mask))+1)
    print("1st address:")
    first = ''
    for i in range(len(l1)):
        first = first + bAND(l1[i], l2[i])+"."
    print(first[0:len(first)-1])
    print("last address:")
    l22 = []
    for var in l2:
        l22.append(bNOT(var))
    last = ''
    for i in range(len(l1)):
        last = last + bOR(l1[i], l22[i])+"."
    print(last[0:len(last)-1])


a_c()
