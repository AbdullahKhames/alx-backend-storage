-- create table with unique index
CREATE TABLE users IF NOT EXISTS contacts
( id INT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(30) NOT NULL,
  name VARCHAR(25),
  CONSTRAINT email_unique UNIQUE (email)
);
