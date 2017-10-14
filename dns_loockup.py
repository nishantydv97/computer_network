import socket
hostname=socket.gethostname()
ipaddr=socket.gethostbyname(hostname)
print("host name of this pc is :"+hostname)
print("ip of this pc is"+ipaddr)
print("enter the site name")
z=input()
ipv4=(socket.getaddrinfo(z,None,socket.AF_INET))
ipv6=(socket.getaddrinfo(z,None,socket.AF_INET6))
print("Information of ipv4 address")
for i in range(len(ipv4)):
     print(ipv4[i])
print("Information of ipv6 address")
for i in range(len(ipv4)):
     print(ipv6[i])
print("enter the ip address")
ip=input()
print(socket.gethostbyaddr(ip))
