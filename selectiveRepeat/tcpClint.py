'''

============================================================================
 Name        : tcpClient.py
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
	s.connect((host, port))
	message=''
	message = raw_input("enter the data you want to send -> ")
	s.send(message)
	m1=list(message)
	data = s.recv(1024)
	data1=list(str(data))
#	print 'Received from server raw is: ' + str(data)
#	print data1
	j=1
	t=0
	for i in data1:
		if i !='0':
			print "acknowlegment receaved for frame no :"+str(j)
		else:
			print "frame no "+str(j)+" is missing"
			t=j
		j+=1
	s.send(str(message[t-1]))
	print "sending again frame no : "+str(t)
	s.close()

if __name__ == '__main__':
	Main()
