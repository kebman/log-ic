#!/usr/bin/python3
# log internet access once - using sqlite
import time 
import sqlite3
import socket
import random

# database connection
con = sqlite3.connect('./db/ic_log1_2020-06-22_manual.db')
cur = con.cursor()

# db table: iclog (date real, ic integer, error text)

def populate_db(ts, outage, err):
	cur.execute("INSERT INTO iclog VALUES (?, ?, ?)", (ts, outage, err,))
	con.commit()
	
	cur.execute('SELECT * FROM iclog ORDER BY date DESC LIMIT 1')
	print(cur.fetchone())

	con.close()

# make a new log entry at a maximum of twice a minute (each 30 seconds)
treshold_time = 30

def check_treshold(ts, treshold_time):
	if time.time() > ts+treshold_time:
		return True 
	else:
		return False

# 1. check if there's an outage (1 yes, there's an outage vs. 0 no, there's no outage)

# Choose a random server, to lessen the load on any single server, and thus lessen the chance of being banned
servers = ['1.1.1.1','4.2.2.1','4.2.2.2','4.2.2.3','4.2.2.4','4.2.2.5','4.2.2.6','8.8.4.4','8.8.8.8','208.67.220.220','208.67.222.222']
random_pick = random.choice(servers)
print("Testing server", random_pick)

def is_connected():
	ic = dict()

	s = socket.socket()
	s.settimeout(0.03)

	try:
		# cnx to dns server on a random port above 1023 for tcp
		s.connect((random_pick, 33061))

		ic['ts'] = time.time()
		ic['outage'] = 0
		return ic

	except OSError as err:
		ic['ts'] = time.time()
		ic['outage'] = 1
		ic['err'] = err
		return ic
	
	finally:
		s.close()

# 2. store the answer in memory (yes or no + timestamp + error if available)
test = is_connected()

# 3. get last entry of db

# Select the last row and show it
cur.execute('SELECT * FROM iclog ORDER BY date DESC LIMIT 1')
db_result = cur.fetchone()

# make timestame human readable
def ts_to_txt(ts):
	return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

# make dasta human readable and print it out
print("Last log entry:", ts_to_txt(db_result[0]), "UTC.", "Online." if db_result[1] == 0 else "Offline.", "Error: %s" %(db_result[2]) if db_result[2].isalpha() else "")

# 4. tests on last entry:

# 4*. if answer is 0 (no), and last entry is None, then make the first entry in the database :D
if test['outage'] == 0 and db_result == None:
	cur.execute("INSERT INTO iclog VALUES (?, ?, ?)", (test['ts'], test['outage'], "",))
	con.commit()
	con.close()
	print("You're connected to the Internet.")
	print("Writing first entry.")

# 4a. if answer is 0 (no), and last entry is 0 (no), then do nothing
else:
	pass 
	# print("You're connected to the Internet.")
	# print("Previous entries already exist so no updated made.")

# 4b. if answer is 0 (no), and last entry is 1 (yes), then make a new entry in the database
if test['outage'] == 0 and db_result[1] == 1:
	cur.execute("INSERT INTO iclog VALUES (?, ?, ?)", (test['ts'], test['outage'], "",))
	con.commit()
	con.close()
	print("Yippee! You're connected to the Internet again!")
	print("Logging it.")
else:
	print("You're already connected to the Internet.")
	# print("No database update needed.")

# 4c. if answer is 1 (yes), and last entry is 1 (yes), then test TRESHOLD time
if test['outage'] == 1 and db_result[1] == 1:
	print("test treshold time...")
	result = check_treshold(ts, treshold_time)

	# 4ci. if last entry timestamp is more than TRESHOLD time ago, then make a new entry in the database	
	if result == True:
		cur.execute("INSERT INTO iclog VALUES (?, ?, ?)", (test['ts'], test['outage'], "",))
		con.commit()
		con.close()
		print("No Internet connection...")
		print("Logging it as it's now past the treshold time.")

	# 4cii. if last entry timestamp is less than TRESHOLD time ago, do nothing
	else:
		print("No Internet connection...")
		print("Still too early to make a new log entry, though.")
else:
	pass
	# print("So no treshold calculated")
