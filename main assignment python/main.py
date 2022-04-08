from pwinput import pwinput
from Admin_functions.check_admin import check_admin
from Admin_functions.add_movie_page import add_movie_page
from Admin_functions.edit_movie_info import  edit_movie_info
from Admin_functions.delete_movie import delete_movie
from User_functions.select_movie import select_movie
from User_functions.movie_details import movie_details
from User_functions.user_registration import user_registration
from User_functions.user_check import user_check
import sys


class Login:
    def __init__(self, user_name, password) -> None:
        self.user_name = user_name
        self.password = password

    def check_admin(self):
        return check_admin(self.user_name, self.password)

    def check_user(self):
        return user_check(self.user_name, self.password)


class Register:
    def __init__(self, name, username, email, phone_num, age, password) -> None:
        self.name = name
        self.username = username
        self.email = email
        self.phone_num = phone_num
        self.age = age
        self.password = password

    def register_user(self):
        return user_registration(self.name, self.username, self.email, self.phone_num, self.age, self.password)


class AdminAccount:
    def admin_panel(self):
        while True:
            print("\n", "*"*20, " Welcome Admin", "*"*20)
            print("1. Add new movie info\n2. Edit movie info\n3. Delete movies\n4. Logout")
            option = int(input("Enter : "))
            if option == 1 or option == 2 or option == 3 or option == 4:
                return option
            else:
                print("Please select valid option")

    def add_new_movie(self):
        add_movie_page()

    def edit_movie_info(self):
        edit_movie_info()

    def delete_movies(self):
        delete_movie()

    def logout(self):
        print("logout")  # call the logout function or simply call the start page function


class UserAccount:
    def select_movie(self):
        movie_num = select_movie()
        return movie_num

    def show_movie_details(self, movie_num):
        option = movie_details(movie_num)
        return option

    def book_tickets(self):
        pass

    def cancel_tickets(self):
        pass

    def user_rating(self):
        pass

    def logout(self):
        pass


class Pages:
    def start_page(self):
        while True:
            print("*" * 20, " Welcome to BookMyShow ", "*" * 20)
            print("1. Login\n2. Register new account\n3. Exit")
            num = int(input("Enter : "))
            if num == 1 or num == 2:
                return num
            elif num == 3:
                sys.exit(0)
            else:
                print("Please enter valid option")

    def login_input(self):
        while True:
            print("\n", "*" * 20, " Welcome to BookMyShow ", "*" * 20)
            username = input("User : ")
            password = pwinput("Password : ")
            if username == "admin":
                login = Login(username, password)
                if login.check_admin():
                    return 'admin'
                else:
                    print("\nInvalid login credentials")
            else:
                login = Login(username, password)
                if login.check_user():
                    return 'user'
                else:
                    print("\nInvalid login credentials")

    def user_registration(self):
        while True:
            """name, username, email, phone_num, age, password"""
            print("\n", "*" * 20, " Create new account ", "*" * 20)
            name = input("Name : ")
            username = input("Username : ")
            email = input("Email : ")
            phone_num = int(input("Phone no. : "))
            age = int(input("Age : "))
            password = pwinput("Password : ")
            register = Register(name, username, email, phone_num, age, password)
            print(register.register_user())
            if register.register_user():
                return True
            else:
                print("Registration unsuccessful")
                return False


if __name__ == "__main__":
    while True:
        start = Pages()
        option = start.start_page()
        if option == 1:
            val = start.login_input()
            while True:
                if val == 'admin':
                    admin = AdminAccount()
                    admin_option = admin.admin_panel()
                    if admin_option == 1:
                        admin.add_new_movie()
                    elif admin_option == 2:
                        admin.edit_movie_info()
                    elif admin_option == 3:
                        admin.delete_movies()
                    else:
                        break
                elif val == 'user':
                    print("User login")
                    break

        elif option == 2:
            while True:
                if start.user_registration():
                    print("Registration successful")
                    break









