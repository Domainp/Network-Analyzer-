from scapy.all import sniff, IP

def process_packet(packet):
    if packet.haslayer(IP):
        print(f"[*] {packet[IP].src} -> {packet[IP].dst}")

print("--- Sniffer Active (Admin Mode) ---")
# store=0 keeps memory usage low
sniff(prn=process_packet, store=0, count=10)