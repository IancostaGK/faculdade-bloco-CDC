import socket
import json

def main():
  host = '127.0.0.1'
  port = 12345

  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect((host, port))

  welcome_msg = client_socket.recv(1024)
  print(welcome_msg.decode())

  candidates_raw = client_socket.recv(1024).decode()
  if candidates_raw:
    candidates = json.loads(candidates_raw)
    print("Candidatos disponíveis:")
    for idx, candidate in enumerate(candidates):
      print(f"{idx + 1}. {candidate}")

  while True:
    choice = input("Digite o número do candidato para votar (ou 'sair' para sair, ou '0' para ver a quantidade de votos por candidato): ")
    if choice.lower() == 'sair':
      client_socket.send(choice.encode())
      break
    elif choice == '0':
      client_socket.send(choice.encode())
      vote_counts_raw = client_socket.recv(1024).decode()
      if vote_counts_raw:
        vote_counts = json.loads(vote_counts_raw)
        print("Quantidade de votos por candidato:")
        for candidate, count in vote_counts.items():
          print(f"{candidate}: {count}")
    else:
      try:
        choice = int(choice)
        if 1 <= choice <= len(candidates):
          client_socket.send(str(choice).encode())
        else:
          print("Opção inválida. Por favor, escolha um número válido.")
      except ValueError:
        print("Opção inválida. Por favor, escolha um número válido.")

  client_socket.close()

if __name__ == "__main__":
  main()

