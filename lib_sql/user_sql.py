class UserSQL():
    def __init__(self, cursor):
        self.cursor = cursor

    def show_tables(self):
        query = """
        SHOW TABLES;
        """
        self.cursor.execute(query)

    def create_table_user(self):
        query = """
        CREATE TABLE [IF NOT EXISTS] users(
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL
            );
        """
        self.cursor.execute(query)

    def add_new_user(self, name, email, password):
        query = f"""
        INSERT INTO users(name, email, password) 
        VALUES('{name}', '{email}', '{password}');
        """
        self.cursor.execute(query)
        print('Новый пользователь успешно добавлен!')

    def get_user(self, id):
        query = f"""
        SELECT * FROM users WHERE id={id}
        """
        self.cursor.execute(query)
        return self.cursor.fetchone()
    def get_all_users(self):
        query = f"""
                SELECT * FROM users;
                """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def delete_user(self, id):
        query= f"""
        DELETE FROM users WHERE id={id};
        """
        self.cursor.execute(query)
        print(f'Пользователь успешно был удален по id:{id}')

    def update_user_name(self,id, value):
        q = f"""
        UPDATE users SET name='{value}' WHERE id={id}
        """
        self.cursor.execute(q)
        print('Поле name успешно обновлено!')
    
    def update_user_email(self,id, value):
        q = f"""
        UPDATE users SET name='{value}' WHERE id={id}
        """
        self.cursor.execute(q)
        print('Поле email успешно обновлено!')
    
    def update_user_password(self,id, value):
        q = f"""
        UPDATE users SET name='{value}' WHERE id={id}
        """
        self.cursor.execute(q)
        print('Поле password успешно обновлено!')
    