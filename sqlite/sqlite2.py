import sqlite3

"""
Retrieve data from table
"""

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn


if __name__ == '__main__':
    conn = create_connection("mydb.db")
    c = conn.cursor()

    sql_select = """select * from stocks"""
    for row in c.execute(sql_select):
        print(row)
    
    print("\nfind all data where symbol=IBM: ")
    t = ('IBM',)
    for row in c.execute('select * from stocks where symbol=?', t):
        print(row)
    
    print("\nfind all BUY transaction for IBM:")
    t = ('BUY','IBM')
    c.execute('select * from stocks where trans=? and symbol=?', t)
    data = c.fetchall()
    print(data)

    conn.close()