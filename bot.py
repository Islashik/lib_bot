from audioop import add
from bdb import GENERATOR_AND_COROUTINE_FLAGS
from pickle import MARK
import telebot
from config import TOKEN
from lib_sql.user_sql import UserSQL
from lib_sql.authors_sql import AuthorsSQL
from lib_sql.books_sql import BooksSQL
from lib_sql.genre_sql import GenreSQL
from telebot import types
import mysql.connector
bot = telebot.TeleBot(token=TOKEN)


db = mysql.connector.connect(
   host="localhost",
    user="root",
    password="Abc12345!",
    db="chat",
    autocommit=True)
cursor = db.cursor()


@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    text = """
    Добро пожаловать в бота имени Ч.Айтматова
    """
    markup = types.InlineKeyboardMarkup()
    mycart = types.InlineKeyboardButton('Моя карточка', callback_data='my_cart')
    genres = types.InlineKeyboardButton('Жанры', callback_data='genres')
    search = types.InlineKeyboardButton('Поиск', callback_data='search')
    my_books = types.InlineKeyboardButton('Мои книги', callback_data='my_books')
    markup.row_width = 1
    markup.add(mycart,genres,search, my_books)
    bot.send_message(message.chat.id, text=text, reply_markup=markup)
    

@bot.callback_query_handler(func= lambda call: call.data=='genres')
def send_all_genres(call):
    message = call.message
    genre_manger = GenreSQL(cursor)
    genres = genre_manger.get_all_genres()
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 2 
    for (id,name) in genres:
        button = types.InlineKeyboardButton(name, callback_data=f"genre_{id}")
        markup.add(button)
    bot.edit_message_text(
        chat_id=message.chat.id, 
        text="Выберите жанр",
        message_id=message.id,
        reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'my_books')
def send_user_books(call):
    message = call.message
    books_manager = BooksSQL(cursor)
    books = books_manager.get_books_full_info()
    markup = types.InlineKeyboardMarkup()
    for book in books:
        name = book[1]
        book_id = book[0]
        button = types.InlineKeyboardButton(
            name,
        callback_data=f"book_{book_id}")
        markup.add(button).row_width = 2
    bot.edit_message_text(
        chat_id = message.chat.id,
        text = 'Выберите книгу',
        message_id = message.id
    )
bot.infinity_polling()

