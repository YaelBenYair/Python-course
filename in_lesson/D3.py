import datetime


# def date_generator(d: datetime):
#     month = d.month
#     date_d = d
#
#     while date_d.month == month:
#         yield date_d
#
#         date_d += datetime.timedelta(days=1)
#
#
# d = datetime.date(year=2022, month=11, day=10)
# for value in date_generator(d):
#     print(value)


# ----------------------------------------------------------------------------------------------------------------------
# D3 2

def batches(n: int, my_list: list):
    li = []
    for item in my_list:
        if len(li) == n:
            yield li
            li = [item]
        else:
            li.append(item)

    if len(li) > 0:
        yield li


my_list = [1, 5, 46, 8, 2, 3, 50, 45]
n = 3
for i in batches(n, my_list):
    print(i)


# ----------------------------------------------------------------------------------------------------------------------
# D3 3


# def fibonacci_numbers(nums):
#     x, y = 0, 1
#     for _ in range(nums):
#         x, y = y, x+y
#         yield x
#
#
# for i in fibonacci_numbers(8):
#     print(i)
#
















