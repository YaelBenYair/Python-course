import string



# ---------------------------------------------------------------------
# D4, 1

# def letter_to_index(char) -> int:
#     if type(char) is not str or char not in string.ascii_letters:
#         raise NotStringError()
#     if char in string.ascii_lowercase:
#         return string.ascii_lowercase.find(char)+1
#     return string.ascii_uppercase.find(char)+1
#
# ab_list = ['a', 'g', 'T', 'D', 'j', 'J']
# # ab_list = ['a', 5, 'T', 'D', 'j', 'J']
#
# inx_list = list(map(letter_to_index, ab_list))
# print(inx_list)
#
# l = list(map((" " + string.ascii_lowercase).find, map(str.lower, ab_list)))
# print(l)
#
#

# ---------------------------------------------------------------------
# D4, 2

# c = 'heLLo'
# li = filter(lambda letter: letter.lower() not in ('a', 'e', 'i', 'o', 'u'), c)
# print("".join(li))


# ----------------------------------------------------------------------------
# D4, 4

# def sort_by_ken(name_list:list):
#     return sorted(name_list, key=lambda l: len(l))
#
#
# print(sort_by_ken(["kdhfyrgd", "hyfg", "surh", "jgyfhegdtacchfn"]))


# ----------------------------------------------------------------------------
# D4, 5

# def chang_to_num(word):#1h
#     ho = 60
#     sum_mini = 0
#     for i in word:
#         if i.isdigit() and sum_mini == 0:
#             sum_mini += int(i)
#         elif i == 'h':
#             sum_mini *= ho
#         elif i.isdigit():
#             sum_mini *= 10
#             sum_mini += int(i)
#     return sum_mini
#
#
# def func_filter(s: str): #1h 20m
#     li = s.split(" ")
#     return sum(list(map(chang_to_num, li)))
#
#
# def func_s(x):
#     delay = sum(list(map(func_filter, x["delays"])))
#     return x["status"], -delay, x["name"]
#
#
# buses = [
#         {
#            "delays": ['1h 20m', '25m', '3h', '2h 1m'],
#            "status": 'bad',
#            "name": "Jacob",
#            "route_num": 560
#         },
#        {
#            "delays": ['20m', '5m', '3h'],
#            "status": 'great',
#            "name": "Moshe",
#            "route_num": 769
#         },
#        {
#            "delays": ['2h 3m'],
#            "status": 'good',
#            "name": "Jack",
#            "route_num": 766
#         },
#        {
#            "delays": ['6h'],
#            "status": 'great',
#            "name": "Mark",
#            "route_num": 876
#         },
#          {
#            "delays": ['2h 3m'],
#            "status": 'good',
#            "name": "Anna",
#            "route_num": 456
#         },
# ]
#
# print(sorted(buses, key=func_s, reverse=True))

# ----------------------------------------------------------------------------
# D4, 3