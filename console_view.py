from user import User
from model import Model
from controller import Controller

ctrl = Controller()
model = ctrl.get_model()

while True:
    print('>>> ' , end='')
    command = input().split(' ')
    if command[0] == 'list':
        print('[Users]')
        print('id\tname\tage\tprofession')
        for user in model.get_user_list():
            print(user.get_id(), '\t', user.get_name(), '\t', user.get_age(), '\t', user.get_profession(), sep='')
    elif command[0] == 'add':
        temp_user = User(name=command[1], age=int(command[2]), profession=command[3])
        ctrl.add_user(temp_user)
    elif command[0] == 'delete':
        ctrl.delete_user(int(command[1]))
    elif command[0] == 'update':
        temp_user = User(id=int(command[1]), name=command[2], age=int(command[3]), profession=command[4])
        ctrl.update_user(temp_user)
    elif command[0] == 'quit':
        break
    else:
        print('Unknown command.')

