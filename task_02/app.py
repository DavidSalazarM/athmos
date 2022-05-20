
import json
import os.path
from simple_term_menu import TerminalMenu


class UserModel():
    def __init__(self, name, last_name, age, email):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.email = email

    def __str__(self):
        return "name:{}, last_name:{}, age:{}, email:{}".format(
            self.name, self.last_name, self.age, self.email)


class Repository():
    def __init__(self):
        self.data = []
        self.path = "file.json"
        if not os.path.isfile(self.path):
            raise OSError("File not exist")
        try:
            self.file = open(self.path)
            self.user_list = json.load(self.file)
            self.file.close()
        except json.decoder.JSONDecodeError:
            with open(self.path, "w") as file:
                file.write(str([]))
        try:
            for data_user in self.user_list:
                if isinstance(data_user, dict):
                    user = UserModel(**data_user)
                    self.data.append(user)
                else:
                    raise Exception("invalid format")
        except AttributeError:
            pass

    def add(self, new_data):
        self.data.append(new_data)

    def list(self):
        return self.data

    def get(self, index):
        try:
            data = self.data[index]
            return data
        except IndexError:
            raise ValueError('User does not exist')

    def update(self, index, update_data):
        try:

            data = self.data
            data[index] = update_data
            return data[index]
        except IndexError:
            raise ValueError('User does not exist')

    def delete(self, index):
        try:
            data = self.data
            data.pop(index)
        except IndexError:
            raise ValueError('User does not exist')

    def rollback(self):
        self.file = open(self.path)
        self.user_list = json.load(self.file)
        for data_user in self.user_list:
            user = UserModel(**data_user)
            self.data.append(user)
        self.file.close()

    def commit(self):
        json_string = json.dumps([ob.__dict__ for ob in self.data])
        with open(self.path, "w") as file:
            file.write(json_string)


def int_value(question):
    try:
        num = int(input(question))
        return num
    except ValueError:
        raise ValueError('that is not a valid number')


def main():
    try:
        repo = Repository()

        print(
            """********************************[Select An Option ]****************************************""")
        options = [
            "Add User",
            "User List",
            "Get User",
            "Update User",
            "Delete User",
            "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected: {options[menu_entry_index]}!")

        if menu_entry_index == 0:
            name = input("User name: ")
            last_name = input("User last name: ")
            age = int_value("User age: ")
            email = input("User email: ")
            user = UserModel(name, last_name, age, email)
            repo.add(user)
            repo.commit()
            return False

        if menu_entry_index == 1:
            users = repo.list()
            for idx, user in enumerate(users):
                print("{}.-".format(idx), user)
            return False

        if menu_entry_index == 2:

            index = int_value("User Index: ")
            print(repo.get(index))
            return False

        if menu_entry_index == 3:
            user_index = int_value("which user would you like to update?: ")
            repo.get(user_index)
            name = input("Update User name: ")
            last_name = input("Update User last name: ")
            age = int_value("Update User age: ")
            email = input("Update User email: ")
            user = UserModel(name, last_name, age, email)
            print(repo.update(user_index, user))
            repo.commit()
            return False

        if menu_entry_index == 4:
            user_index = int_value("which user would you like to delete?: ")
            repo.delete(user_index)
            repo.commit()
            print("Deleted")
            return False

        if menu_entry_index == 5:
            print("Chao")
            return True
    except Exception as e:
        print(e)
        exit()


if __name__ == "__main__":
    var = False
    while var == False:
        var = main()
