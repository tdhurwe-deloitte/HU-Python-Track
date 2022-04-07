from csv import writer
from os.path import join, dirname


def add_movie_page():
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
    # add function to calculate timings
    ls2 = []
    for i in range(len(ls)):
        print(ls[i], end="")
        value = input()
        ls2.append(value)

    dictionary = dict(zip(ls, ls2))
    path = join(dirname(__file__), "../resources/movie data.csv")
    try:
        with open(path, 'a') as file:
            writer_obj = writer(file)
            writer_obj.writerow(ls2)
            file.close()
        print("Movie added successfully\n")
    except:
        print("Task failed\n")


if __name__ == "__main__":
    add_movie_page()
