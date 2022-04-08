import pandas as pd
from os.path import join, dirname


def select_movie():
    path = join(dirname(__file__), "../resources/movie data.csv")
    df = pd.read_csv(path)
    while True:
        for i in range(df.shape[0]):
            print(i+1, ". ", df.iloc[i][0])
        print(df.shape[0]+1, ". Logout")
        choice = int(input("Enter movie : "))
        if 0 < choice <= df.shape[0] + 1:
            return choice - 1
        else:
            print("Please Enter valid option")


if __name__ == "__main__":
    select_movie()

