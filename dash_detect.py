#!/usr/bin/python

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"THE BEER-WARE LICENSE" (Revision 42):
<algspd@gmail.com> wrote this file.  As long as you retain this notice you
can do whatever you want with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me a beer in return.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

def action(pkt):
      print pkt[Ether].src
      
sniff(prn=action, filter="udp and port 67 and ether dst ff:ff:ff:ff:ff:ff", store=0, count=0)
