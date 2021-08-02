#!/usr/bin/python3
# log internet access once every time you manually run it - using SQLite 
from datetime import datetime
import time 
import sqlite3
import random
import sys
import http.client as httplib

# ready repeater
starttime = time.time()
seconds = 14.995


while True:

	# database connection
	con = sqlite3.connect('./db/ic_log1_2020-08-01_manual.db')
	cur = con.cursor()

	# db table: iclog (date real, ic integer, error text)

	def populate_db(ts, outage, err):
		cur.execute("INSERT INTO iclog VALUES (?, ?, ?)", (ts, outage, err,))
		con.commit()
		
		cur.execute('SELECT * FROM iclog ORDER BY date DESC LIMIT 1')
		print(cur.fetchone())

		con.close()

	def log_to_db(ts, outage, note):
		cur.execute("INSERT INTO iclog VALUES (?, ?, ?)", (ts, outage, note,))
		con.commit()
		con.close()

	# make a new log entry at a maximum of twice a minute (each 30 seconds)
	treshold_time = 30

	def check_treshold(ts, treshold_time):
		if time.time() > ts+treshold_time:
			return True 
		else:
			return False

	def ic(note):
		ic = dict()
		ic['ts'] = time.time()
		ic['outage'] = 0
		ic['note'] = note
		return ic

	# 1. check if there's an outage (1 yes, there's an outage vs. 0 no, there's no outage)

	# Choose a random server, to lessen the load on any single server, and thus lessen the chance of being banned
	servers = ['1.1.1.1','1.0.0.1', '4.2.2.1','4.2.2.2','4.2.2.3','4.2.2.4','4.2.2.5','4.2.2.6','8.8.4.4','8.8.8.8','9.9.9.9','8.26.56.26','8.20.247.20','149.112.112.112','208.67.220.220','208.67.222.222', '80.202.2.2', '217.13.0.2']
	random_pick = random.choice(servers)
	sys.stdout.write(str(datetime.now()))
	sys.stdout.write(" Testing ")
	sys.stdout.write(random_pick)

	def head(server):
		dns_port = 53
		c = httplib.HTTPConnection(server, dns_port, timeout=1.0)

		try:
			c.request("HEAD", "/")
			sys.stdout.write(" Online \n")
			return ic(server)

		# except httplib.HTTPException as err:
		except Exception as err:
			sys.stdout.write(" " + str(err) + "\n")
			return ic(str(err))

		finally:
			c.close()

	# 2. store the answer in memory (yes or no + timestamp + error if available)
	test = head(random_pick)

	# 3. get last entry of db

	# Select the last row and show it
	cur.execute('SELECT * FROM iclog ORDER BY date DESC LIMIT 1')
	db_result = cur.fetchone()


	# if there is 0 outage:
	if(test['outage']==0):

		# if there's no records already...
		if (db_result == None):
			# ...then record the 1st one
			print("run 1st SQL")
			log_to_db(test['ts'], test['outage'], test['note'])

		# if there's a change since last record...
		if(db_result[1] == 1):
			# ...then run SQL immediately
			print("Run SQL: Connection restored")
			log_to_db(test['ts'], test['outage'], test['note'])
		# otherwise do nothing

	# But if there IS an outage...
	else:
		print("There's an internet outage...")

		# ...and if there's a change since last record...
		if(db_result[1] == 0):
			# ...then run SQL immediately
			print("Run SQL: Internet outage stored...")
			log_to_db(test['ts'], test['outage'], test['note'])

		# But if there is no change since the last record...
		else:

			# ...then check treshold instead, and if it's over...
			if (time.time() > test['ts']+treshold_time):
				# ... then run SQL if it's over
				print("Run SQL: Still internet outage...")
				log_to_db(test['ts'], test['outage'], test['note'])
			# Otherwise do nothing.

	# make timestame human readable
	def ts_to_txt(ts):
		return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

	# wait a little until loop restarts
	time.sleep(seconds - ((time.time() - starttime) % seconds))
