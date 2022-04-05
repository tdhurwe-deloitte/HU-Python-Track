from itertools import combinations


class StringClass:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2
        # self.string1 = "12314532"
        # self.string2 = "45211834"

    def length_of_string(self):
        print(len(self.string1))
        return len(self.string1)

    def string_to_list(self):
        print(list(self.string2))
        return list(self.string2)


class PairsPossible(StringClass):
    def possible_pairs(self):
        res = list(combinations(self.string1, 2))
        print(res)


class SearchCommonElements(StringClass):
    arr = []

    def common_element(self):
        dictionary = {}
        for char in self.string1:
            if char in dictionary:
                continue
            else:
                dictionary[char] = 1
        for char in self.string2:
            if char in dictionary:
                self.arr.append(char)

        for key, val in dictionary.items():
            print(key + " ")

    def print_list(self):
        print("third")
        print(self.arr)


str1 = "12314532"
str2 = "45211834"
obj = StringClass(str1, str2)
obj.length_of_string()
obj.string_to_list()
obj1 = PairsPossible()
obj1.possible_pairs()
obj2 = SearchCommonElements()
obj2.common_element()
obj2.print_list()