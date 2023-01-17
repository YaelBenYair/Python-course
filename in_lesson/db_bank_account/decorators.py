

def intvaluecheck(func):

    def wrapper(*args, **kwargs):
        if len(args) == 5 and len(kwargs) == 0:
            count = 0
            for num in args:
                if count == 0:
                    count += 1
                elif not isinstance(num, int):
                    raise ValueError()
            func(*args, **kwargs)

    return wrapper

# if (1, 9, 4) is int:
#     print(True)
# else:
#     print(False)




