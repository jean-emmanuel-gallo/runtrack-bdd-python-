import mysql.connector

# connexion à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@Jedeviles88",
  database="LaPlateforme"
)

# Exécuter la requête SQL
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM etudiants")

# Afficher les résultats
for x in mycursor:
  print(x)