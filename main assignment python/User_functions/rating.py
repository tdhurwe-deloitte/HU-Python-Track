import pandas as pd
from os.path import join, dirname


def user_rating(movie_num, user):
    path = join(dirname(__file__), '../resources/tickets data.csv')
    df = pd.read_csv(path)
    print("please enter rating for ", df.loc[movie_num, 'Movie name'])
    rating = int(input("Rating (out of 10) : "))
    r = str(rating) +"/10"
    df.loc[movie_num, 'User rating'] = r
    df.to_csv(path, index=False)