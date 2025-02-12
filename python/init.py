import mariadb
import sys
import re

try:
    conn = mariadb.connect(
        user="mysqlusr",
        password="mysqlpwd",
        host="database",
        port=3306,
        database="parc"
    )
    cur = conn.cursor()

    # Fonction pour exécuter les fichiers SQL avec debug
    def execute_sql_file(filename):
        with open(filename) as f:
            fichier = f.read()
            lines = fichier.split(";")  # Séparation des requêtes SQL
            for index, line in enumerate(lines):
                line = line.strip()  # Supprime les espaces et les sauts de ligne inutiles
                line = re.sub("\s+", " ", line)  # Nettoie les espaces multiples
                
                if line:  # Éviter d'exécuter des lignes vides
                    try:
                        print(f"Exécution SQL ({filename} - Ligne {index}): {line}", flush=True)
                        cur.execute(line)
                    except mariadb.Error as e:
                        print(f"Erreur SQL ({filename} - Ligne {index}): {e}")
                        sys.exit(1)  # Stoppe l'exécution en cas d'erreur

    # Exécute les fichiers SQL
    execute_sql_file('sql_file/init.sql')
    execute_sql_file('sql_file/create.sql')

    conn.commit()
    conn.close()

except mariadb.Error as e:
    print(f"Erreur lors de la connexion à la base de données: {e}")
    sys.exit(1)