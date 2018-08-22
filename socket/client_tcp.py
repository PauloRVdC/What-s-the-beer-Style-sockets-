import socket
import sys

# Endereco IP do Servidor
SERVER = '127.0.0.1'
# Porta que o Servidor esta escutando
PORT = 5002
tcp = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
dest = (SERVER, PORT)
tcp.connect(dest)

word = tcp.recv(1024).decode()
if word[:9] == 'GAME OVER':
	print(word + "Pontuação: " + word[9:])
	sys.exit()
msg = input("Acerte a Palavra, " + word + ": ")
while True:
    tcp.send(msg.encode())
    word = tcp.recv(1024).decode()
    if word[:9] == 'GAME OVER':
    	print(word[:9] + "! Pontuação: " + word[9:])
    	sys.exit()
    msg = input("Acerte a Palavra, " + word + ": ")
tcp.close()