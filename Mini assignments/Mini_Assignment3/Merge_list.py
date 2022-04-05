from itertools import chain


def merge_list(arr1, arr2):
    # for i in range(len(arr2)):
    #     arr1.append(arr2[i])
    # return arr1
    return arr1 + arr2


list1 = list(map(str, input("Enter first string : \n").split(" ")))
list2 = list(map(str, input("Enter second string : \n").split(" ")))
# result = [*list1, *list2]
print(merge_list(list1, list2))
# list1.extend(list2)
# print(list1)
# print(result)
# print(list(chain(list1, list2)))