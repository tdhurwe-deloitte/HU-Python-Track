def merge_nested_list(list1, list2):
    return list1[2][1][2].extend(list2)


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list2 = ["h", "i", "j"]
merge_nested_list(list1, list2)
print(list1)