import json
from pytz import timezone
import pytz
import requests
import pprint
import datetime
from concurrent.futures import ThreadPoolExecutor, wait
import concurrent
import os

# E3 3 -----------------------------------------------------------------------------------------------------------------


def create_files_names_details(base_prefix: str, name_in: list):
    if not os.path.exists(base_prefix):
        # If the path to the file does not exist, this function generates the path to the file
        os.makedirs(base_prefix)


    executor = ThreadPoolExecutor(max_workers=20)
    futures = []

    for inx, name in enumerate(name_in):

        path_file = os.path.join(base_prefix, f"{name}_{inx}.txt")

        future = executor.submit(display_information, path_file, name)  # does not block
        futures.append(future)

    done, not_done = wait(futures,
                          return_when=concurrent.futures.ALL_COMPLETED)
    print(f"done: {len(done)}")
    print(f"not done: {len(not_done)}")



def display_information(path_file, name):


    NAME_URL = "https://api.nationalize.io/"
    respons = requests.get(NAME_URL, params={'name': name})
    if respons.status_code > 400:
        raise Exception()
    js_name = respons.json()
    # print(js_name)

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
    js_country = country_exp.json()

    writing_to_file(path_file, js_country, name)


def writing_to_file(path_file, result, name):

    with open(path_file, "w") as fh:

        fh.writelines(f"{name} - nationality: {result[0]['name']['common']}")


if __name__ == '__main__':
    start = datetime.datetime.utcnow()
    names = ["Kenyon", "Deshawn", "Michaela", "Molly", "Barrett", "Steven", "Brisa", "Zackery", "Kamora", "Sara",
             "Jaycee",
             "Leland", "Danny", "Ashlee", "Royce", "Bryce", "Anabel", "Skyler", "Cristian", "Shannon", "Aditya",
             "Asher",
             "Quintin", "Hunter", "Rose", "Ronin", "Zion", "Rayne", "Nyasia", "Sanaa", "Dominic", "Tyshawn", "Gillian",
             "Clayton", "Easton", "Julio", "Coby", "Melany", "Bradyn", "Jazlene", "Myah", "Zayden", "Noemi", "Brooks",
             "Mckenzie", "Khalil", "Ruben", "Kristina", "Dixie", "Sawyer", "Ali", "Nasir", "Kaylynn", "Messiah",
             "Kevin",
             "Will", "Cordell", "Dereon", "Jamari", "Adrien", "Ashtyn", "Santos", "Isabela", "Lucas", "Harley",
             "Esteban",
             "Zain", "Alma", "Elliot", "Collin", "Alexa", "Magdalena", "Kristopher", "Kaya", "Jaydin", "Aimee", "June",
             "Ryland", "Belinda", "Kennedy", "Mohammed", "Kenna", "Kaia", "Ada", "Frida", "Valeria", "Noe", "Savannah",
             "Jorge", "Claire", "Abdullah", "Hillary", "Drake", "Kristen", "Amelia", "Marcus", "Liana", "Saniya",
             "Karissa",
             "Jasper"]
    create_files_names_details("D:\\Full Stack Python\\Python_Course\\in_lesson\\multithreading\\file_write", names)
    end = datetime.datetime.utcnow()
    print(f"Time took: {(end - start).total_seconds()}s")


# yael,tom,liam,shira,rachel,noa


