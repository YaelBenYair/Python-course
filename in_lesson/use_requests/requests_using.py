import json
from pytz import timezone
import pytz
import requests
import pprint
import datetime


# BORED_URL = "https://www.boredapi.com/api/activity"
# response = requests.get(BORED_URL)
# print(response)
# print(response.status_code)
# print(response.text)
# res = json.loads(response.text)  # it will be dict
#
# to_js = response.json()  # requests function
# print(to_js['activity'])

# response = requests.get("http://www.google.com")
# print(response.status_code)
# print(response.text)  # return html!
# print(response.json())  # error


# name = input("insert name: ")
# NAME_URL = "https://api.nationalize.io/"
# respons = requests.get(NAME_URL, params={'name': name})
# if respons.status_code > 400:
#     raise Exception()
# js_name = respons.json()
# pprint.pprint(js_name)
#
# high_prob = js_name['country'][0]['probability']
# code = None
# inx_name = None
# for inx, country in enumerate(js_name['country']):
#     if country['probability'] >= high_prob:
#         high_prob = country['probability']
#         code = country['country_id']
#         inx_name = inx
# CODE_URL = f"https://restcountries.com/v3.1/alpha/{code}"
# country_exp = requests.get(CODE_URL)
# js_country = country_exp.json()
#
# print(f"The name {name} is high probability of {js_name['country'][inx_name]['probability']} in country:")
# print(js_country[0]['name']['common'])
# print(f"The continent the country is located: {js_country[0]['region']}")
# print(f"The language spoken in the country: {js_country[0]['languages']}")
#
# format = "%Y-%m-%d %H:%M:%S %Z%z"
# # time_now = datetime.datetime.now(timezone('UTC'))
# time_now = datetime.datetime.utcnow()
# tz = datetime.datetime.utcnow().astimezone(pytz.timezone(js_country[0]['name']['common']))
# print(tz.strftime(format))

# time_zone_format = datetime.datetime.strptime(time_zone, "%Z%z")
# now_time = time_now.astimezone(timezone(time_zone_format.strftime("%Z%z")))





# import requests
#
# url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"
#
# querystring = {"lat":"35.5","lon":"-78.5"}
#
# headers = {
# 	"X-RapidAPI-Key": "b24a9ecf38mshc19aed2a1f0db70p195786jsn6cb1adf82282",
# 	"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)


import requests

# url = "https://love-calculator.p.rapidapi.com/getPercentage"
#
# querystring = {"sname":"hodaya","fname":"yaron"}
#
# headers = {
# 	"X-RapidAPI-Key": "b24a9ecf38mshc19aed2a1f0db70p195786jsn6cb1adf82282",
# 	"X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)

# url = "www.thecocktaildb.com/api/json/v1/1/filter.php?g=Cocktail_glass"

d = datetime.date(year=2022, month=11, day=10)
print(d.month)
day = datetime.timedelta(days=1)
print(d+day)

# import requests
#
# url = "https://weatherapi-com.p.rapidapi.com/future.json"
#
# querystring = {"q":"Israel","dt":"2022-12-25"}
#
# headers = {
# 	"X-RapidAPI-Key": "b24a9ecf38mshc19aed2a1f0db70p195786jsn6cb1adf82282",
# 	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)

