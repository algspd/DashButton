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
import time
from subprocess import call

last={}

def action(pkt):
  global test

  try:
    # First time a button is pressed, create the key in the dictionary
    if not pkt[Ether].src in last:
      last[pkt[Ether].src]=0

    # If this packet is received before 5 seconds have passed
    # from the last one for the same device, do nothing
    if last[pkt[Ether].src]+5<time.time():

      # Do something for this device
      if pkt[Ether].src=="01:23:45:67:89:AB":
        print "Dash button presed!"
  
      # Do something for this other device
      if pkt[Ether].src=="00:11:22:33:44:55":
        print "Another button presed!"
        call(["/some/command", "and", "its", "parameters"])

    # Update last packet time
    last[pkt[Ether].src]=time.time()

  except:
    # If the packet had no Ether info, just skip
    print("No ether layer!")

# Start sniffing packets, forever
sniff(prn=action, filter="ether src 01:23:45:67:89:AB or ether src 00:11:22:33:44:55", store=0, count=0)
