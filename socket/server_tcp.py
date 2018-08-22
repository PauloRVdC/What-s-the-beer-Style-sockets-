import socket
from random import shuffle

#Dados do jogo
def getPalavra():
    palavras = ['Lager','Pilsner','Stout','Weiss','Porter','Bock','Indian Pale Ale','American Pale Ale',
    'Sour','Golden Ale','Kellerbier','Belgian Tripel','Altbier','Belgian Dubbel','Kölsch','Saison']
    shuffle(palavras)
    return palavras[0]

#Misturador
def misturaPalavra(p):
    l = list(p)
    shuffle(l)
    result = ''.join(l)
    return result

# Endereco IP do Servidor
HOST = ''
# Porta que o Servidor vai escutar
PORT = 5002
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
pontos = 0
while True:
    con, cliente = tcp.accept()
    print ('Conectado por ', cliente)
    palavra = getPalavra()
    con.send(misturaPalavra(palavra).encode())
    while True:
        msg = con.recv(1024).decode()
        if not msg: break
        print('Player: ', msg)
        if msg == palavra:
            pontos = pontos + 1
            palavra = getPalavra()
            con.send(misturaPalavra(palavra).encode())
        else:
            s = "GAME OVER" + str(pontos) 
            con.send(s.encode())
            break
    print ('Finalizando conexao do cliente', cliente)
    pontos = 0
    con.close()