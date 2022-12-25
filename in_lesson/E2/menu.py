from E2 import CocktailsAndGames
from general_func import *
from exeprions import *
from pprint import pprint


class Menu:
    def __init__(self, cockt_and_game: CocktailsAndGames):
        self.cockt_and_game = cockt_and_game

    @staticmethod
    def _display_dict(result_dict: dict):
        for key, name in result_dict.items():
            print(f"{key}: {name}")

    @staticmethod
    def _display_list(result_list: list):
        for item in result_list:
            print(item)

    def search_menu(self):
        print("[1] - Search cocktail by ingredient\n"
              "[2] - Search cocktail by name\n"
              "[3] - All cocktails by first letter\n"
              "[4] - Random cocktail\n"
              "[5] - Random game\n"
              "[6] - History cocktail search\n"
              "[7] - Exit\n")

    def search_loop(self, msg :str, pattern: str, func_search: callable):
        while True:
            try:
                general_var = insert_string_int(msg, pattern)
                self._display_dict(func_search(general_var))
                break
            except CocktailsAndGamesExeption as e:
                print(e)

    def id_cocktail(self):
        while True:
            try:
                id_cockt = int(insert_string_int("To get information about the cocktail you want, "
                                                 "enter an id cocktail: ", "[0-9]+$"))
                # result = self.search_ingredient(ingred, self.cockt_and_game.get_cock_by_ingredient)
                self._display_list(self.cockt_and_game.get_cocktail_by_id(id_cockt))
                break
            except CocktailsAndGamesExeption as e:
                print(e)


    def run(self):
        exit_upp = False
        while not exit_upp:
            self.search_menu()
            while True:
                try:
                    num = int(input_selection("[1-7]"))
                    break
                except NumberSelectionError as e:
                    print(e)

            match num:
                case 1:
                    self.search_loop("Insert an ingredient: ", "[a-zA-Z]+$", self.cockt_and_game.get_cock_by_ingredient)
                    print("\n")
                    self.id_cocktail()
                    print("\n")
                case 2:
                    self.search_loop("Insert name: ", "[a-zA-Z]+$", self.cockt_and_game.get_cock_by_name)
                    print("\n")
                    self.id_cocktail()
                    print("\n")
                case 3:
                    self.search_loop("Insert a letter: ", "[a-zA-Z]$", self.cockt_and_game.get_cock_by_letter)
                    print("\n")
                    self.id_cocktail()
                    print("\n")
                case 4:
                    self._display_list(self.cockt_and_game.get_random_cockt())
                    print("\n")
                case 5:
                    self._display_list(self.cockt_and_game.get_random_activity())
                    print("\n")
                case 6:
                    pprint(self.cockt_and_game.get_history())
                    print("\n")
                case 7:
                    exit_upp = True
