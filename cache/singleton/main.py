from pprint import pprint

from apikey import key
from weather_request import weather_request
from concurrent.futures import ThreadPoolExecutor

if __name__ == '__main__':
    api_key = key
    for i in [{'name': 'Israel', 'code': 'ISR'}, {'name': 'Israel', 'code': 'ISR'}]:
        data = weather_request(api_key, i['name'], i['code'])
        pprint(data)
        print()
    # with


