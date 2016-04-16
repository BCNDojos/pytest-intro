import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE stocks ( date text, symbol text, qty real, price real)''')
c.execute("INSERT INTO stocks VALUES ('2006-01-05','RHAT',100,35.14)")
purchases = [('2006-01-05','RHAT',100,35.14),
             ('2006-03-28', 'IBM', 1000, 45.00),
             ('2006-04-05', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'IBM3', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?)', purchases)
conn.commit()
conn.close()