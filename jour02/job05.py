import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@Jedeviles88",
  database="laplateforme"
)

cursor = mydb.cursor()

query = "SELECT SUM(superficie) AS superficie_totale FROM etage;"
cursor.execute(query)

result = cursor.fetchone()

superficie_totale = result[0]
print(f"La superficie de La Plateforme est de {superficie_totale} m2")

mydb.close()
