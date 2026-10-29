-- Movie Database System
-- Database and table creation script

CREATE DATABASE IF NOT EXISTS moviedb;

USE moviedb;

-- Table 1: Directors
CREATE TABLE IF NOT EXISTS Directors (
    director_id INT AUTO_INCREMENT PRIMARY KEY,
    director_name VARCHAR(255) NOT NULL UNIQUE
);

-- Table 2: Movies
CREATE TABLE IF NOT EXISTS Movies (
    title VARCHAR(255) NOT NULL PRIMARY KEY,
    release_year YEAR NOT NULL,
    genre VARCHAR(100),
    director_name VARCHAR(255),
    FOREIGN KEY (director_name)
        REFERENCES Directors(director_name)
);

-- Table 3: Reviews
CREATE TABLE IF NOT EXISTS Reviews (
    review_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    movie_title VARCHAR(255) NOT NULL,
    rating INT NOT NULL,
    CONSTRAINT chk_rating_range
        CHECK (rating BETWEEN 1 AND 10),
    FOREIGN KEY (movie_title)
        REFERENCES Movies(title)
);
