from pprint import pprint
from threading import Lock
import requests
import datetime

from cache.singleton.singleton_factory import Singleton

lock = Lock()

def weather_request(api_key: str, city_name: str, country_code: str) -> dict:
    weather = Singleton()
    data_now = datetime.datetime.now().date()
    if city_name in weather.cache and data_now in weather.cache[city_name]:
        print('from cache')
        return weather.cache[city_name][data_now]['data']

    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&appid={api_key}'

    response = requests.get(url)
    response = response.json()

    url2 = f'https://api.openweathermap.org/data/2.5/weather?lat={response[0]["lat"]}&lon={response[0]["lon"]}&appid={api_key}'

    response2 = requests.get(url2)
    response2 = response2.json()

    with lock:
        weather.add_to_cache(city_name, {data_now: {'data': response2}})
    return response2

