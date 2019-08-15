import socket

def main():
	host = '127.0.0.1' #setting host as the local address.
	port = 3003 #setting the port.
	
	server = ('127.0.0.1' , 3000) #The address and port from where the message will be received!

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #specifying socket family and socket type as it is UDP and not the default TCP

	s.bind((host,port)) #binding the socket 
	print "Enter 'q' to quit!"	
	message = str(raw_input("-> ")) #getting message from the user

	while True: #infinite loop
		s.sendto(message.encode('utf-8'), server)
		if message == 'q':
			break
		data, addr = s.recvfrom(1024)
		data = data.decode('utf-8')
		print "Received from server: " + data

		message = str(raw_input("-> ")) 
	s.close()

if __name__ == '__main__':
	main()	
