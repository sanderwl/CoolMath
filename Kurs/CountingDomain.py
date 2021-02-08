import sqlite3

conn = sqlite3.connect("emaildb.sqlite")
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')
cur.execute('''
DROP TABLE IF EXISTS CountsOrder''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
cur.execute('''
CREATE TABLE CountsOrder (org TEXT, count INTEGER)''')

fname = 'mbox.txt'
print("Filename is ", fname)
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    org = (pieces[1].split('@')[1])#.split('.')[0]
    cur.execute('''SELECT count FROM Counts WHERE org = ?''', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) VALUES (?, 1)''', (org,))
    else:
        cur.execute('''UPDATE Counts SET count = count + 1 WHERE org = ?''', (org,))

sqlstr = '''SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'''

for i in cur.execute(sqlstr):
    print(str(i[0]), i[1])
    conn.execute('''INSERT INTO CountsOrder(org,count) VALUES(?,?)''', (i[0], i[1]))

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
DROP TABLE IF EXISTS Countsa''')

cur.execute('''ALTER TABLE CountsOrder RENAME TO Counts''')

conn.commit()
cur.close()