id	nom	prenom	age	email
1	Betty	Spaghetti	20	betty.Spaghetti@laplateforme.io

mysql -u root -p laplateforme -e "SELECT * FROM etudiants WHERE nom = 'Betty'" > Job17.sql

UPDATE etudiants
SET age = 20
WHERE prenom = 'Betty' AND nom = 'Spaghetti';