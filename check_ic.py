#!/usr/bin/python3
# Check your internet connection with a touch of randomness!
import socket
import random
from datetime import datetime

# Timestamp for the logs (because time is important!)
print("Timestamp:", datetime.now())

### 
# Test #1: The Localhost Reality Check
# (Is your internet really down, or are we just talking to ourselves?)

ip_address = socket.gethostbyname(socket.gethostname())

if ip_address == "127.0.0.1":
    print("No internet detected. You're talking to yourself (localhost IP: " + ip_address + ")")
else:
    print("You're online! (LAN IP address: " + ip_address + ")")

### 
# Test #2: Ping-a-Server
# (Let's see if one of these DNS servers will talk to us)

# A delightful mix of DNS servers to randomly choose from
servers = [
    '1.1.1.1', '4.2.2.1', '4.2.2.2', '4.2.2.3', '4.2.2.4', 
    '4.2.2.5', '4.2.2.6', '8.8.4.4', '8.8.8.8', 
    '208.67.220.220', '208.67.222.222', '80.202.2.2', '217.13.0.2'
]
random_pick = random.choice(servers)

def is_connected():
    # Set up the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)

    try:
        # Try to resolve the randomly picked server
        host = socket.gethostbyaddr(random_pick)[0]
        return (True, "Connected to server: " + host)
  
    except OSError as err:
        # Uh-oh, something went wrong. No connection?
        return (False, "Connection failed: " + str(err))
  
    finally:
        s.close()

test = is_connected()
print("Connection status:", test[0], "-", test[1])

###
# Test #3: The Mystery Test
# (What will it be? Who knows? Stay tuned!)
# Pssst! Maybe this is where you'll add your own awesome test code.
