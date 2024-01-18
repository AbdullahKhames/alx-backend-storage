-- create table with unique index
CREATE TABLE IF NOT EXISTS users 
( id INT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL,
  name VARCHAR(255),
  country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
  CONSTRAINT email_unique UNIQUE (email)
);
