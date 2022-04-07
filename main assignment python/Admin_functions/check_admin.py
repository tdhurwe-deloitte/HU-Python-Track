import json
from os.path import join, dirname


def check_admin(uname, passwd):
    path = join(dirname(__file__), "../resources/admin.json")

    with open(path, "r") as file:
        data = json.load(file)
        user_name = data["user_name"]
        password = data["password"]

    if uname == user_name and passwd == password:
        return True
    else:
        return False


if __name__ == "__main__":
    check_admin("admin", "randompassword")
