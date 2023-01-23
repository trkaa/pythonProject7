def main_menu() -> int:
    print('Главное меню.')
    menu_list = ['Показать все контакты',
                 'Открыть файл',
                 'Сохранить файл',
                 'Создать контакт',
                 'Изменить контакт',
                 'Удалить контакт',
                 'Выход'
                 ]
    for i in range(len(menu_list)):
        print(f'\t{i + 1}. {menu_list[i]}')
    user_input = int(input('Введи команду >: '))
    # TODO: сделать валидацию
    return user_input


def show_all(db: list):
    if db_success(db):
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end='. ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()


def db_success(db: list):
    if db:
        print('Телефонная книга открыта')
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        return False


def exit_program():
    print('Завершение программы.')
    exit()


def create_contact():
    print('Создание нового контакта.')
    new_contact = dict()

    new_contact['lastname'] = input('\tВведите фамилию >: ')
    new_contact['firstname'] = input('\tВведите имя >: ')
    new_contact['phone'] = input('\tВведите телефон >: ')
    new_contact['comment'] = input('\tВведите комментарий >: ')
    return new_contact

def change_contact(db_list):
    # user_id = 0
    # phone = ''
    # lastname = ''
    # firstname = ''
    # comment = ''
    user_id = int(input('Введите номер контакта который хотите изменить >:'))
    while user_id not in range(1, len(db_list)+1):
        print('такого контакта нет')
        user_id = int(input('Введите номер контакта который хотите изменить >:'))
    phone = db_list[user_id-1]['phone']
    lastname = db_list[user_id - 1]['lastname']
    firstname = db_list[user_id - 1]['firstname']
    comment = db_list[user_id - 1]['comment']
    db_list[user_id - 1]['lastname'] = str(input(f'изменить Имя {lastname} на новый >:'))
    db_list[user_id - 1]['firstname'] = str(input(f'изменить Фамилию {firstname} на новый >:'))
    db_list[user_id - 1]['phone'] = str(input(f'изменить телефон {phone} на новый >:'))
    db_list[user_id - 1]['comment'] = str(input(f'изменить комментарий {comment} на новый >:'))



def delet_id(db_list):
    a = int(input('Ведите номер контакта который хотите удалить >: '))
    while a not in range(1, len(db_list) + 1):
        print('такого контакта нет')
        a = int(input('Ведите номер контакта который хотите удалить >: '))
    db_list.pop(a-1)


