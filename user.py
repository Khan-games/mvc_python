class User:
    def __init__(self, id=-1, name='New_user', age=0, profession='Unemployed'):
        self.id = id
        self.name = name
        self.age = age
        self.profession = profession

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_profession(self):
        return self.profession

    def set_id(self, new_id):
        self.id = new_id
    
    def set_name(self, new_name):
        self.name = new_name

    def set_age(self, new_age):
        self.age = new_age

    def set_profession(self, new_profession):
        self.profession = new_profession

    def copy_user(self, user):
        self.set_id(user.get_id())
        self.set_name(user.get_name())
        self.set_age(user.get_age())
        self.set_profession(user.get_profession())

