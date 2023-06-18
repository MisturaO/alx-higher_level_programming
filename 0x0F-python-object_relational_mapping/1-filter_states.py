#!/usr/bin/python3
"""A script that lists all states with a name starting with 'N'"""

import MySQLdb
from sys import argv

"""so my code can only be executed when it's script is run
directly and not execute when imported into another module"""
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name\
                Like 'N%' ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)
