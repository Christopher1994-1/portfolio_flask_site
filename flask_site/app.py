import sqlite3



db = sqlite3.connect('products.db')

cur = db.cursor()


# cur.execute('''CREATE TABLE prods
#              (id INTEGER PRIMARY KEY,
#              name TEXT,
#              price TEXT,
#              category TEXT,
#              description TEXT,
#              image_url TEXT);''')

name = "Hybrid Product Two"
price = "8.99"
cat = "Hybrid"
id = 1
des = "This is a demo description for the demo website Growth, if you like this demo website place contact AvrlineTech for more information about where to purchase this template"
image_url = "https://i.ibb.co/RNk0DGY/indica1.png"

# cur.execute("""INSERT INTO prods (name, price, category, description, image_url) VALUES (?,?,?,?,?)""",
#             (name, price, cat, des, image_url))

# cur.execute("DELETE FROM prods"); print("deleted all...")

for row in cur.execute("SELECT * FROM prods"):
    print()
    print(row)

db.commit()
db.close()
    
    