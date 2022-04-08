import pandas as pd
from os.path import join, dirname


def delete_movie():
    print("\n", "*" * 20, " Welcome Admin", "*" * 20)
    path = join(dirname(__file__), '../resources/movie data.csv')
    df = pd.read_csv(path)
    for i in range(df.shape[0]):
        print(i+1, ". ", df.iloc[i][0])

    choice = int(input("Enter : "))
    choice -= 1
    try:
        df.drop(choice, inplace=True)
        print("Data deleted successfully\n")
    except Exception as e:
        print("Task failed", e)


if __name__ == "__main__":
    delete_movie()
