#!/usr/bin/python3
"""a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

# code should not be excuted
if __name__ == '__main__':

    # connecting to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    # running multiple database
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", [argv[4]])

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Clean up process
    cur.close()
    db.close()
