import socket
import json

def main():
  host = '127.0.0.1'
  port = 12345

  candidates = {
    'Candidato A': 0,
    'Candidato B': 0,
    'Candidato C': 0
  }

  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.bind((host, port))
  server_socket.listen(5)

  print("Servidor ouvindo na porta", port)

  while True:
    client_socket, addr = server_socket.accept()
    print("Conexão recebida de", addr)

    client_socket.send(b"Conexao estabelecida. Bem-vindo ao servidor de votacao!\n")
    client_socket.send(json.dumps(list(candidates.keys())).encode())

    while True:
      data = client_socket.recv(1024).decode()
      if data == '0':
        client_socket.send(json.dumps(candidates).encode())
      elif data.lower() == 'sair':
        break
      else:
        try:
          vote = int(data)
          if 1 <= vote <= len(candidates):
            candidate_name = list(candidates.keys())[vote - 1]
            candidates[candidate_name] += 1
            print("Voto recebido para", candidate_name)
          else:
            print("Opção inválida. Por favor, escolha um número válido.")
        except ValueError:
          print("Opção inválida. Por favor, escolha um número válido.")

    client_socket.close()

if __name__ == "__main__":
  main()
