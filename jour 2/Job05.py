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
cursor.execute("SELECT SUM(superficie) FROM etage")

# Récupération du résultat
resultat = cursor.fetchone()
superficie_totale = resultat[0]

# Affichage du résultat
print("La superficie de La Plateforme est de", superficie_totale, "m2")

# Fermeture de la connexion à la base de données
conn.close()
