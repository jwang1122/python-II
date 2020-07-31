from sqlite2 import *
"""
Update record in database
"""
if __name__ == '__main__':
    conn = create_connection("mydb.db")
    c = conn.cursor()
    t = ('BUY','IBM')
    c.execute('update stocks set qty=1500 where trans=? and symbol=?',t)
    conn.commit()
    for row in c.execute("select * from stocks"):
        print(row)

    conn.close()