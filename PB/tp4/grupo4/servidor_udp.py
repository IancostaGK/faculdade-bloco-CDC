import socket

SERVER_ADDRESS = ('0.0.0.0', 12345)  

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind(SERVER_ADDRESS)
    print('Servidor UDP esperando por mensagens...')
    data, address = sock.recvfrom(1024)
    print('Mensagem recebida do cliente UDP:', data.decode())
    sock.sendto(b'Hello, UDP Client!', address)
