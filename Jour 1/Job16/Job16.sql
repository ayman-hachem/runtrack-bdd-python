id	nom	prenom	age	email
4	Binkie	Barnes	16	binkie.barnes@laplateforme.io

 mysql -u root -p laplateforme -e "SELECT  *  FROM etudiants WHERE prenom LIKE 'B%'" > Job16.sql