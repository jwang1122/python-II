from sqlite2 import *
"""
Delete record in database
"""
if __name__ == '__main__':
    conn = create_connection("mydb.db")
    c = conn.cursor()
    t = ('2006-03-28',)
    c.execute('delete from stocks where date=?',t)
    conn.commit()
    for row in c.execute("select * from stocks"):
        print(row)

    conn.close()