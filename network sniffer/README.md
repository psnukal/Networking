<h1>Network-Sniffer<h1>
<br/>
<br/>
The user has to give the network range in the command line. <br/>
The program gives the IP Addresses of all the devices connected to the network in the specified range. <br/>
The program will also give the bandwidth of the network. <br/>
<br/>
1) Initially find the IPv4 IP Address of the device using 'ipconfig' command. <br/>
2) Then type the following command: python code.py -t <first 3 octets of the IP Address>.1/24 <br/>
3) Type first three octets of the IP Address from the IP Address found using ipconfig. <br/>
4) Output is displayed. <br/>
<br/>
The foloowing libraries are used. Install them before running the python code.<br/>
1) scapy.all<br/>
2) argparse<br/>
3) psutil<br/>
4) time<br/>
