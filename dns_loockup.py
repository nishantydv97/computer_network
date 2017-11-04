'''

============================================================================
 Name        : dns.py
 Author      : Nishant
 Version     :
 Copyright   : public
 Description : Hello World in Python, Ansi-style
============================================================================

'''

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

'''

nishant@nishant-Inspiron-3542:~/computer_network$ python3 dns_loockup.py 
host name of this pc is :nishant-Inspiron-3542
ip of this pc is127.0.1.1
enter the site name
www.google.com
Information of ipv4 address
(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('216.58.196.100', 0))
(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_DGRAM: 2>, 17, '', ('216.58.196.100', 0))
(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_RAW: 3>, 0, '', ('216.58.196.100', 0))
Information of ipv6 address
(<AddressFamily.AF_INET6: 10>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('2404:6800:4007:806::2004', 0, 0, 0))
(<AddressFamily.AF_INET6: 10>, <SocketKind.SOCK_DGRAM: 2>, 17, '', ('2404:6800:4007:806::2004', 0, 0, 0))
(<AddressFamily.AF_INET6: 10>, <SocketKind.SOCK_RAW: 3>, 0, '', ('2404:6800:4007:806::2004', 0, 0, 0))
enter the ip address
8.8.8.8
('google-public-dns-a.google.com', [], ['8.8.8.8'])
nishant@nishant-Inspiron-3542:~/computer_network$ ^C


'''
