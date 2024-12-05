import socket
import threading
#allows the server to handle multiple client connections simultaneously by using threads.


IP = '0.0.0.0'
PORT = 9998
def main():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind((IP, PORT))
  server.listen(5)  
#max accepting 5 connection requests (i.e., if 6 incoming requests, dropping one)
  print(f'[*] Listening on {IP}:{PORT}')

  while True:
    client, address = server.accept()

#accept(): Accepts a connection from a client and returns a new socket for communication.
#client: A new socket object representing the connection with the client.
#address: A tuple containing the client’s IP address and port number.

    print(f'[*] Accepted connection from {address[0]}:{address[1]}')
    client_handler = threading.Thread(target=handle_client, args=(client,))   #passing 'client' in the handle_client() function
#Creates a new thread to handle the connected client. This allows multiple clients to be handled simultaneously.
    client_handler.start()

def handle_client(client_socket):  #passing 'client' in the argement
  with client_socket as sock:
#with statement for exception handling --> i.e., close 'sock' automatically after to avoid exception
    request = sock.recv(1024)
    print(f'[*] Received: {request.decode("utf-8")}')
    sock.send(b'ACK')

if __name__ == '__main__':
 main()
