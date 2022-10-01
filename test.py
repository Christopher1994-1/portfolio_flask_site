import sqlite3


db = sqlite3.connect('passwords.db')


conn = db.cursor()

# conn.execute("INSERT INTO passwords VALUES ('', '', '')")


for row in conn.execute('SELECT * FROM passwords'):
    print(row)