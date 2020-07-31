import sqlite3
"""
Insert many data row at once
"""

conn = sqlite3.connect("mydb.db")
c = conn.cursor()
# Never do this -- insecure!
# symbol = 'RHAT'
# c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print("12:",c.fetchone())

try:
    # Larger example that inserts many records at a time
    purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
                ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
                ]
    c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
    # the following is very important statement, otherwise no data will be stored into database
    conn.commit()
except Exception as error:
    print("Error:",error)
conn.close()
print("Done.")