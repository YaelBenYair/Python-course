import time
from concurrent.futures import ThreadPoolExecutor
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest")
    if response.status_code < 400:
        print(f"quote: {response.json()['quote']}")
    else:
        raise Exception(f"Received response code {response.status_code}")






if __name__ == '__main__':
    num = int(input("Insert num second: "))
    with ThreadPoolExecutor() as tp:
        while num >= 0:
            print(f"{num: .1f} seconds left")
            time.sleep(0.1)
            num -= 0.1
            num = round(num, 1)
            if num == int(num):
                tp.submit(get_quote)


    print("DONE")



