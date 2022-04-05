def dictionary_to_list(dictionary):
    result = [[key]+value for key, value in dictionary.items()]
    return result


dictionary = dict()
num = int(input("Enter total number of key value pairs : "))
for i in range(num):
    key = input("Key : ")
    value = list(map(int, input("Value : ").split(" ")))
    dictionary[key] = value

print(dictionary_to_list(dictionary))