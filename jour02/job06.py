import mysql.connector

# se connecter à la base de données
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@Jedeviles88",
  database="laplateforme"
)

# créer un curseur pour exécuter des requêtes
cursor = mydb.cursor()

# exécuter la requête
cursor.execute("SELECT SUM(capacite) FROM salles;")

# récupérer le résultat
result = cursor.fetchone()[0]

# afficher le résultat
print(f"La somme des capacités des salles est de {result} personnes.")

# fermer le curseur et la connexion à la base de données
cursor.close()
mydb.close()
