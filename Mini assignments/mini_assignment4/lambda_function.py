from math import sqrt


res = lambda a, b, c: ((-b + sqrt((b * b) - (4 * a * c))) / (2 * a), (-b - sqrt((b * b) - (4 * a * c))) / (2 * a)) if (pow(b, 2) - 4*a*c) >= 0 else "No roots"
inp = res(*map(int,input("enter numbers: ").split(" ")))
print(inp)