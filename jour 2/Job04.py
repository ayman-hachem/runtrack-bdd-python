import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="LaPlateforme"
)
cursor = conn.cursor()

# Exécution de la requête pour récupérer les noms et les capacités des salles
cursor.execute("SELECT nom, capacite FROM salle")

# Récupération des résultats
resultats = cursor.fetchall()

# Affichage des résultats en console
for resultat in resultats:
    print("Nom de la salle :", resultat[0])
    print("Capacité de la salle :", resultat[1])
    print()

# Fermeture de la connexion à la base de données
conn.close()
