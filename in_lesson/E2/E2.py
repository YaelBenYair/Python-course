




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

