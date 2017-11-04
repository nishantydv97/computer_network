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
    while message != 'q':
        message = raw_input("enter the data you want to send -> ")
        s.send(message)
        data = s.recv(1024)
        print 'Received from server: ' + str(data)

    s.close()

if __name__ == '__main__':
    Main()
