#QUESTO SCRIPT VA AVVIATO PER PRIMO
import socket
server_socket = socket.socket()
host = '127.0.0.1' #QUESTO E' IL MIO IP LOCALE
port = 7654 #Questa è la porta che ho settato
server_socket.bind((host, port))
server_socket.listen(1)
conn, addr_p = server_socket.accept() #accept è un medoto
print(f"Connected by {addr_p}\n") #tupla, quello che è all'interno non è modificabile
#conn.sendall('Indicami il tuo username'.encode())
conn.sendall(b'Indicami il tuo username: ') #b sta per bytes #dopo username ho messo lo spazio
username = conn.recv(1024).decode()
print(username)
conn.sendall(b'Indicami la tua password: ') #b sta per bytes #dopo username ho messo lo spazio
password = conn.recv(1024).decode()
print(password)
conn.close()
server_socket.close()
