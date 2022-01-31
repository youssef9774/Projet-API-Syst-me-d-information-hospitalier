import sqlite3
conn = sqlite3.connect ( 'database.db' )
print ("Base de données ouverte avec succès")
conn.execute ( 'CREATE TABLE etudiants (nom TEXT, addr TEXT, pin TEXT)' )
print ("Table créée avec succès")
conn.close ()

with sqlite3.connect("database.db") as con:
       cur = con.cursor()
       cur.execute("INSERT INTO etudiants(nom,addr,pin) VALUES (?,?,?)", (" John Doe" ," 122 rue paul armangot" ," 123"))
       con.commit()
con.close()