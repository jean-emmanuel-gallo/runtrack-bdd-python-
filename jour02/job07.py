import mysql.connector

class Employe:
    def __init__(self, nom, prenom, salaire, id_service):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.id_service = id_service
        self.cnx = mysql.connector.connect(user='root', password='@Jedeviles88', host='localhost', database='laplateforme')
    
    def insert(self):
        cursor = self.cnx.cursor()
        query = "INSERT INTO employes (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (self.nom, self.prenom, self.salaire, self.id_service)
        cursor.execute(query, values)
        self.cnx.commit()
        cursor.close()
    
    def update(self):
        cursor = self.cnx.cursor()
        query = "UPDATE employes SET nom = %s, prenom = %s, salaire = %s, id_service = %s WHERE id = %s"
        values = (self.nom, self.prenom, self.salaire, self.id_service, self.id)
        cursor.execute(query, values)
        self.cnx.commit()
        cursor.close()
    
    def delete(self):
        cursor = self.cnx.cursor()
        query = "DELETE FROM employes WHERE id = %s"
        values = (self.id,)
        cursor.execute(query, values)
        self.cnx.commit()
        cursor.close()
    
    @staticmethod
    def get_all():
        cnx = mysql.connector.connect(user='root', password='@Jedeviles88', host='localhost', database='laplateforme')
        cursor = cnx.cursor()
        query = "SELECT employes.*, services.nom FROM employes JOIN services ON employes.id_service = services.id"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        return result
