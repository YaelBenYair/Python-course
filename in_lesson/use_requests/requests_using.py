import json
from pytz import timezone
import pytz
import requests
import pprint
import datetime
from concurrent.futures import ThreadPoolExecutor, wait
import concurrent


def names_details(name_in: str):
    name_list = name_in.split(",")
    dict_information: dict[str: list] = {}

    executor = ThreadPoolExecutor(max_workers=10)
    futures = []

    for name in name_list:

        future = executor.submit(display_information, name, dict_information)  # does not block
        futures.append(future)


    done, not_done = wait(futures,
                              return_when=concurrent.futures.ALL_COMPLETED)
    print(f"done: {len(done)}")
    print(f"not done: {len(not_done)}")
    return dict_information

def display_information(name, dict_information):
    NAME_URL = "https://api.nationalize.io/"
    respons = requests.get(NAME_URL, params={'name': name})
    if respons.status_code > 400:
        raise Exception()
    js_name = respons.json()
    # pprint.pprint(js_name)

    high_prob = js_name['country'][0]['probability']
    code = None
    inx_name = None
    for inx, country in enumerate(js_name['country']):
        if country['probability'] >= high_prob:
            high_prob = country['probability']
            code = country['country_id']
            inx_name = inx

    CODE_URL = f"https://restcountries.com/v3.1/alpha/{code}"
    country_exp = requests.get(CODE_URL)
    if country_exp.status_code > 400:
        raise Exception()
    js_country = country_exp.json()

    dict_information[name] = [f"The name {name} is high probability of {js_name['country'][inx_name]['probability']} "
                              f"in country: {js_country[0]['name']['common']}",
                              f"The continent the country is located: {js_country[0]['region']}",
                              f"The language spoken in the country: {js_country[0]['languages']}"]







if __name__ == '__main__':

    start = datetime.datetime.utcnow()
    name_in = input("insert 10 names: ")
    d = names_details(name_in)
    pprint.pprint(d)
    end = datetime.datetime.utcnow()
    print(f"Time took: {(end - start).total_seconds()}s")




    # Time took: 9.532686s
    # Time took: 6.799645s


# yael,tom,liam,shira,rachel,noa
# NAMES = ["Kenyon", "Deshawn", "Michaela", "Molly", "Barrett", "Steven", "Brisa", "Zackery", "Kamora", "Sara", "Jaycee",
#          "Leland", "Danny", "Ashlee", "Royce", "Bryce", "Anabel", "Skyler", "Cristian", "Shannon", "Aditya", "Asher",
#          "Quintin", "Hunter", "Rose", "Ronin", "Zion", "Rayne", "Nyasia", "Sanaa", "Dominic", "Tyshawn", "Gillian",
#          "Clayton", "Easton", "Julio", "Coby", "Melany", "Bradyn", "Jazlene", "Myah", "Zayden", "Noemi", "Brooks",
#          "Mckenzie", "Khalil", "Ruben", "Kristina", "Dixie", "Sawyer", "Ali", "Nasir", "Kaylynn", "Messiah", "Kevin",
#          "Will", "Cordell", "Dereon", "Jamari", "Adrien", "Ashtyn", "Santos", "Isabela", "Lucas", "Harley", "Esteban",
#          "Zain", "Alma", "Elliot", "Collin", "Alexa", "Magdalena", "Kristopher", "Kaya", "Jaydin", "Aimee", "June",
#          "Ryland", "Belinda", "Kennedy", "Mohammed", "Kenna", "Kaia", "Ada", "Frida", "Valeria", "Noe", "Savannah",
#          "Jorge", "Claire", "Abdullah", "Hillary", "Drake", "Kristen", "Amelia", "Marcus", "Liana", "Saniya", "Karissa",
#          "Jasper"]
























# print(f"The name {name} is high probability of {js_name['country'][inx_name]['probability']} in country:")
    # print(js_country[0]['name']['common'])
    # print(f"The continent the country is located: {js_country[0]['region']}")
    # print(f"The language spoken in the country: {js_country[0]['languages']}")

        # format = "%Y-%m-%d %H:%M:%S %Z%z"
        # time_now = datetime.datetime.utcnow()
        # tz = datetime.datetime.utcnow().astimezone(pytz.timezone(js_country[0]['name']['common']))
        # print(tz.strftime(format))