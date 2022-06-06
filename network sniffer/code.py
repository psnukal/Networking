#Network Sniffer


import scapy.all as scapy
import argparse
import psutil
import time



#IP address
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Sepcify target ip or ip range")
    options = parser.parse_args()
    return  options

def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_packet = broadcast_packet/arp_packet
    answered_list = scapy.srp(arp_broadcast_packet, timeout=1, verbose=False)[0]
    client_list = []

    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)

    return client_list

def print_result(scan_list):
    print("IP\t\t\tMAC\n----------------------------------------")
    for client in scan_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()
result_list = scan(options.target)
print_result(result_list)


#bandwidth
last_received = psutil.net_io_counters().bytes_recv 
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_received + last_sent

while True:

    bytes_received = psutil.net_io_counters ().bytes_recv 
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_received+bytes_sent
    
    new_received=bytes_received -last_received
    new_sent=bytes_sent -last_sent
    new_total= bytes_total -last_total

    mb_new_received = new_received/ 1024
    mb_new_sent = new_sent / 1024
    mb_new_total = new_total / 1024

    print(f"{ mb_new_received:.2f} MB received,{ mb_new_sent:.2f} MB sent,{mb_new_total:.2f} MB total")

    last_received = bytes_received 
    last_sent = bytes_sent
    last_total = bytes_total

    time.sleep(1)


#THANK YOU
#MODULE AUTHOR
#PURVIK S NUKAL
