-- create table with unique index
CREATE TABLE users IF NOT EXISTS contacts
( id INT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL,
  name VARCHAR(255),
  CONSTRAINT email_unique UNIQUE (email)
);
