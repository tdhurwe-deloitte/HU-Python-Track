import pandas as pd
from os.path import join, dirname


def edit_movie_info():
    print("\n", "*" * 20, " Welcome Admin", "*" * 20)
    ls = [
        "Title : ",
        "Genre : ",
        "Length(in min) : ",
        "Cast : ",
        "Director : ",
        "Admin rating : ",
        "Language : ",
        "Timings : ",
        "Number of shows in a day : ",
        "First show : ",
        "Interval time : ",
        "Gap between shows : ",
        "Capacity : "
    ]
    path = join(dirname(__file__), '../resources/movie data.csv')
    df = pd.read_csv(path)
    ls2 = []
    for i in df.columns:
        ls2.append(i)

    print(ls2[1])
    for i in range(df.shape[0]):
        print(i+1, ". ", df.iloc[i][0])
    choice = int(input("Enter : "))
    for j in range(df.shape[1]):
        print(j+1, ". ", ls[j], df.iloc[choice-1][j])
    option = int(input("Enter : "))
    value = input("Enter value : ")
    try:
        df.loc[choice-1, ls2[option - 1]] = value
        df.to_csv(path, index=False)
        print("Data updated successfully\n")
    except:
        print("Task failed\n")


if __name__ == "__main__":
    edit_movie_info()
