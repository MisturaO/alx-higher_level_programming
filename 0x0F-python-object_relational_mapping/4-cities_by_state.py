#!/usr/bin/python3
"""This script lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv


db = MySQLdb.connect(host="localhost", user=argv[1],
                     passwd=argv[2], db=argv[3], port=3306)

cur = db.cursor()
cur.execute("SELECT cities.id, states.name, cities.name\
            FROM cities, states\
            WHERE states.id = cities.state_id\
            ORDER BY cities.id ASC")

rows = cur.fetchall()
for row in rows:
    print(row)
