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

def action(pkt):
  try:
    if pkt[Ether].src=="01:23:45:67:89:AB":
      # Loreal
      print "Dash button presed!"

    if pkt[Ether].src=="00:11:22:33:44:55":
      print "Another button presed!"
      call(["/some/command", "and", "its", "parameters"])

  except:
    print("No ether layer!")
      
while 1:
  sniff(prn=action, filter="ether src 01:23:45:67:89:AB or ether src 00:11:22:33:44:55", store=0, count=1)
  time.sleep(3)
