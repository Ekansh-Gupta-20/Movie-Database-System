# Movie Database System

## Project Overview
The Movie Database System is a menu-driven application developed using Python and MySQL. It allows users to manage movie details, director information, and movie ratings through a simple command-line interface.

## Technologies Used
- Python
- MySQL
- MySQL Connector for Python
- SQL

## Features
- Add director details.
- Add movies with their release year, genre, and director.
- Add ratings for existing movies.
- View all movies stored in the database.
- View movie ratings.
- Validate user inputs and handle database errors.
- Maintain relationships between directors, movies, and reviews using foreign keys.

## Database Structure

The project uses a MySQL database named `moviedb` with three tables:

**Directors**
- Stores director IDs and names.

**Movies**
- Stores movie titles, release years, genres, and director names.

**Reviews**
- Stores movie titles and their ratings.

Foreign keys maintain relationships between the tables.

## Prerequisites
- Python installed on your computer.
- MySQL Server installed and running.
- MySQL Connector for Python.

## Installation and Setup

1. Download or clone this repository.
2. Create a MySQL database named `moviedb`.
3. Create the required tables: `Directors`, `Movies`, and `Reviews`, with the appropriate primary key and foreign key constraints.
4. Install the required Python package:

   ```bash
   pip install mysql-connector-python
   ```

5. Update the database connection settings in `movie_database.py` with your own MySQL credentials.
6. Run the application:

   ```bash
   python movie_database.py
   ```

## Learning Outcomes
- Connecting Python applications to MySQL.
- Executing SQL queries using Python.
- Understanding primary keys and foreign keys.
- Performing database insert and select operations.
- Handling user input and database exceptions.
