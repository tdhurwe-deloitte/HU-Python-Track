class StringClass:
    def __init__(self, string):
        self.string = string

    def return_string(self):
        return self.string

    def length_of_string(self):
        return len(self.string)

    def string_to_list(self, string2):
        return list(self.string)


class PairsPossible(StringClass):
    def __init__(self, string):
        super().__init__(string)
        self.possible_pairs = []

    def all_possible_pairs(self):
        # possible_pairs = []
        string1 = StringClass.string_to_list(self, self.string)
        length = StringClass.length_of_string(self)
        for i in range(length):
            for j in range(length):
                self.possible_pairs.append((self.string[i], self.string[j]))
                # print("(", self.string[i], ",", self.string[j], ")", end=" ")

    def string_to_list(self, string2):
        return list(string2)

    def print_pais(self):
        for i in range(len(self.possible_pairs)):
            print(self.possible_pairs[i], end=" ")


class SearchCommonElements:
    def common_elements(self):
        obj1 = StringClass("1234")
        ls1 = obj1.string_to_list("1234")
        obj2 = StringClass("4321")
        ls2 = obj2.string_to_list("4321")
        dictionary = {}
        new_list = []


obj1 = StringClass("12345")
