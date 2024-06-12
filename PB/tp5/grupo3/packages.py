import sys
from scapy.all import sniff, Ether, IP, TCP, UDP

def captura_pacotes(interface, count=10):
  print(f"Capturando {count} pacotes na interface {interface}")
  pacotes = sniff(iface=interface, count=count)
  return pacotes

def ler_cabecalhos(pacotes):
  for i, pacote in enumerate(pacotes):
    print(f"\nPacote {i + 1}:")
    
    if Ether in pacote:
      ether = pacote[Ether]
      print("Ethernet:")
      print(f"  MAC Destino: {ether.dst}")
      print(f"  MAC Origem: {ether.src}")
      print(f"  Tipo: {ether.type}")
  
    if IP in pacote:
      ip = pacote[IP]
      print("IP:")
      print(f"  IP Origem: {ip.src}")
      print(f"  IP Destino: {ip.dst}")
      print(f"  Versão: {ip.version}")
      print(f"  Tamanho do Cabeçalho: {ip.ihl * 4} bytes")
      print(f"  TTL: {ip.ttl}")
      print(f"  Protocolo: {ip.proto}")
  
    if TCP in pacote:
      tcp = pacote[TCP]
      print("TCP:")
      print(f"  Porta Origem: {tcp.sport}")
      print(f"  Porta Destino: {tcp.dport}")
      print(f"  Número de Sequência: {tcp.seq}")
      print(f"  Número de Confirmação: {tcp.ack}")
      print(f"  Tamanho do Cabeçalho: {tcp.dataofs * 4} bytes")
  
    elif UDP in pacote:
      udp = pacote[UDP]
      print("UDP:")
      print(f"  Porta Origem: {udp.sport}")
      print(f"  Porta Destino: {udp.dport}")
      print(f"  Comprimento: {udp.len}")

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Uso: python3 captura_pacotes.py <interface>")
    sys.exit(1)

  interface = sys.argv[1]
  pacotes_capturados = captura_pacotes(interface, count=1)
  ler_cabecalhos(pacotes_capturados)
