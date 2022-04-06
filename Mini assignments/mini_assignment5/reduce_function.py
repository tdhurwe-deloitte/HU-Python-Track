from functools import reduce
import operator

list1 = list(map(int, input("Enter numbers : \n").split(" ")))
res = reduce(operator.mul, list1)
print(res)
