import socket

def Main():
    host = '127.0.0.1'
    port = 5001
    server = ('127.0.0.1',5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    message=''
    while message != 'q':
        message = raw_input("enter the data you want to send or q to quit-> ")
        s.sendto(message, server)
        data, addr = s.recvfrom(1024)
        print 'Received from server: '+str(addr) + str(data)   
    s.close()

if __name__ == '__main__':
    Main()

