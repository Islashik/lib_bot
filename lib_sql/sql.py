import mysql.connector
from user_sql import UserSQL
from genre_sql import GenreSQL
from authors_sql import AuthorsSQL
from books_sql import BooksSQL
from datetime import datetime
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "Abc12345!",
    db = "Neman",
    autocommit = True)
cursor = db.cursor()

user_manager = UserSQL(cursor=cursor)
genre_manager = GenreSQL(cursor= cursor)
author_manager = AuthorsSQL(cursor)
book_manager = BooksSQL(cursor)


for (book_id, book_name, author_id, author_name, genre_id, genre) in book_manager.get_books_full_info():
    print('book_id:', book_id)
    print('book_name:',book_name)
    print('author_id:', author_id)
    print("author_name:", author_name)
    print("genre_id:", genre_id)
    print("genre:", genre)
    print("-------------------------------------------")
# print(author_manager.get_author(3))
# print(author_manager.get_all_authors())
cursor.close()

