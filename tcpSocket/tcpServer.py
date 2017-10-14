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
    while True:
        data = c.recv(1024)
        if not data:
            break
        print "from connected user: " + str(data)
        data = raw_input("enter the data you want to send ->")
        print "sending: " + str(data)
        c.send(data)
    c.close()

if __name__ == '__main__':
    Main()
