#!/usr/bin/python

import sys
from scapy.all import *

devices = set()

def PacketHandler (pkt) :

        if pkt.haslayer(Dot11) :
                
                if pkt.addr2 and (pkt.addr2 not in devices) :
                	devices.add(pkt.addr2)
                	print len(devices), pkt.addr2
                

sniff(iface = sys.argv[1], count = int(sys.argv[2]), prn = PacketHandler)