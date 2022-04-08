from itertools import combinations


class StringClass:
    def __init__(self):
        # self.string1 = string1
        # self.string2 = string2
        self.string1 = "12314532"
        self.string2 = "45211834"

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
            print(key, end=", ")

    def print_list(self):
        print("\nCommon elements ", end=" ")
        print(self.arr)


# str1 = "12314532"
# str2 = "45211834"
obj1 = StringClass()
obj1.length_of_string()
obj1.string_to_list()
obj2 = PairsPossible()
obj2.possible_pairs()
obj3 = SearchCommonElements()
obj3.common_element()
obj3.print_list()
