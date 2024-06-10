from scapy.all import *

def sniff_packets():
  a = sniff(count=30)
  a.nsummary()

def port_scanning_and_traceroute():
  res, unans = sr(IP(dst="187.16.106.206") / TCP(flags="S", dport=(1, 100)))
  res.nsummary(lfilter=lambda s, r: (r.haslayer(TCP) and (r.getlayer(TCP).flags & 2)))

  ans, unans = sr(IP(dst="187.16.106.206", ttl=(4, 25), id=RandShort()) / TCP(flags=0x2))
  for snd, rcv in ans:
    print(snd.ttl, rcv.src, isinstance(rcv.payload, TCP))

def detect_arp_spoofing():
  def arp_spoof_detection(packet):
    print("ARP Reply detected from: " + packet[ARP].hwsrc + " for IP: " + packet[ARP].psrc)

  sniff(prn=arp_spoof_detection, filter="arp", store=0, count=1)

def main():
  print("Escolha uma opção:")
  print("1. Sniff de pacotes")
  print("2. Port Scanning e Traceroute")
  print("3. Detectar ARP Spoofing")
  print("4. Sair")

  while True:
    choice = input("Digite o número da opção desejada: ")
    if choice == '1':
      sniff_packets()
    elif choice == '2':
      port_scanning_and_traceroute()
    elif choice == '3':
      detect_arp_spoofing()
    elif choice == '4':
      print("Saindo...")
      break
    else:
      print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
  main()
