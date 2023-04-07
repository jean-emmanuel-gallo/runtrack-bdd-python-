import mysql.connector

# connexion à la base de données
cnx = mysql.connector.connect(user='root', password='@Jedeviles88',
                              host='localhost', database='laplateforme')
cursor = cnx.cursor()

# récupération des données de la table etage
etage_sql = "SELECT * FROM etage"
cursor.execute(etage_sql)
etage_result = cursor.fetchall()

# affichage des données de la table etage
print("Données de la table etage:")
for row in etage_result:
    print(row)

# récupération des données de la table salles
salles_sql = "SELECT * FROM salles"
cursor.execute(salles_sql)
salles_result = cursor.fetchall()

# affichage des données de la table salles
print("Données de la table salles:")
for row in salles_result:
    print(row)

# fermeture du curseur et de la connexion
cursor.close()
cnx.close()
