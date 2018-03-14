#!/usr/bin/python 
#!/bin/bash 

import commands 
import socket 
import sys
from thread import * 
#making bridge_node a global variable  
#bridge_node = 1 
#node_MAC = 1 

class Node :
   priority = 32768 
   port_one = 0
   port_two = 0 
   port_three = 0 
   IP_addr = 0 
   MAC_addr = 0
   bridge_node = 0  

node = Node() 

#getting IP address from specific nodes  
ips = commands.getoutput("/sbin/ifconfig | grep -i \"inet\" | cut -d: -f2 | awk '{print $1}'") 
#print ips
node.IP_addr, dont_need = ips.split("\n")
print node.IP_addr

#to get the MAC address from specific nodes 
node.MAC_addr = commands.getoutput("/sbin/ifconfig | grep -i \"HWaddr\" | awk '{print $5}'")
print node.MAC_addr 

#IP addresses of each bridge 
data_ips = [('b1', "10.0.0.1"), 
            ('b2', "10.0.0.2"),
            ('b3', "10.0.0.3"), 
            ('b4', "10.0.0.4")]; 
print data_ips 

#finding designated node and IP address from data_ips 
for i in range(len(data_ips)): 
    for j in range(len(data_ips[i])): 
          if node.IP_addr == data_ips[i][j]: 
             print "found match" 
             #print data_ips[i][j-1]
             node.bridge_node = data_ips[i][j-1]
 
#if bridge_node == b1, use port_mapping_one, etc..  
port_mapping_one = [('b1', 'b2', 3),
                    ('b1', 'b3', 1),
                    ('b1', 'b4', 2)];
 
port_mapping_two = [('b2', 'b1', 3), 
                    ('b2', 'b3', 2),
                    ('b2', 'b4', 1)];  

port_mapping_three =  [('b3', 'b1', 1),
                       ('b3', 'b2', 2), 
                       ('b3', 'b4', 3)];  

port_mapping_four = [('b4', 'b1', 2),
                     ('b4', 'b2', 1),
                     ('b4', 'b3', 3)];  

#establishing connections 
HOST = node.bridge_node
PORT = 8000 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
print "Socket created" 

s.listen(10) 
print "Socket now listening" 

def clientthread(conn): 
    conn.send('Welcome to the server. Type something and hit enter\n') 
    data = conn.recv(1024) 
    if not data: 
	  print "No data sent" 
          return 
    print data 
    if len(data) > 2 and data[:2]=="!q": 
       conn.sendall("Connection is closed\n") 
       conn.close()
       return 
    conn.close() 

while True: 
    conn, addr = s.accept() 
    print "Connected with " + addr[0] + ": " + str(addr[1]) 
 
    start_new_thread(clientthread, (conn,)) 

conn.close() 
s.close() 
