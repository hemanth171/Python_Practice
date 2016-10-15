import re
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

filename = '/Users/hemanth/Documents/Python_workspace/mbox.txt'
fh = open(filename)
for line in fh:
    organizations = re.findall('^From .*@(\S+)', line)
    for orgs in organizations:
        cur.execute('SELECT count from Counts where org=?',(orgs, ))
        rows = cur.fetchone()
        if rows is None:
            cur.execute('''INSERT INTO Counts(org,count) VALUES(?,1)''',(orgs, ))
        else:
            cur.execute('UPDATE Counts set count=count+1 where org=?',(orgs, ))
conn.commit()
sqlselect = 'SELECT org,count from Counts ORDER BY count DESC LIMIT 10'
rows = cur.execute(sqlselect)
for row in rows:
    print str(row[0]), row[1]

cur.close()