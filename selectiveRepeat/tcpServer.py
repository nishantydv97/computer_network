'''

============================================================================
 Name        : tcpServer.py
 Author      : Nishant
 Version     :
 Copyright   : public
 Description : Hello World in Python, Ansi-style
============================================================================

'''

import socket

def Main():
	host = '127.0.0.1'
	port = 5000
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host,port))
	print "serveer started :"
	s.listen(1)
	c, addr = s.accept()
	print "Connection from: " + str(addr)
	data = c.recv(1024)
#creating error in the code
#	 print "from connected user: " + str(data)
#	 data = raw_input("enter the data you want to send ->")
	data1=list(str(data))
	data1[5]='0'
	for i in data1:
		if i!='0':
			print "recieved data is "+i
	data1="".join(data1)
#	print "sending data is :"+data1
#	 print "sending: " + str(data)
	c.send(data1)
	data=c.recv(1024)
	print "frame received is "+str(data)+" at position : "+'6'
	c.close()

if __name__ == '__main__':
	Main()
