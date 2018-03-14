S 164: Computer Networks Project
Win
t
er 2018
Spanning Tree 
Protocol
Submission deadline: March 15
th
2018 11:59pm
For this project, you will 
be 
implementing 
the algorithm
for the 
Spanning Tree 
Protocol
.
The 
Spanning Tree 
protocol is used to build loop 
free networks while still allowing backup links for 
fault  tolerance.  The  STP  algorithm  creates  a  spanning  tree  within  a  set  of  connected 
bridges/switches by disabling links that are not part of the spanning tree.
A.
Background
The STP algorithm is used to p
revent transmission loops, broadcast storms and unstable MAC 
address tables and f
or this project you will be programming 
a simplified version of 
the STP 
protocol 
IEEE 
802.1D.
There are several stages in the STP prot
ocol. The first involves selecting the 
ro
ot bridge. The switches 
exchange 
messages to
determine which switch will be the root bridge. 
After the root has
been determined, all other non
-
root switches need to identify the port nearest 
to the root bridge (root port)
and the
switches which don’t have a direct connection to the root 
bridge need to identify 
a designated port on 
the closest
neighboring 
switch to the root bridge.
Any port that is not a root port or designated port is put in the blocking state.
Note that in this 
d
ocument switch and bridge are both used to refer to the same device.
B.
Operation
Initially each bridge assumes it is the root and sends out a configuration message on each of its 
ports,  identifying  itself  as  the  root  and  giving  a  distance  of  0.    When  a  brid
ge  receives  a 
configuration message over a given port
it will check to see if the new message is better than the 
current best configuration message for that port.
A new configuration message is better than the current recorded information if
:
a.
It identifie
s a root with a smaller ID
b.
It identifies a root with an equal ID but a shorter distance
c.
The root ID and distance are equal but the sending bridge has a smaller ID
If the new message is better, the old information is discarded and the new information saved.
However
,
the bridge first adds a 1 to the distance to root field (hops) since this bridge is one hop 
further away from the root than the bridge that sent the message.
When a bridge receives a configuration message indicating it is not the root bridge (
i.e
.
it receives 
a message from a bridge with a smaller bridge ID)
that bridge will stop generating configuration 
messages on its own and will only forward 
configuration messages from
other bridges after first 
adding 1 to the distance field.
Also when a bridg
e receives a configuration message indicating that it is not the designated 
bridge for that port (
i.e.
it receives a message from a bridge closer to the root or equally far from 
the root but with a smaller id), the bridge stops sending configuration messag
es over that port.
2
When the system is finally stable, only the root bridge is still generating configuration messages 
and the other bridges are forwarding these messages only over ports  for which they are the 
designated bridge.
If a bridge fails  during t
his stable period and other downstream bridges do 
not receive configuration messages after a configured period, the algorithm restarts with them 
sending out BPDUs to elect a new root bridge.
C.
Phases
1.
Elect a Root Bridge
The switches elect a root bridge by e
xchanging Bridge Protocol Data Units (BPDUs). Each BPDU 
contains the
switch priority, 
MAC ID, and bridge ID. The bridge ID is the concatenation of the 
priority and the MAC address. For example a bridge with priority 32768 and MAC address 
0200.0000.1111 has
a bridge ID 32768.0200.0000.1111. The bridge IDs can only be configured in 
multiples of 4096 and the default priority in 32768. When comparing bridges, the priority is 
compared first and only if they are equal is the MAC address compared. The switch with 
the 
lowest priority or lowest MAC address 
in case of equal priorities 
will be the root. 
Each 
bridge
sends
out BPDUs out of all its ports 
2.
Place all root interfaces into a forwarding state
Once a root bridge has been selected, all its interfaces need to 
be placed into a forwarding state
i
.
e
.
can send and receive traffic and all ports are
labelled
designated ports
.
3.
Each 
non
-
root
switch selects it
s root port
By examining the configuration messages and settings for each port, the switch determines wh
ich 
por
t is closest to the root and label
s
this as the root port (RP)
4.
Remaining 
links chose
a designated port
By examining the configuration messages and settings for each port, the switch determines which 
neighbor bridge port is closest to the root and label th
is port as the designated port (DP)
5.
All other ports put in blocking state
Any other ports on the bridge that have not been classified as either a root port or designated 
port are set as blocked ports (BP)
. Blocked ports still receive data but do not do an
ything with it.
D.
Bridge Protocol Data Unit Fields
There are two types of BPDUs, the configuration BPDUs (BCPDU) for spanning tree computation 
and Topology Change Notification (TCN) BPDUs to announce changes in the network topology.
The BPDU messages will
have the format (Y, d, X) where Y is the bridge ID of the node that the 
sending bridge think
s is the root, cost to reach 
Y and
X is the bridge ID of the bridge sending the 
message.
If the speed of the networking technology is uniform at all ports, the cos
t is measured 
in terms of number of hops to the root bridge where the least number of hops is preferred. If the 
speed of the networking technology differs for each port then the cost is determined by the 

