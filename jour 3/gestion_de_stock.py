import tkinter as tk
from tkinter import ttk
from tkinter import *
import mysql.connector

# Fonction pour afficher les données depuis MySQL dans le tableau Tkinter
def afficher_donnees():
    # Effacer les données existantes dans le tableau
    tableau.delete(*tableau.get_children())

    # Connexion à la base de données
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="store"
    )
    cursor = conn.cursor()

    # Exécution de la requête
    cursor.execute("SELECT product.ID, product.Nom, product.Description, product.Prix, product.Quantite, category.Nom FROM product LEFT JOIN category ON product.id_category = category.id")

    # Récupération du résultat
    resultat = cursor.fetchall()

    # Ajout des données récupérées depuis MySQL au tableau
    for row in resultat:
        tableau.insert("", "end", values=row)

    # Fermeture de la connexion à la base de données
    conn.close()

# Fonction pour ajouter un élément dans la base de données
def ajouter_element():
    # Récupérer les données depuis les champs d'entrée
    nom = entry_nom.get()
    description = entry_description.get()
    prix = entry_prix.get()
    quantite = entry_quantite.get()
    id_category = entry_id_category.get()  # Récupérer la valeur de id_category

    # Connexion à la base de données
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="store"
    )
    cursor = conn.cursor()

    # Exécution de la requête d'insertion
    cursor.execute("INSERT INTO product (Nom, Description, Prix, Quantite, id_category) VALUES (%s, %s, %s, %s, %s)",
                   (nom, description, prix, quantite, id_category))

    # Commit des changements
    conn.commit()

    # Fermeture de la connexion à la base de données
    conn.close()

    # Rafraîchir les données affichées dans le tableau
    afficher_donnees()

# Fonction pour supprimer un élément de la base de données
def supprimer_element():
    # Récupérer l'ID de l'élément à supprimer
    selected_item = tableau.selection()[0]
    element_id = tableau.item(selected_item)['values'][0]  # Supposant que l'ID soit dans la première colonne

    # Connexion à la base de données
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="store"
    )
    cursor = conn.cursor()

    # Exécution de la requête de suppression
    cursor.execute("DELETE FROM product WHERE ID = %s", (element_id,))

    # Commit des changements
    conn.commit()

    # Fermeture de la connexion à la base de données
    conn.close()

    # Rafraîchir les données affichées dans le tableau
    afficher_donnees()

# Fonction pour modifier un élément de la base de données
def modifier_element():
    # Récupérer les données depuis les champs d'entrée
    selected_item = tableau.selection()[0]
    element_id = tableau.item(selected_item)['values'][0]  # Supposant que l'ID soit dans la première colonne
    nom = entry_nom.get()
    description = entry_description.get()
    prix = entry_prix.get()
    quantite = entry_quantite.get()
    id_category = entry_id_category.get()  # Récupérer la valeur de id_category

    # Connexion à la base de données
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="store"
    )
    cursor = conn.cursor()

    # Exécution de la requête de mise à jour
    cursor.execute("UPDATE product SET Nom=%s, Description=%s, Prix=%s, Quantite=%s, id_category=%s WHERE ID=%s",
                   (nom, description, prix, quantite, id_category, element_id))

    # Commit des changements
    conn.commit()

    # Fermeture de la connexion à la base de données
    conn.close()

    # Rafraîchir les données affichées dans le tableau
    afficher_donnees()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Données de la base de données")

# Création du tableau
tableau = ttk.Treeview(root, columns=("ID", "Nom", "Description", "Prix", "Quantité", "Nom de la catégorie"), show="headings")

# Définition des en-têtes de colonnes
tableau.heading("ID", text="ID")
tableau.heading("Nom", text="Nom")
tableau.heading("Description", text="Description")
tableau.heading("Prix", text="Prix")
tableau.heading("Quantité", text="Quantité")
tableau.heading("Nom de la catégorie", text="Nom de la catégorie")  # Ajout de l'en-tête Nom de la catégorie

# Alignement du contenu des cellules
for col in tableau["columns"]:
    tableau.column(col, anchor="center")

# Affichage du tableau
tableau.pack(expand=True, fill="both")

# Bouton pour afficher les données depuis MySQL dans le tableau
bouton_afficher = Button(root, text="Afficher les données", command=afficher_donnees)
bouton_afficher.pack()

# Création des champs d'entrée et des boutons pour ajouter, supprimer et modifier
label_nom = Label(root, text="Nom :")
label_nom.pack()
entry_nom = Entry(root)
entry_nom.pack()

label_description = Label(root, text="Description :")
label_description.pack()
entry_description = Entry(root)
entry_description.pack()

label_prix = Label(root, text="Prix :")
label_prix.pack()
entry_prix = Entry(root)
entry_prix.pack()

label_quantite = Label(root, text="Quantité :")
label_quantite.pack()
entry_quantite = Entry(root)
entry_quantite.pack()

label_id_category = Label(root, text="ID Category :")  # Ajout du label pour id_category
label_id_category.pack()
entry_id_category = Entry(root)  # Ajout du champ pour id_category
entry_id_category.pack()

# Bouton pour ajouter un élément
bouton_ajouter = Button(root, text="Ajouter", command=ajouter_element)
bouton_ajouter.pack()

# Bouton pour supprimer un élément
bouton_supprimer = Button(root, text="Supprimer", command=supprimer_element)
bouton_supprimer.pack()

# Bouton pour modifier un élément
bouton_modifier = Button(root, text="Modifier", command=modifier_element)
bouton_modifier.pack()

root.mainloop()
