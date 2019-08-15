import socket

def Main():

    host = '127.0.0.1' #We want the host to be this machine itself
    port = 5000

    s = socket.socket() #New socket object 's'
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port)) #Binding the socket to a port

    s.listen(1) #We only wanna listen from one connection at a time

    c, addr = s.accept()

    print "Connection from:: "+  str(addr)
   # print "enter - 'q' to close connection!"
    while True: #While we are listening from the client
        data = c.recv(1024)
        if not data:
            #If connection is closed
            break
        print "from connected user: "+  str(data)
        data = data.split()
        count = 0
        while count < len(data):
            data[count] = int(data[count])
            count = count + 1
        data = str(sorted(data)) #We are going to sort the received data and send it back
        c.send(data)
    c.close() #When the connection is closed, we close our socket

if __name__ == "__main__":
    Main()
