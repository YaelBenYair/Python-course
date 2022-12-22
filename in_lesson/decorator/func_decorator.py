import time
# def
# def
# time
# in def
# time

def performance_log(time_units= 's'):

    def wrapper(func):

        def time_log(*args, **kwargs):

            time_func = time.perf_counter if time_units != 'ns' else time.perf_counter_ns

            t1_start = time_func()
            result = func(*args, **kwargs)
            t2_stop = time_func()

            exec_time = t2_stop - t1_start
            if time_units == 'ms':
                exec_time *= 1000

            print(f"The time the function takes to run: {exec_time}")

            return result

        return time_log
    return wrapper




class InvalidArgument(Exception):
    pass

# ----------------------------------------------------------------------------------------------------------------------
# Implement a decorator @single_str_arg that validates that function received exactly one argument and that the
# argument type is string. If the validation fails, the decorator should raise an InvalidArgument exception.


def single_str_arg(func):
    def func_str(*args, **kwargs):
        if len(args) != 1 or len(kwargs) != 0 or not isinstance(args[0], str):
            raise InvalidArgument()
        return func(*args, **kwargs)

    return func_str

# def single_str_arg(func):
#     def validator(*args, **kwargs):
#         if len(args) == 1 and isinstance(args[0], str):
#             result = func(*args, **kwargs)
#             return result
#         else:
#             raise InvalidArgument()
#     return validator

#
# def single_str_arg(other_function):
#     def validator(*args, **kwargs):
#         if len(args) == 1 and isinstance(args[0], str):
#             result = other_function(*args, **kwargs)
#             return result
#         else:
#             raise InvalidArgument()
#
#     return validator


# @single_str_arg
# def str_func(sr: str) -> str:
#     return sr.lower()
#
#
#
#
# if __name__ == '__main__':
#
#
#     s = input("str: ")
#     print(str_func(s))
