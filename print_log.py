#!/usr/bin/python3
# prints the outage log.
import sqlite3
from datetime import datetime

# connect to the db
con = sqlite3.connect('./db/ic_log1_2020-06-30_manual.db')
cur = con.cursor()

# convert unix timestamp float to human readable date string
def ts_to_txt(ts):
	return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

# format and show the data
for row in cur.execute('SELECT * FROM iclog ORDER BY date'): print(ts_to_txt(row[0]), "UTC.", "Online." if row[1] == 0 else "Offline.", "Note: %s" %(row[2]))

# for row in cur.execute('SELECT * FROM iclog ORDER BY date'): print(row)
# Explanation:
# print(ts_to_txt(row[0]), "UTC." # Prints the UNIX timestamp as a human readable date in the UTC time zone.
# "Online." if row[1] == 0 else "Offline." # turns 0 / False into "Online" and 1 / True into "Offline"
# "Note: %s" %(row[2]) # Shows the note, which is either a server name or an error message
con.close()
