from game_play import GamePlay


def check_play_again():
    y_n = input("Do you want to play again?\n1 for yes, 2 for no: ")
    while not y_n.isdigit() or int(y_n) > 2 or int(y_n) < 1:
        print("\n\033[4;1;31mPlease enter 1 for yes, 2 for no\033[1;0m")
        y_n = input("Do you want to play again? ")

    if int(y_n) == 1:
        return True

    return False


def player_play(game: GamePlay, place_insert: int, status: int, player, size):

    cant_play = True

    # loop for insert player game correct. if the slot that the player selected is occupied
    # the function send him to select again
    while cant_play:
        status_game = game.enter_player_play(status, place_insert)
        if status_game:
            cant_play = False
        else:
            print("There is an object in this slot!")
            place_insert = check_input_player(player, size)



def bord_input_check() -> int:
    bord = input("Enter the size of the bord, 3-9: ")
    while not bord.isdigit() or int(bord) < 3:
        print("\n\033[4;1;31mPlease enter number in range 3-9\033[1;0m")
        bord = input("Enter the size of the bord, 3-9: ")
    return int(bord)


def bord_size_print():
    g = '\033[1;1;37m'
    e = '\033[1;0m'
    bord_size = bord_input_check()
    bord = []
    count = 1
    for i in range(1, bord_size+1):
        for j in range(1, bord_size + 1):
            if count < 10:
                bord.append(f"|{g}_{count}_{e}|")
                print(f"|{g}_{count}_{e}|", end= "")
            else:
                bord.append(f"{g}|_{count}{e}|")
                print(f"|{g}_{count}{e}|", end="")
            count += 1
        print()
    return bord, bord_size


def check_input_player(player, size):
    place_insert = input(f"{player} turn: ")
    while not place_insert.isdigit() or int(place_insert) < 1 or int(place_insert) > size*size:
        print(f"Error! pleas enter num between 1 - {size*size} ")
        place_insert = input(f"{player} turn: ")
    return int(place_insert)


















# def check_game_stuck(game: GamePlay):
#     stuck_row = False
#     stuck_column = False
#     stuck_diagonal = False
#
#     if game.stuck_row():
#         stuck_row = True
#     if game.stuck_column():
#         stuck_column = True
#     if game.stuck_diagonal():
#         stuck_diagonal = True
#
#     if stuck_row and stuck_column and stuck_diagonal:
#         return True
#     return False


# def winning_check(name_player: str, game: GamePlay):
#     winn = None
#     if game.check_winning_row():
#         winn = True
#     elif game.check_winning_column():
#         winn = True
#     elif game.check_winning_diagonal():
#         winn = True
#     else:
#         winn = False
#
#     return winn, name_player
