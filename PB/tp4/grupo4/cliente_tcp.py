import socket

HOST = 'localhost'  
PORT = 12345        

# Criando o socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, TCP Server!')
    data = s.recv(1024)

print('Mensagem recebida do servidor TCP:', data.decode())
