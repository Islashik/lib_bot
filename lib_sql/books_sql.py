class BooksSQL():
    def __init__(self,cursor):
        self.cursor =cursor

    def add_new_book(self,name, author_id, genre_id):
        query = f"""
        INSERT INTO books(name, author_id, genre_id) VALUES('{name}','{author_id}','{genre_id}')
        """
        self.cursor.execute(query)
        print('Книга успешно создана!')

    def get_books_full_info(self):
        query = f"""
        SELECT books.id, books.name, 
        authors.id as authors_id,
        concat(authors.first_name, ' ', authors.last_name) as author,
        genre.id as genre_id,
        genre.name as genre_name FROM books
        LEFT JOIN authors
        ON books.author_id=authors.id
        LEFT JOIN genre
        ON books.genre_id = genre.id;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_books(self):
        query = f"""
        SELECT * FROM books;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
