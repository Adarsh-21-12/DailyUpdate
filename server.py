import socket

s = socket.socket()
print("Socket created")

s.bind(('localhost', 9999))

s.listen(3)
print("Waiting")

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("Client connected", addr)
    
    c.send(bytes("Welcome here", 'utf-8'))

    c.close()



import socket

s = socket.socket()

s.bind("localhost", 9999)

s.listen(5)

while True:
    client_socket, client_address = s.accept()

    c.send("Welcome", 'utf-8')
    c.close()

