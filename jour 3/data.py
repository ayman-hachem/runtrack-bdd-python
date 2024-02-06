import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="entreprise"
)
cursor = conn.cursor()

# Exécution de la requête
cursor.execute("SELECT * FROM employe WHERE salaire > 3000.00")

# Récupération du résultat
resultat = cursor.fetchall()

# Affichage du résultat
print(resultat)

# Fermeture de la connexion à la base de données
conn.close()
