#!/usr/bin/python3
""" script that takes in an argument and displays all values i
the states table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
from sys import argv

# code should not be excuted when imported
if __name__ == '__main__':

    # database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                       passwd=argv[2], db=argv[3])

    # ability to run multiple database
    cur = db.cursor()
    cur.execute("SELECT *FROM states WHERE BINARY name = %s", [argv[4]])

    rows = cur.fetchall()
    for x in rows:
        print(x)

        # clean process
        cur.close()
        db.close()
