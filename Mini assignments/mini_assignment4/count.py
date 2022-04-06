lst1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
count_A = list(map(lambda x: x.count('A'), lst1))
count_a = list(map(lambda x: x.count('a'), lst1))
print("Count of A : ", count_A)
print("Count of a : ", count_a)

