def merge_dictionaries(dict1, dict2):
    return dict1.update(dict2)


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

# Input for dictionary
# total_elements_for_dict1 = int(input("Enter total number of elements in first dictionary : "))
# dict1 = dict()
# for i in range(total_elements_for_dict1):
#     key = input("Key : ")
#     value = int(input("Value : "))
#     dict1[key] = value
#
# total_elements_for_dict2 = int(input("Enter total number of elements in second dictionary : "))
# dict2 = dict()
# for i in range(total_elements_for_dict2):
#     key = input("Key : ")
#     value = int(input("Value : "))
#     dict2[key] = value

# dict3 = {**dict1, **dict2}
# print(dict3)
# dict3 = dict1 | dict2
# print(dict3)
merge_dictionaries(dict1, dict2)
print(dict1)
