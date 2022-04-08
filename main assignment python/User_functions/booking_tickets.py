import pandas as pd
from os.path import join, dirname
from csv import writer


def booking_tickets(movie_num, user):
    path = join(dirname(__file__), '../resources/movie data.csv')
    path2 = join(dirname(__file__), '../resources/tickets data.csv')
    df = pd.read_csv(path)
    print("Timings: \n1. 08:00 - 09:30\n2. 11:00 - 12:30")
    timings = int(input("Select Timings : "))
    if timings == 1:
        slot = "08:00 - 09:30"
    else:
        slot = "11:00 - 12:30"
    seats = int(df.iloc[movie_num]['Capacity'])
    print("Remaining seats : ", seats)
    movie_name = df.iloc[movie_num]['Title']
    while True:
        num_of_seats = int(input("Enter number of seats : "))
        if num_of_seats <= seats:
            ls = [user, movie_num + 1, movie_name, num_of_seats, slot]
            with open(path2, 'a') as file:
                writer_obj = writer(file)
                writer_obj.writerow(ls)
                file.close()
            remaining_seat = seats - num_of_seats
            df.loc[movie_num, 'Capacity'] = remaining_seat
            df.to_csv(path, index=False)
            print("Tickets booked successfully ")
            break
        else:
            print("Please Enter valid number of seats")


if __name__ == "__main__":
    booking_tickets(0, 'random')
