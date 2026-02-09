import socket
s = socket.socket()
s.settimeout(2)
porta = 80
indirizzo = "10.0.3.215"
s.connect((indirizzo , porta))
s.sendall(b'Hello, world')
risposta = s.recv(1024)
print(risposta.decode())
s.close()