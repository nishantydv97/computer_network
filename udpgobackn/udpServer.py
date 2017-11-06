import socket
host='127.0.0.1'
port=5000
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
print "server is waiting for connections "
data,addr=s.recvfrom(1024)
print "connection established from the client :"+str(addr)
#adding error in the file
data=list(str(data))
data[4]=0
t=0
for i in data:
	if i!=0:
		print "data recieved are :"+str(i)
		t+=1
	else:
		print "packet no :"+str(t)+" is missing resend after packet no "+str(t)
		break
s.sendto(str(t),addr)
data,addr=s.recvfrom(1024)
data=list(str(data))
for i in data:
	print "data recieved are :"+i
s.close()
