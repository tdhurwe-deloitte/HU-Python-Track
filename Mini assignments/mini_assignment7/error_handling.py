class Formula_error(Exception):
    pass


def calculator():
    string = input("Enter expression : \n")
    # string = "1 + 2"
    ls = string.split(" ")
    try:
        if len(ls) < 3:
            raise Formula_error
        if ls[1] != "+":
            if ls[1] != "-":
                raise Formula_error

        val1 = float(ls[0])
        val2 = float(ls[2])
        if ls[1] == "+":
            print(f"{val1} + {val2} = {val1 + val2}")
        else:
            print(f"{val1} - {val2} = {val1 - val2}")
    except Formula_error:
        print("Invalid input format")

    except ValueError as e:
        print(e)

    except:
        print("Invalid inputs")

    finally:
        choice = input("Enter y to continue and n to exit : ")
        if choice == "y":
            calculator()
        else:
            print("Thank you")


calculator()
