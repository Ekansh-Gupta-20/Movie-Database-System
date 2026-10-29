import mysql.connector

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',
            database='moviedb'
        )

        if connection.is_connected():
            print("Connection established successfully!")

        return connection

    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None

def add_director(cursor, connection):
    try:
        director_name = input("Enter director's name: ").strip()

        if not director_name:
            print("Director name cannot be empty.")
            return

        cursor.execute(
            "SELECT director_id FROM Directors WHERE director_name = %s",
            (director_name,)
        )

        director = cursor.fetchone()

        if director:
            print(f"Director '{director_name}' already exists.")
            return

        cursor.execute(
            "INSERT INTO Directors (director_name) VALUES (%s)",
            (director_name,)
        )

        connection.commit()

        print(f"Director '{director_name}' added successfully.")

    except mysql.connector.Error as err:
        connection.rollback()
        print(f"Database error: {err}")

def add_movie(cursor, connection):
    try:
        title = input("Enter movie title: ").strip()
        release_year = input("Enter release year: ").strip()
        genre = input("Enter genre: ").strip()
        director_name = input("Enter director's name: ").strip()

        if not title:
            print("Movie title cannot be empty.")
            return

        if not director_name:
            print("Director name cannot be empty.")
            return

        try:
            release_year = int(release_year)
        except ValueError:
            print("Invalid year. Please enter a valid integer.")
            return

        if not 1888 <= release_year <= 2100:
            print("Release year must be between 1888 and 2100.")
            return

        cursor.execute(
            "SELECT title FROM Movies WHERE title = %s",
            (title,)
        )

        if cursor.fetchone():
            print(f"Movie '{title}' already exists.")
            return

        cursor.execute(
            "SELECT director_name FROM Directors "
            "WHERE director_name = %s",
            (director_name,)
        )

        director = cursor.fetchone()

        if not director:
            choice = input(
                f"Director '{director_name}' does not exist. "
                "Would you like to add this director? (y/n): "
            ).strip().lower()

            if choice != 'y':
                print("Movie was not added.")
                return

            cursor.execute(
                "INSERT INTO Directors (director_name) VALUES (%s)",
                (director_name,)
            )

        cursor.execute(
            """
            INSERT INTO Movies
                (title, release_year, genre, director_name)
            VALUES (%s, %s, %s, %s)
            """,
            (title, release_year, genre, director_name)
        )

        connection.commit()

        print(f"Movie '{title}' added successfully.")

    except mysql.connector.Error as err:
        connection.rollback()
        print(f"Database error: {err}")

def add_review(cursor, connection):
    try:
        movie_title = input(
            "Enter movie title for review: "
        ).strip()

        if not movie_title:
            print("Movie title cannot be empty.")
            return

        rating_input = input(
            "Enter rating (1 to 10): "
        ).strip()

        try:
            rating = int(rating_input)
        except ValueError:
            print("Invalid rating. Please enter an integer.")
            return

        if not 1 <= rating <= 10:
            print("Rating must be between 1 and 10.")
            return

        cursor.execute(
            "SELECT title FROM Movies WHERE title = %s",
            (movie_title,)
        )

        movie = cursor.fetchone()

        if not movie:
            print(
                f"Movie '{movie_title}' does not exist "
                "in the database."
            )
            return

        cursor.execute(
            """
            INSERT INTO Reviews (movie_title, rating)
            VALUES (%s, %s)
            """,
            (movie_title, rating)
        )

        connection.commit()

        print(f"Review for '{movie_title}' added successfully.")

    except mysql.connector.Error as err:
        connection.rollback()
        print(f"Database error: {err}")

def view_movies(cursor):
    try:
        cursor.execute(
            """
            SELECT title, release_year, genre, director_name
            FROM Movies
            ORDER BY title
            """
        )

        movies = cursor.fetchall()

        if not movies:
            print("No movies found.")
            return

        print("\n========== MOVIES ==========")

        for movie in movies:
            print(f"Title: {movie[0]}")
            print(f"Release Year: {movie[1]}")
            print(f"Genre: {movie[2]}")
            print(f"Director: {movie[3]}")
            print("-" * 30)

    except mysql.connector.Error as err:
        print(f"Database error: {err}")

def view_reviews(cursor):
    try:
        cursor.execute(
            """
            SELECT movie_title, rating
            FROM Reviews
            ORDER BY movie_title
            """
        )

        reviews = cursor.fetchall()

        if not reviews:
            print("No reviews found.")
            return

        print("\n========== REVIEWS ==========")

        for review in reviews:
            print(f"Movie: {review[0]}")
            print(f"Rating: {review[1]}/10")
            print("-" * 30)

    except mysql.connector.Error as err:
        print(f"Database error: {err}")

def main():
    connection = create_connection()

    if connection is None:
        return

    cursor = None

    try:
        cursor = connection.cursor()

        while True:
            print("\n========== MOVIE DATABASE SYSTEM ==========")
            print("1. Add Director")
            print("2. Add Movie")
            print("3. Add Review")
            print("4. View Movies")
            print("5. View Reviews")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                add_director(cursor, connection)

            elif choice == '2':
                add_movie(cursor, connection)

            elif choice == '3':
                add_review(cursor, connection)

            elif choice == '4':
                view_movies(cursor)

            elif choice == '5':
                view_reviews(cursor)

            elif choice == '6':
                print("Exiting the program...")
                break

            else:
                print("Invalid choice. Please try again.")

    except mysql.connector.Error as err:
        print(f"Database error: {err}")

    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")

    finally:
        if cursor is not None:
            cursor.close()

        if connection.is_connected():
            connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    main()
