db_list = []


def read_db(path: str) -> list:
    global db_list
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        for line in my_list:
            id_dict = dict()
            line = line.strip().split(' ')
            id_dict['lastname'] = line[0]
            id_dict['firstname'] = line[1]
            id_dict['phone'] = line[2]
            id_dict['comment'] = line[3]
            db_list.append(id_dict)

def save_file(n):
    n = db_list
    ns = []
    a = ''
    for i in range(len(n)):
        a = ''
        for v in db_list[i].values():
            v = str(f'{v} ')
            a = a+v
        ns.append(a)
    with open('database.txt', 'w', encoding='UTF-8') as file1:
        file1.writelines('\n'.join(ns))










    # with open('database.txt', 'w', encoding='UTF-8') as file:
    #     for i in range(len(db_list)):
    #         file.write(db_list[i].values)



