id	nom	prenom	age	email
4	Binkie	Barnes	16	binkie.barnes@laplateforme.io
3	John	Doe	18	john.doe@laplateforme.io
5	Gertrude	Dupuis	20	gertrude.dupuis@laplateforme.io
1	Betty	Spaghetti	23	betty.Spaghetti@laplateforme.io
2	Chuck	Steak	45	chuck.steak@laplateforme.io

 mysql -u root -p laplateforme -e "SELECT * FROM etudiants ORDER BY age ASC" > Job09.sql