nombre_etudiants_18_25
4

mysql -u root -p laplateforme -e "SELECT COUNT(*) AS nombre_etudiants_18_25 FROM etudiants WHERE age BETWEEN 18 AND 25" > Job21.sql