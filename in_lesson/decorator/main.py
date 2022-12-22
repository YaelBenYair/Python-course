import time
from func_decorator import performance_log, single_str_arg


@performance_log('ms')
def long_running_func(num, iters):
    val = 1
    for i in range(iters):
        val *= num
    return val




@single_str_arg
def str_func(sr: str) -> str:
    return sr.lower()




if __name__ == '__main__':
    s = input("str: ")
    print(str_func(s))

    # long_running_func(17, 1000)
    # long_running_func(17, 10000)
    # long_running_func(17, 100000)





















