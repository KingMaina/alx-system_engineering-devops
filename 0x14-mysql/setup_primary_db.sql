--- Set up the primary database with an entry
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	name VARCHAR NOT NULL
);
INSERT INTO nexus6 (name) VALUES ('Janet');
