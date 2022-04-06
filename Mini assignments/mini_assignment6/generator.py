def fibonacci(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        a, b = b, a + b


num = int(input("Enter number : "))
for x in fibonacci(num):
    print(x, end=", ")
