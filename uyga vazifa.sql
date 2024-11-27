-- self join
-- 1-Topshiriq
DROP TABLE IF EXISTS employees;

CREATE TABLE IF NOT EXISTS employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    manager_id INT REFERENCES employees(id)
);

INSERT INTO employees (id, name, manager_id) VALUES
(1, 'Ali', NULL),         
(2, 'Bobur', 1),          
(3, 'Dilnoza', 1),        
(4, 'Elmurod', 2),        
(5, 'Feruza', 3);            

SELECT 
    e1.name AS employee_name,
    e2.name AS manager_name
FROM 
    employees e1
LEFT JOIN 
    employees e2
ON 
    e1.manager_id = e2.id;

-- 2-Topshiriq
DROP TABLE IF EXISTS actors CASCADE;
DROP TABLE IF EXISTS movies CASCADE;
DROP TABLE IF EXISTS movie_actors;

CREATE TABLE actors (
    actor_id SERIAL PRIMARY KEY,
    actor_name VARCHAR(100) NOT NULL
);

CREATE TABLE movies (
    movie_id SERIAL PRIMARY KEY,
    movie_title VARCHAR(200) NOT NULL,
    release_year INT CHECK (release_year > 1800 AND release_year <= EXTRACT(YEAR FROM CURRENT_DATE))
);

CREATE TABLE movie_actors (
    id SERIAL PRIMARY KEY,
    movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE,
    actor_id INT REFERENCES actors(actor_id) ON DELETE CASCADE
);

INSERT INTO actors (actor_name) VALUES
('Leonardo DiCaprio'),
('Kate Winslet'),
('Brad Pitt'),
('Johnny Depp'),
('Meryl Streep');

INSERT INTO movies (movie_title, release_year) VALUES
('Titanic', 1997),
('Inception', 2010),
('Fight Club', 1999),
('Pirates of the Caribbean', 2003),
('The Devil Wears Prada', 2006);

INSERT INTO movie_actors (movie_id, actor_id) VALUES
(1, 1),
(1, 2),
(2, 1),
(3, 3),
(4, 4), 
(5, 5); 

SELECT 
    movies.movie_title, 
    actors.actor_name
FROM 
    movies 
JOIN 
    movie_actors  ON movies.movie_id = movie_actors.movie_id
JOIN 
    actors  ON movie_actors.actor_id = actors.actor_id;















