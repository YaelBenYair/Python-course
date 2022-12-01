import between
from game_play import GamePlay


# ------ main ----------------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    name = None
    print("Welcome to Tic Tac Toe game\n")
    yes_no = True
    winn_play = False
    bord_full = False
    stuck = False
    count_num_games = 0


    # print(bord)

    x = '\033[1;1;36m'
    e = '\033[1;0m'
    o = '\033[4;1;31m'

    player1 = input("Name player 1: ").strip()
    player2 = input("Name player 2: ").strip()



    while yes_no:

        print()
        # get from the user the size of the bord and return num and list of the bord
        bord, bord_size = between.bord_size_print()

        # setting up a game
        game = GamePlay(bord_size, bord)
        # game.display_of_the_bord()

        # random who play first
        player1_play_turn, player2_play_turn = game.random_who_first()  # rand(0,1) and enter X to the first

        # the object player status save the number who first thet we will know who play - 'X' or 'O'.
        # 2 = first, 1 = second
        player1_status = player1_play_turn + 1
        player2_status = player2_play_turn + 1

        print()
        # between.game_main()
        not_winn = True
        while not_winn:
            # check who play turn, 1 = turn
            if player1_play_turn == 1:
                place_insert = between.check_input_player(player1, bord_size)

                between.player_play(game, place_insert, player1_status, player1, bord_size)

                winn_play, name = between.winning_check(player1, game)

                player1_play_turn -= 1
                player2_play_turn +=1

            else:
                place_insert = between.check_input_player(player2, bord_size)

                between.player_play(game, place_insert, player2_status, player2, bord_size)

                winn_play, name = between.winning_check(player2, game)

                player2_play_turn -= 1
                player1_play_turn += 1


            game.display_of_the_bord()

            if winn_play:
                not_winn = False

            bord_full = game.check_full_bord()
            if bord_full:
                not_winn = False

            stuck = between.check_game_stuck(game)
            if stuck:
                not_winn = False

        print()

        if winn_play:
            print(f"{name} winn")

        if bord_full:
            print("No one won")

        if stuck:
            print("The game is stuck")

        if between.check_play_again():
            yes_no = True
        else:
            yes_no = False

        # game.initialize_board()
        # count_num_games += 1

    print("\nBye Bye!")



















