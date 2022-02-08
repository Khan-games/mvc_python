from numpy import empty
from user import User

class Model:
    def __init__(self):
        self.users = []

    def get_user_list(self):
        return self.users

    def get_user_by_id(self, id):
        return [user for user in self.users if user.get_id() == id][0]

    def add_user(self, new_user: User):
        id = new_user.get_id()
        temp_list = [user for user in self.users if user.get_id() == id]
        if temp_list:
            temp_list[0].copy_user(new_user)
        else:
            self.users.append(new_user)

    def delete_user(self, id):
        self.users = [user for user in self.users if id != user.get_id()]
    
    def update_user(self, new_user: User):
        self.add_user(new_user)
