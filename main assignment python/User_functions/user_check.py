import pandas as pd
from os.path import join, dirname


def user_check(username, password):
    try:
        path = join(dirname(__file__), "../resources/user data.csv")
        data = pd.read_csv(path)
        user_name = data['Username'].tolist()
        passwd = data['Password'].tolist()
        if user_name.index(username) == passwd.index(password):
            return True
        else:
            return False
    except Exception as e:
        print("Error : ", e)


if __name__ == "__main__":
    user_check('user1', 'user1password')
