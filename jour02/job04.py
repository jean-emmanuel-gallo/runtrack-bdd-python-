import mysql.connector

# Connexion à la base de données
cnx = mysql.connector.connect(user='root', password='@Jedeviles88',
                              host='127.0.0.1',
                              database='laplateforme')

# Création d'un curseur
cursor = cnx.cursor()

# Requête SQL pour récupérer les noms et les capacités de la table "salles"
query = ("SELECT nom, capacite FROM salles")

# Exécution de la requête
cursor.execute(query)

# Récupération des résultats
for (nom, capacite) in cursor:
    print("{} : {}".format(nom, capacite))

# Fermeture du curseur et de la connexion à la base de données
cursor.close()
cnx.close()
