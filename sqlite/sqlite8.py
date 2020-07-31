import sqlite3
from sqlite2 import *
"""
Retrieve relational data from projects and tasks tables
"""

if __name__ == '__main__':
    database = "pythonsqlite.db"
    conn = create_connection(database)
    c = conn.cursor()
    try:
        t = (111,)
        for row in c.execute('select * from projects where id=?',t):
            print(row)

        for row in c.execute('select * from tasks where project_id=?',t):
            print(row)

    except Exception as error:
        print("Error:", error)
    conn.close()
    print("Done.")
