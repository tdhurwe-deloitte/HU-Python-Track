def merge_dictionaries(dict1, dict2):
    return dict1.update(dict2)


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}
# dict3 = {**dict1, **dict2}
# print(dict3)
# dict3 = dict1 | dict2
# print(dict3)
merge_dictionaries(dict1, dict2)
print(dict1)
