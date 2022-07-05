# Modules
from scapy.all import *
import time
import os


# Variables
index = """
 _____   _   _   _____   _____  
|  _  \ | | | | /  ___| |  _  \ 
| | | | | |_| | | |     | |_| | 
| | | | |  _  | | |     |  ___/ 
| |_| | | | | | | |___  | |     
|_____/ |_| |_| \_____| |_|     v1.0
"""
line = "================================================="


# Index
os.system('clear')
print(index)
print(line)


# Function
def listen_dhcp():
    sniff(prn=print_packet, filter='udp and (port 67 or port 68)')
    
def print_packet(packet):
    target_mac, requested_ip, hostname, vendor_id = [None] * 4
    
    if packet.haslayer(Ether):
        target_mac = packet.getlayer(Ether).src
    dhcp_options = packet[DHCP].options
    
    for item in dhcp_options:
        try:
            label, value = item
        except ValueError:
            continue
        if label == 'requested_addr':
            requested_ip = value
        elif label == 'hostname':
            hostname = value.decode()
        elif label == 'vendor_class_id':
            vendor_id = value.decode()
    if target_mac and vendor_id and hostname and requested_ip:
        time_now = time.strftime("[%Y-%m-%d - %H:%M:%S]")
        print(f"{time_now} : {target_mac}  -  {hostname} / {vendor_id} requested {requested_ip}")


if __name__ == "__main__":
    listen_dhcp()