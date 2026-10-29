# Movie Database System

A menu-driven movie database management application developed using Python and MySQL. It allows users to manage movie details, director information, and movie ratings through a command-line interface.

## Features

- Add director information.
- Add movies with their release year, genre, and director.
- Add ratings for existing movies.
- View the list of movies stored in the database.
- View movie reviews and ratings.
- Validate user inputs and handle database errors.
- Maintain relationships between directors, movies, and reviews using foreign keys.

## Technologies Used

- **Python** — Application logic and user interaction.
- **MySQL** — Relational database management.
- **MySQL Connector/Python** — Communication between Python and MySQL.
- **SQL** — Database and table creation, insertion, and retrieval.

## Project Structure

```text
Movie-Database-System/
├── movie_database.py
├── schema.sql
└── README.md
```

## Database Design

The application uses a MySQL database named `moviedb`, containing three tables:

### 1. Directors

Stores director information.

- `director_id` — Primary key; automatically generated.
- `director_name` — Director's name; must be unique and cannot be NULL.

### 2. Movies

Stores movie details.

- `title` — Primary key.
- `release_year` — Movie release year.
- `genre` — Movie genre.
- `director_name` — Foreign key referencing the Directors table.

### 3. Reviews

Stores movie ratings.

- `review_id` — Primary key; automatically generated.
- `movie_title` — Foreign key referencing the Movies table.
- `rating` — Integer rating restricted to the range 1–10.

## Prerequisites

Before running the application, install:

- Python 3
- MySQL Server
- MySQL Connector/Python

Install the Python connector using:

```bash
python -m pip install mysql-connector-python
```

## Setup and Execution

### Step 1: Clone the repository

```bash
git clone https://github.com/Ekansh-Gupta-20/Movie-Database-System.git
cd Movie-Database-System
```

Alternatively, download the repository as a ZIP file and extract it.

### Step 2: Create the database and tables

Open MySQL and execute the SQL script in `schema.sql`.

For example, from a terminal in the project directory:

```bash
mysql -u root -p < schema.sql
```

Enter your MySQL password when prompted.

**Note:** This command creates the database and tables for a fresh setup. It does not update tables that already exist.

### Step 3: Configure the database connection

Open `movie_database.py` and configure the connection settings in the `create_connection()` function to match your local MySQL setup.

Keep your actual database password private. Do not commit passwords or other credentials to GitHub.

### Step 4: Run the application

```bash
python movie_database.py
```

The application displays a menu with the following options:

1. Add Director
2. Add Movie
3. Add Review
4. View Movies
5. View Reviews
6. Exit

Choose an option and follow the prompts displayed in the terminal.

## Validation

The application validates user input and handles database errors. The database schema also enforces foreign-key relationships and restricts ratings to values between 1 and 10.

## Author

Ekansh Gupta
