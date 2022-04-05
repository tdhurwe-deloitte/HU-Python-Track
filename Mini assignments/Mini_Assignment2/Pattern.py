def pattern1(num):
    for x in range(num):
        print(" " * (num - x), "*" * (2 * x + 1))
    for x in range(num - 2, -1, -1):
        print(" " * (num - x), "*" * (2 * x + 1))


def pattern2(num):
    for i in range(num):
        for j in range(num - i):
            print(' ', end='')

        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i or i == num - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def pattern3(num):
    for row in range(1, num +1):
        for col in range(1, num + 1):
            if(col == num) or (row == 1) or (col == row):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


num = int(input("Enter number : "))
print("Printing pattern1")
pattern1(num)
print("\nPrinting pattern 2")
pattern2(num)
print("\nPrinting pattern 3")
pattern3(num)