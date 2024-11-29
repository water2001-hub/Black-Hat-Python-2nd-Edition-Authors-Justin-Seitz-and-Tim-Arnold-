import socket



target_host = "127.0.0.1"
target_port = 9987



#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket.SOCK_DGRAM indicates UDP client.



#send some data
client.sendto(b"AAABBBCCC",(target_host,target_port)) 
"""
we don't use send() like TCP client since UDP is connectionless protocol,
while sendto() can specify the destination as a UDP client
"""



#receive some data
data, addr = client.recvfrom(4096)
"""
recvfrom() function returns two items:
data: The received data (in bytes).
address: A tuple containing the sender's IP address and port.
"""


print(data.decode())
client.close()
