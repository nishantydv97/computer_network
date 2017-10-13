import sys
print('enter the ip address')
ip = [int(i) for i in input().strip().split('.')]
if ip[0] > 0 and ip[0] < 128:
    print("given ip is of class A")
    mask = '255.0.0.0'
    print(mask)
elif ip[0] > 127 and ip[0] < 192:
    print("given ip is of calss B")
    mask = '255.255.0.0'
    print(mask)
elif ip[0] > 191 and ip[0] < 224:
    print("given ip is of class C")
    mask = '255.255.255.0'
    print(mask)
elif ip[0] > 223 and ip[0] < 239:
    print("given ip is of class D")
    mask = '255.0.0.0'
    print(mask)
mask1 = [int(i) for i in mask.split('.')]
print('network address is ')
for i in range(4):
    k = (ip[i])
    m = (mask1[i])
    print m and k,
    ptint('helllo')
