def lists_int_dictionary(list1, list2):
    dictionary = dict(zip(list1, list2))
    return dictionary


list1 = list(map(str, input().split(' ')))
list2 = list(map(int, input().split(" ")))
print(lists_int_dictionary(list1, list2))