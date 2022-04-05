from math import factorial


def pascal_triangle(num):
    for line in range(0, num):
        for i in range(0, line + 1):
            print(binomial_coeff(line, i), " ", end="")
        print("0  " * (num-line))
        print()


def binomial_coeff(num, k):
    res = 1
    if k > num - k:
        k = num - k
    for i in range(0, k):
        res = res * (num - i)
        res = res // (i + 1)

    return res


num = int(input("Enter the number : "))
pascal_triangle(num)
