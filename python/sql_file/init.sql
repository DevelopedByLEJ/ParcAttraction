DROP TABLE IF EXISTS attraction;

CREATE TABLE attraction (
    attraction_id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    difficulte INT CHECK (difficulte BETWEEN 0 AND 5),
    visible BOOL DEFAULT TRUE
);

DROP TABLE IF EXISTS users;

CREATE TABLE users (
    users_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS critique;

CREATE TABLE critique (
    critique_id INT AUTO_INCREMENT PRIMARY KEY,
    texte VARCHAR(255) NOT NULL,
    note INT NOT NULL CHECK (note BETWEEN 0 AND 5),
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    attraction_id INT NOT NULL,

    CONSTRAINT fk_attraction FOREIGN KEY (attraction_id)
    REFERENCES attraction(attraction_id) ON DELETE CASCADE
);