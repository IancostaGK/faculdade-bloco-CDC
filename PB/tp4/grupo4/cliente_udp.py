import socket

SERVER_ADDRESS = ('localhost', 12345)  
# Criando o socket UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.sendto(b'Hello, UDP Server!', SERVER_ADDRESS)
    data, _ = sock.recvfrom(1024)

print('Mensagem recebida do servidor UDP:', data.decode())
