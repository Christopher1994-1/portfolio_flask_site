import sqlite3



db = sqlite3.connect('flask_site/products.db')

cur = db.cursor()


for i in cur.execute('SELECT * FROM prods'):
    print(i)
    
    