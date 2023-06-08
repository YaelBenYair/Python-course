
# Implement a class SortedList in python that represents a sorted python list.
# You can assume that the list contains only numbers (no need to check this)
# Your class should implement the following methods:
#
# init - create a new SortedList instance - either empty or from a given python list
# len
# get_index(num) - O(logn) - use binary search to return the index of the number in the SortedList.
# Bonus: Make sure to return the index of the first occurrence of the number
# insert(num) - add num to an existing list. Complexity: O(n)


class SortedList:

    def __init__(self, given_list: list | None = None):

        if given_list:
            self.given_list = sorted(given_list)
        else:
            self.given_list = []

        self.len = len(self.given_list)

    def __len__(self):
        return self.len

    def __str__(self):
        return f'{self.given_list}'

    def get_index(self, value):
        long = self.len
        index = long // 2
        v = self.given_list[index]
        while value != v:
            # if long - index == 1 or long - index == -1:
            #     return -1
            if value > v:
                if index == (index + long) // 2:
                    return -1
                index = (index + long) // 2
                v = self.given_list[index]
            elif value < v:
                long = index
                if index == index // 2:
                    return -1
                index = index // 2
                v = self.given_list[index]

        return index

    def insert(self, value):
        long = self.len
        index = long // 2
        v = self.given_list[index]
        flag = False
        while value != v and not flag:
            # if long - index == 1 or long - index == -1:
            #     if long == self.len:
            #         index += 1
            #
            #     flag = True
            #     continue
            if value > v:
                if index == (index + long) // 2:
                    index += 1
                    flag = True
                    continue
                index = (index + long) // 2
                v = self.given_list[index]
            elif value < v:
                long = index
                if index == index // 2:
                    flag = True
                index = index // 2
                v = self.given_list[index]
        self.len += 1
        self.given_list.insert(index, value)


if __name__ == '__main__':

    s_list = SortedList([4, 7, 90, 3, 75, 8, 30])
    print(s_list)
    print(s_list.len)
    print(s_list.get_index(90))
    s_list.insert(7)
    print(s_list)
    print(s_list.len)
    s_list.insert(9)
    print(s_list)
    s_list.insert(100)
    print(s_list)
    s_list.insert(2)
    print(s_list)
    s_list.insert(4)
    print(s_list)
    print(s_list.get_index(3))


