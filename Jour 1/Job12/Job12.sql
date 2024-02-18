id	nom	prenom	age	email
5	Dupuis	Gertrude	20	gertrude.dupuis@laplateforme.io
6	Dupuis	Martin	18	martin.dupuis@laplateforme.io

mysql -u root -p laplateforme -e "SELECT * FROM etudiants WHERE nom = 'Dupuis'" > Job12.sql