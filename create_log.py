#!/usr/bin/python3
# SQLite Database Creator for Internet Connection Logs
# Run this first to set up your logging database!

import sqlite3
from datetime import datetime

# Generate a filename with today's date (because nobody likes outdated logs)
db_filename = './db/ic_log_' + datetime.now().strftime('%Y-%m-%d') + '_manual.db'

# Create the SQLite database file
con = sqlite3.connect(db_filename)
cur = con.cursor()

# Create the logging table (if it doesn't exist already)
cur.execute('''
    CREATE TABLE IF NOT EXISTS iclog (
        date REAL,      -- UNIX timestamp
        ic INTEGER,     -- Internet connection status: 1 (connected) | 0 (disconnected)
        note TEXT       -- A short description or error message
    )
''')

# Close the connection because we’re tidy like that
con.close()

# Inform the user of the successful creation (or lack thereof)
print(f"Database created successfully! Your logs will be saved in: {db_filename}")

'''
Legend:
- date: UNIX timestamp
- ic: Internet connection status (1 = connected, 0 = disconnected)
- note: A short description of the problem or status
'''
