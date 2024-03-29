-- Creates a stored procedure AddBonus
-- that adds a new correction for a student.

DELIMITER //
CREATE PROCEDURE AddBonus
(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN

    -- insert the project if does not already exists
    INSERT INTO projects (name)
    SELECT project_name  
    WHERE project_name NOT IN (SELECT name FROM projects);

    INSERT INTO corrections 
    VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END//
