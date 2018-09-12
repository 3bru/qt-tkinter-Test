import sqlite3, os

con = sqlite3.connect('database.sqlite')
im = con.cursor()

tablo = """CREATE TABLE IF NOT EXISTS writes(day, topic, texti)"""

deger = """INSERT INTO writes VALUES('oneDay', 'nmap', 'nmaple ilgili bisiler')"""

im.execute(tablo)
im.execute(deger)
con.commit()
im.execute("""SELECT * FROM writes""")
veriler = im.fetchall()
print(veriler)
