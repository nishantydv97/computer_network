import socket
host='127.0.0.1'
port=5001
server=('127.0.0.1',5000)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
z=raw_input("enter the data you want to sent to the  server : ->")
s.sendto(z,server)
data,addr=s.recvfrom(1024)
print "connection established from the server "+str(addr)
k=0
for i in range(int(data)):
	print "acknowlegment receved for packet no "+str(i)
	k=i
print "resending packet after packet no :"+str(k)
s.sendto(z[int(data):9999],addr)
it=int(data)
while it < len(z):
	print "acknowlegment receved for packet no "+str(it)
	it+=1
