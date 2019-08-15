#importing the socket library of python.
import socket

def main():
	host = '127.0.0.1' #We set the host as the local address.
	port = 3000 #Initializing the port number.
	
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #TCP is default in python hence, we need not have done anything there, but here we need to specify the socket family - "AF_INET" and socket type - "SOCK_DGRAM"

	s.bind((host,port)) #Binding the socket to a port
	
	print "Server Started!"
	
	while True: #Infinite loop!
		data, addr = s.recvfrom(1024) #The buffer value is set and this will keep waiting to receive a UDP Message.
		data = data.decode('utf-8')
		if data == 'q':
			break
		print "Message From:: " + str(addr)
		print "From connected user : " + data
		
		i = 0
		data = data.split()
		while i < len(data):
			data[i] = int(data[i])
			i = i + 1
		data = sorted(data, reverse = 1)
		data = str(data)
		print "Sending: " + str(data)
		s.sendto(data.encode('utf-8'), addr) #Need to specify the address here again as UDP is not connected the entire time.
	
	s.close()
if __name__ == '__main__':
	main()
