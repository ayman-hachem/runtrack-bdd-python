id	nom	prenom	age	email
5	Gertrude	Dupuis	20	gertrude.dupuis@laplateforme.io

mysql -u root -p laplateforme -e "SELECT * FROM etudiants WHERE prenom = 'Dupuis' AND nom = 'Gertrude'" > Job11.sql