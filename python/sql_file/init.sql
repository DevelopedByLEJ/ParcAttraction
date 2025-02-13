SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS attraction;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS critique;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE attraction (
    attraction_id INT AUTO_INCREMENT, 
    PRIMARY KEY (attraction_id),
    nom VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    difficulte INT CHECK (difficulte BETWEEN 0 AND 5),
    visible BOOL DEFAULT TRUE
);

CREATE TABLE users (
    users_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE critique (
  critique_id INT AUTO_INCREMENT,
  attraction_id INT NOT NULL,
  PRIMARY KEY (critique_id),
  texte VARCHAR(255) NOT NULL,
  note INT NOT NULL CHECK (note BETWEEN 0 AND 5),
  nom VARCHAR(255) NOT NULL,
  prenom VARCHAR(255) NOT NULL,
  FOREIGN KEY (attraction_id) REFERENCES attraction(attraction_id) ON DELETE CASCADE
)