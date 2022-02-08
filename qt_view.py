from turtle import update
from PyQt5.QtWidgets import *
from PyQt5 import QtCore 
from matplotlib.pyplot import connect 
from user import User
from model import Model
from controller import Controller

app = QApplication([])
window = QDialog()
window.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

# H layouts
id_layout = QHBoxLayout()
name_layout = QHBoxLayout()
age_layout = QHBoxLayout()
prof_layout = QHBoxLayout()
main_layout = QHBoxLayout(window)
# V layouts
fields_layout = QVBoxLayout()
list_layout = QVBoxLayout()

# labels
id_label = QLabel('ID:')
name_label = QLabel('Name')
age_label = QLabel('Age')
prof_label = QLabel('Profession')

# buttons
add_button = QPushButton('Add')
delete_button = QPushButton('Delete')
save_button = QPushButton('Save')

# line edits
name_edit = QLineEdit()
age_edit = QLineEdit()
prof_edit = QLineEdit()

# list 
users_list = QListWidget()

# insert widgets to layouts
# fields layout
id_layout.addWidget(id_label)
id_layout.addStretch()
name_layout.addWidget(name_label)
name_layout.addWidget(name_edit)
age_layout.addWidget(age_label)
age_layout.addWidget(age_edit)
prof_layout.addWidget(prof_label)
prof_layout.addWidget(prof_edit)
fields_layout.addLayout(id_layout)
fields_layout.addLayout(name_layout)
fields_layout.addLayout(age_layout)
fields_layout.addLayout(prof_layout)
fields_layout.addWidget(save_button)
fields_layout.addStretch()
# list layout
list_layout.addWidget(users_list)
list_layout.addWidget(add_button)
list_layout.addWidget(delete_button)
# main layout
main_layout.addLayout(list_layout)
main_layout.addLayout(fields_layout)

# load list
ctrl = Controller()
model = ctrl.get_model()
for user in model.get_user_list():
    users_list.addItem(user.get_name())

# slots
def update_list():
    users_list.clear()
    for user in model.get_user_list():
        users_list.addItem(user.get_name())

def update_fields():
    selected_user = model.get_user_list()[users_list.selectedIndexes()[0].row()]
    id_label.setText(f'ID: {selected_user.get_id()}')
    name_edit.setText(selected_user.get_name())
    age_edit.setText(str(selected_user.get_age()))
    prof_edit.setText(selected_user.get_profession())

def save_fields():
    if users_list.selectedIndexes():
        selected_user = model.get_user_list()[users_list.selectedIndexes()[0].row()]
        temp_user = User(id=selected_user.get_id())
        temp_user.set_name(name_edit.text())
        temp_user.set_age(int(age_edit.text()))
        temp_user.set_profession(prof_edit.text())
        ctrl.update_user(temp_user)
        update_list()

def add_user():
    new_user = User()
    ctrl.add_user(new_user)
    update_list()

def delete_user():
    if users_list.selectedIndexes():
        selected_user = model.get_user_list()[users_list.selectedIndexes()[0].row()]
        ctrl.delete_user(selected_user.get_id())
        update_list()

# connect slots
users_list.itemClicked.connect(lambda item: update_fields())
save_button.clicked.connect(lambda: save_fields())
add_button.clicked.connect(lambda: add_user())
delete_button.clicked.connect(lambda: delete_user())

window.exec_()
