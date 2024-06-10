from scapy.all import *

# Exercício 10: Implementar um sniffer de pacotes
# https://scapy.readthedocs.io/en/latest/usage.html#asynchronous-sniffing
a = sniff(count=30)
a.nsummary()

print('\n----------------------------------------------------------------------------\n')

# Exercício 11: Implementar um programa para executar port scanning e Traceroute
# https://scapy.readthedocs.io/en/latest/usage.html#tcp-port-scanning
res, unans = sr( IP(dst="187.16.106.206" )
                /TCP(flags="S", dport=(1,100)))
res.nsummary( lfilter=lambda s,r: (r.haslayer(TCP) and (r.getlayer(TCP).flags & 2)) )

print('\n')

# https://scapy.readthedocs.io/en/latest/usage.html#tcp-traceroute
ans, unans = sr(IP(dst="187.16.106.206", ttl=(4,25),id=RandShort())/TCP(flags=0x2))
for snd, rcv in ans:
    print(snd.ttl, rcv.src, isinstance(rcv.payload, TCP))

print('\n----------------------------------------------------------------------------\n')

# Exercício 12: Implementar um programa que detecta ARP spoofing
# https://scapy.readthedocs.io/en/latest/api/scapy.layers.inet.html#scapy.layers.inet.connect_from_ip
def arp_spoof_detection(packet):
  print("ARP Reply detected from: " + packet[ARP].hwsrc + " for IP: " + packet[ARP].psrc)

sniff(prn=arp_spoof_detection, filter="arp", store=0, count=1)

