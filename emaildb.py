import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')

cur.execute('''CREATE TABLE Counts(email TEXT, count INTEGER)''')

filename = '/Users/hemanth/Documents/Python_workspace/mbox.txt'
fh = open(filename)
for line in fh:
    if not line.startswith('From '): continue
    lsplit = line.split()
    email = lsplit[1]
    cur.execute('SELECT count from Counts where email=?',(email, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts(email,count) VALUES(?,1)''',(email, ))
    else:
        cur.execute('UPDATE Counts set count=count+1 where email=?',(email, ))
    conn.commit()

sqlselect = 'SELECT email,count from Counts ORDER BY count DESC LIMIT 10'
rows = cur.execute(sqlselect)
for row in rows:
    print str(row[0]), row[1]

cur.close()