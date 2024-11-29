import socket 
"""Socket is an endpoint in a two-way communication link between two programs running on a network. 
A socket is identified by an IP address and a port number
"""

target_host = "www.google.com"   #this is a string
target_port = 80                 #this is an integer



#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET indicates IPv4, SOCK_STREAM indicates TCP client.



#connect to a server (i.e., you act as a client and connect to a server)
client.connect((target_host, target_port))
""" if you act as a server, you use bind(), listen(), and accept() to listen to client's incomming 
server.bind(('127.0.0.1', 12345))  # Bind to a specific address and port
server.listen(5)  # Start listening for incoming connections
conn, addr = server.accept()  # Accept a client connection
"""

#send some data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n") #socket.send() method requires the data to be in bytes. The b prefix converts the string into a bytes object.



#receive some data
response = client.recv(4096) #Receive up to 4096 bytes




print(response.decode())
client.close() #close the connection
