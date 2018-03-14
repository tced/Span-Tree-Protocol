#!/usr/bin/python 
#!/bin/bash 

#getting 
import commands 
#ips = commands.getoutput("/sbin/ifconfig eth0 | grep -i \"inet\" | awk '{print $2}'") 
ips = commands.getoutput("/sbin/ifconfig eth0 | grep -i 'inet addr' | awk '{print $2}'")  
print ips 

data_rows = [(ips, 0.0)]; 

print data_rows 
#fill up table with perspective IP 

#macs = commands.getoutput("/sbin/ifconfig | grep -i \"HWaddr\" | awk '{print $5}'")
#print macs 
