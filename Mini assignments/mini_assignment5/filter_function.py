lst1 = [-1000, 500, -600, 700, 5000, -90000, -17500]
result = list(map(lambda x: x*-1, list(filter(lambda x: x < 0, lst1))))
print(result)
