import socket

HOST = '0.0.0.0'   
PORT = 12345       
# Criando o socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Servidor TCP esperando por conexões...')
    conn, addr = s.accept()
    with conn:
        print('Conectado por', addr)
        # Recebendo dados
        data = conn.recv(1024)
        print('Mensagem recebida do cliente TCP:', data.decode())
        # Enviando resposta
        conn.sendall(b'Hello, TCP Client!')
