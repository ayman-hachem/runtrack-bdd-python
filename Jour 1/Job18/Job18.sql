id	nom	prenom	age	email
1	Betty	Spaghetti	20	betty.Spaghetti@laplateforme.io
2	Chuck	Steak	45	chuck.steak@laplateforme.io
3	John	Doe	18	john.doe@laplateforme.io
4	Binkie	Barnes	16	binkie.barnes@laplateforme.io
5	Dupuis	Gertrude	20	gertrude.dupuis@laplateforme.io
6	Dupuis	Martin	18	martin.dupuis@laplateforme.io

DELETE FROM etudiants
    -> WHERE prenom = 'John' AND nom = 'Doe';

SELECT * FROM etudiants