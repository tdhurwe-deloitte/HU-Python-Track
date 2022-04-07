from pwinput import pwinput
from check_admin import check_admin
from add_movie_page import add_movie_page
import sys


class Login:
    def __init__(self, user_name, password) -> None:
        self.user_name = user_name
        self.password = password

    def check_admin(self):
        return check_admin(self.user_name, self.password)

    def check_user(self):
        pass


class Register:
    def __init__(self, name, email, phone_num, age, password) -> None:
        self.name = name
        self.email = email
        self.phone_num = phone_num
        self.age = age
        self.password = password

    def register_user(self):
        pass  # function to register details for the registered user in csv file


class AdminAccount:
    def admin_panel(self):
        print("\n", "*"*20, " Welcome Admin", "*"*20)
        print("1. Add new movie info\n2. Edit movie info\n3. Delete movies\n4. Logout")
        option = int(input("Enter : "))
        if option == 1 or option == 2 or option == 3 or option == 4:
            return option
        else:
            print("Please select valid option")
            return self.admin_panel()

    def add_new_movie(self):
        return add_movie_page()

    def edit_movie_info(self):
        print("edit new movies")  # call the function to edit movie info

    def delete_movies(self):
        print("Delete new movies")  # call the function to delete movies

    def logout(self):
        print("logout")  # call the logout function or simply call the start page function


class UserAccount(Login):
    def select_movie(self):
        pass  # function to select movie

    def show_movie_details(self):
        pass  # call the function for movie details and options

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
                    return True
                else:
                    print("\nInvalid login credentials")
            else:
                login = Login(username, password)
                if login.check_user():
                    return True
                else:
                    print("\nInvalid login credentials")


if __name__ == "__main__":
    start = Pages()
    option = start.start_page()
    if option == 1:
        val = start.login_input()
        if val:
            admin = AdminAccount()
            admin_option = admin.admin_panel()
            # dictionary = {1: admin.add_new_movie(), 2: admin.edit_movie_info(), 3: admin.delete_movies()}
            if admin_option == 1:
                admin.add_new_movie()
            elif admin_option == 2:
                admin.edit_movie_info()
            elif admin_option == 3:
                admin.delete_movies()
            else:
                print("Error")
        else:
            print("Some error occurred")

    elif option == 2:
        print("register user")






