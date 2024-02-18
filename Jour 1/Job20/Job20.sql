nombre_etudiants_mineurs
1

 mysql -u root -p laplateforme -e "SELECT COUNT(*) AS nombre_etudiants_mineurs FROM etudiants WHERE age < 18" > Job20.sql