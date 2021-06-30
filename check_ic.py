#!/usr/bin/python3
# check ic - various ways - without logging
import socket
import random
from datetime import datetime

# human readable timestamp
print(datetime.now())

###
# test #1: semi passive

ip_address = socket.gethostbyname(socket.gethostname())

if ip_address == "127.0.0.1":
    print("No internet. Your localhost is "+ ip_address)
else:
    print("Connected. LAN IP address: "+ ip_address )

###
# test #2: socket.gethostbyaddr

servers = ['1.1.1.1','4.2.2.1','4.2.2.2','4.2.2.3','4.2.2.4','4.2.2.5','4.2.2.6','8.8.4.4','8.8.8.8','208.67.220.220','208.67.222.222', '80.202.2.2', '217.13.0.2']
random_pick = random.choice(servers)

def is_connected():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.settimeout(1)

	try:
		host = socket.gethostbyaddr(random_pick)[0]
		return (True, host)
  
	except OSError as err:
		return (False, err)
	finally:
		s.close()

test = is_connected()
print("Connection:", test[0], test[1])

###
# test #3: ?
