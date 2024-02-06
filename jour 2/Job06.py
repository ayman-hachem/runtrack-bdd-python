import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="LaPlateforme"
)
cursor = conn.cursor()

# Exécution de la requête pour calculer la superficie totale
cursor.execute("SELECT SUM(capacite) FROM salle")

# Récupération du résultat
resultat = cursor.fetchone()
capacite_total = resultat[0]

# Affichage du résultat
print("La capacite de La Plateforme est de :", capacite_total)

# Fermeture de la connexion à la base de données
conn.close()
