from pprint import pprint
import requests
import datetime
from exeprions import *


# url = "https://edamam-recipe-search.p.rapidapi.com/search"
#
# querystring = {"q":"pasta"}
#
# headers = {
# 	"X-RapidAPI-Key": "b24a9ecf38mshc19aed2a1f0db70p195786jsn6cb1adf82282",
# 	"X-RapidAPI-Host": "edamam-recipe-search.p.rapidapi.com"
# }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# pprint(response.text)


class CocktailsAndGames:

	def __init__(self):
		self._history_cockt: dict[datetime: list[str]] = {}
		# cocktail_ids: dict[int: Cocktail] = {}

	def get_history(self):
		return self._history_cockt

	def get_history_dy_date(self, date_he: datetime):
		if date_he not in self._history_cockt:
			raise DateNotFoundError()
		return self._history_cockt[date_he]

	def add_history(self, cockt: list):
		date_today = datetime.datetime.now().date()
		if date_today not in self._history_cockt:
			self._history_cockt[date_today] = []
		self._history_cockt[date_today].append(cockt)

	@staticmethod
	def get_random_activity() -> list:
		url_bored = "https://www.boredapi.com/api/activity"
		result_bored = requests.get(url_bored).json()
		return ["activity: " + result_bored["activity"],
				"participants: " + result_bored["participants"],
				"link: " + result_bored["link"]]

	@staticmethod
	def _get_cockt_ingredient(js):
		ingredient = []
		count = 1
		while js["drinks"][0][f"strMeasure{count}"] is not None:
			ingredient.append(js["drinks"][0][f"strMeasure{count}"] + js["drinks"][0][f"strIngredient{count}"])
			count += 1
		return ingredient

	def _get_cock(self, result) -> list:
		js_resolt = result.json()

		ingrid = self._get_cockt_ingredient(js_resolt)
		cocktail_detail = ["name: " + js_resolt["drinks"][0]["strDrink"], ingrid,
						   "Instructions: " + js_resolt["drinks"][0]["strInstructions"],
						   "Glass type: " + js_resolt["drinks"][0]["strGlass"]]
		self.add_history(cocktail_detail)
		return cocktail_detail

	@staticmethod
	def check_requests(result):
		if result.status_code > 400:
			raise StatusCodeError(result.status_code)

	def get_cocktail_by_id(self, id_cockt: int) -> list:
		url = f"http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={id_cockt}"
		result = requests.get(url)
		self.check_requests(result)
		return self._get_cock(result)

	def sort_by_search(self, url) -> dict[str: str]:
		search_result = {}
		result = requests.get(url)
		self.check_requests(result)
		result = result.json()
		for item in result["drinks"]:
			search_result[item["idDrink"]] = item["strDrink"]

		return search_result

	def get_cock_by_ingredient(self, ingre: str) -> dict[str: str]:
		url = f"http://www.thecocktaildb.com/api/json/v1/1/filter.php?i={ingre}"
		return self.sort_by_search(url)

	def get_cock_by_name(self, name: str) -> dict[str: str]:
		url = f"http://www.thecocktaildb.com/api/json/v1/1/search.php?s={name}"
		return self.sort_by_search(url)

	def get_cock_by_letter(self, letter: str) -> dict[str: str]:
		url = f"http://www.thecocktaildb.com/api/json/v1/1/search.php?f={letter}"
		return self.sort_by_search(url)

	def get_random_cockt(self) -> list:
		url = f"www.thecocktaildb.com/api/json/v1/1/random.php"
		result = requests.get(url)
		self.check_requests(result)
		return self._get_cock(result)













# class Cocktail:
#
# 	def __init__(self, id_cockt: int, drink_name: str, glass_type: str, instructions: str, ingredient: list):
# 		self._id_cockt = id_cockt
# 		self._drink_name = drink_name
# 		self._glass_type = glass_type
# 		self._instructions = instructions
# 		self._ingredient = ingredient
#
# 	def __str__(self):
# 		return f"Id: {self._id_cockt}\n" \
# 			   f"Drink name: {self._drink_name}\m"
#
# 	def __repr__(self):
# 		pass








































