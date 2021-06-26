#!/usr/bin/python3
import sqlite3

# create db file
con = sqlite3.connect('./db/ic_log1_2020-06-22_manual.db')
cur = con.cursor()

# create table
cur.execute('''CREATE TABLE IF NOT EXISTS iclog (date real, ic integer, error text)''')

# close the connection 
con.close()

'''
Legend:
date: a UNIX timestamp
ic: internet connection boolean true or false, 1 | 0
error: short description of the problem
'''
