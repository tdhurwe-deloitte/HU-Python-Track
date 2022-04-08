from csv import writer
from os.path import join, dirname
import pandas as pd


def user_registration(name, username, email, phone_no, age, password):
    path = join(dirname(__file__), "../resources/user data.csv")
    data = pd.read_csv(path)
    user_name = data['Username'].tolist()
    user_email = data['Email'].tolist()
    user_phone_no = data['Phone no.'].tolist()
    if username not in user_name:
        if email not in user_email:
            if phone_no not in user_phone_no:
                ls = [name, username, email, phone_no, age, password]
                with open(path, 'a') as file:
                    writer_obj = writer(file)
                    writer_obj.writerow(ls)
                    file.close()
                print("User added successfully")
                return True
    return False


if __name__ == "__main__":
    user_registration("random user1", "user1", "random.user1@gmail.com", '9080706050', '32', 'user1password')