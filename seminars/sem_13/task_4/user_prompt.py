import json
from pathlib import Path

_PATH = Path.cwd() / 'users.json'


def input_data():
    name = input('Enter name:\n')
    uid = input('Enter id:\n')
    access = input('Enter access level:\n')
    return access, uid, name


def get_id_list(path: Path):
    id_list = []
    with open(path, 'r', encoding='utf-8') as file:
        users = json.load(file)
        for entry in users.values():
            for uid in entry.keys():
                id_list.append(uid)
    return id_list


def save_user_data(path: Path = _PATH):
    id_list = get_id_list(path)
    while True:
        print("1. Enter user data.\n"
              "2. Quit.")
        choice = input()
        if choice == '2':
            quit()
        else:
            user = input_data()
            if user[1] in id_list:
                print('This user id already exists')
            else:
                id_list.append(user[1])
                with open(path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    try:
                        data[user[0]][user[1]] = user[2]
                    except KeyError:
                        entry = {user[1]: user[2]}
                        data[user[0]] = entry
                with open(path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, sort_keys=True)


if __name__ == '__main__':
    save_user_data()
