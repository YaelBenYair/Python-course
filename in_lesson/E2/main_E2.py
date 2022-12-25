import os
import pickle
from E2 import CocktailsAndGames
from menu import Menu


if __name__ == '__main__':

    # check whether this is the first time you run the app
    # if this is the first time - create a new class
    if not os.path.exists('files\\cocktails_and_games.pickle'):
        cocktail_and_game = CocktailsAndGames()
    else:
        # this is not the first time - we already have a DB
        # with data from the previous runs
        with open('files\\cocktails_and_games.pickle', 'rb') as fh:
            cocktail_and_game = pickle.load(fh)

    menu = Menu(cocktail_and_game)
    print("Welcome to the cocktail and game night app.\n"
          "In the application you can find all kinds of cocktails and random games\n")
    menu.run()


    # before exiting the program, persist the current state
    # of te system in the file, so next time it will be loaded
    with open('files\\cocktails_and_games.pickle', 'wb') as fh:
        pickle.dump(cocktail_and_game, fh)

    print("\nBye bye")