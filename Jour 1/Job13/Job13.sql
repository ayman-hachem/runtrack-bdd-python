id	nom	prenom	age	email
1	Betty	Spaghetti	23	betty.Spaghetti@laplateforme.io
3	John	Doe	18	john.doe@laplateforme.io
5	Dupuis	Gertrude	20	gertrude.dupuis@laplateforme.io
6	Dupuis	Martin	18	martin.dupuis@laplateforme.io

mysql -u root -p laplateforme -e "SELECT  *  FROM etudiants WHERE age BETWEEN 18 AND 25" > Job13.sql