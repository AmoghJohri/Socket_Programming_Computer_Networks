import socket

def Main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((host, port))

    #Whenever the connection succeeds, it will ask the user for a message to send
    print "Enter 'q' to close the connection!"
    message = raw_input("-> ")
    while message != 'q':
        s.send(message) #We send the message to the server
        data = s.recv(1024)
        print "Received from server: " + str(data) #Printing the message we received
        message = raw_input("-> ")

    print "Connection closed!"
    s.close()

if __name__ == "__main__":
    Main()
