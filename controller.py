import sqlite3
from user import User
from model import Model

class Controller:
    def __init__(self):
        self.con = sqlite3.connect('sqlite.db')
        self.model = Model()
        self.load_model()

    def __del__(self):
        self.con.commit()
        self.con.close()

    def get_model(self):
        return self.model

    def load_model(self):
        cur = self.con.cursor()
        for row in cur.execute('select * from users;'):
            temp_user = User(row[0], row[1], row[2], row[3])
            self.model.add_user(temp_user)

    def add_user(self, new_user: User):
        cur = self.con.cursor()
        cur.execute(f'insert into users(name, age, profession) values(\'{new_user.get_name()}\', {new_user.get_age()}, \'{new_user.get_profession()}\');')
        new_user.set_id(cur.lastrowid)
        self.model.add_user(new_user)
        self.con.commit()

    def delete_user(self, id):
        cur = self.con.cursor()
        cur.execute(f'delete from users where id={id};')
        self.model.delete_user(id)
        self.con.commit()
    
    def update_user(self, new_user: User):
        cur = self.con.cursor()
        cur.execute(f'update users set name=\'{new_user.get_name()}\', age={new_user.get_age()}, profession=\'{new_user.get_profession()}\' where id={new_user.get_id()};')
        self.model.update_user(new_user)
        self.con.commit()
