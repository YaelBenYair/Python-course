import datetime
import multiprocessing
from concurrent.futures import ProcessPoolExecutor, Future
import time


def factorial(num_f):
    for j in range(500):
        factor = 1
        for num in range(1, num_f+1):
            factor *= num
        return factor, num_f


# def display(f: Future):
#     print(f"{f.result()[1]}! = {f.result()[0]}")





if __name__ == '__main__':

    num_fact = input("insert number num: ")
    start = datetime.datetime.utcnow()
    futures = []
    with ProcessPoolExecutor(max_workers=8) as executor:
        # for n in range(100_000):
        for n in range(200):
            futures.append(executor.submit(factorial, int(num_fact)))

        # for f in futures:
        #     f.add_done_callback(display)
    end = datetime.datetime.utcnow()
    print(f"Time took: {(end - start).total_seconds()}s")





# a = [[1500]* 100]*100
# print(a)







