def decorator_function(execute_twice):
    def print_twice(num1, num2):
        execute_twice(num1, num2)
        execute_twice(num1, num2)
    return print_twice


@decorator_function
def multiply(num1, num2):
    print(num1*num2)


num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
multiply(num1, num2)