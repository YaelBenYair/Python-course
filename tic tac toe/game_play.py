import random

# player 1 - get from random 'X'
# player 2 - get from random 'O'
# game_bord_size - get from main
# bord_play - insert in def
class GamePlay:

    def __init__(self, game_bord_size: int, bord_play: list):

        self.game_bord_size = game_bord_size
        self.bord_play = bord_play

        self.x = '\033[4;1;36m'
        self.e = '\033[1;0m'
        self.o = '\033[4;1;31m'

        self.player1 = f'{self.x}X{self.e}'
        self.player2 = f'{self.o}O{self.e}'

    # print the bord
    def display_of_the_bord(self):
        position = 0
        for i in range(self.game_bord_size):
            for j in range(position, position + self.game_bord_size):
                print(self.bord_play[j], end="")
            position = j+1

            print()

    # rand(0,1) return who the first
    def random_who_first(self) -> tuple[int, int]:
        rand = random.randint(0, 1)
        if rand == 0:
            return 1, 0
        else:
            return 0, 1

    def enter_player_play(self, player, place_insert):
        if player == 1:
            if (self.bord_play[place_insert-1]) == f'| {self.player2} |' \
                    or (self.bord_play[place_insert-1]) == f'| {self.player1} |':
                return False
            else:
                self.bord_play[place_insert-1] = f"| {self.player2} |"
                return True
        elif player == 2:
            if (self.bord_play[place_insert-1]) == f'| {self.player2} |' \
                    or (self.bord_play[place_insert-1]) == f'| {self.player1} |':
                return False
            else:
                self.bord_play[place_insert - 1] = f"| {self.player1} |"
                return True

    def check_winning_row(self):
        slot = self.bord_play[0]
        place = 0
        count = 0

        for i in range(self.game_bord_size):
            for j in range(place, place + self.game_bord_size):
                if slot == self.bord_play[j]:
                    count += 1

            if count == self.game_bord_size:
                return True

            place = j + 1

            # check that the list will not be out of range
            if j < (self.game_bord_size ** 2 - 1):
                slot = self.bord_play[place]

            count = 0
        return False

    def check_winning_column(self):
        slot = self.bord_play[0]
        count = 0

        for i in range(self.game_bord_size):
            for j in range(i, self.game_bord_size ** 2, self.game_bord_size):
                if slot == self.bord_play[j]:
                    count += 1

            if count == self.game_bord_size:
                return True

            slot = self.bord_play[i+1]

            count = 0
        return False

    def check_winning_diagonal(self):
        slot = self.bord_play[0]
        count = 0

        # diagonal left to right
        for i in range(0, self.game_bord_size ** 2, self.game_bord_size + 1):

            if slot == self.bord_play[i]:
                count += 1

        if count == self.game_bord_size:
            return True

        # diagonal right to left
        # place = self.game_bord_size -1
        count = 0
        slot = self.bord_play[self.game_bord_size - 1]
        for i in range(self.game_bord_size - 1, self.game_bord_size ** 2, self.game_bord_size -1):

            if slot == self.bord_play[i]:
                count += 1

        if count == self.game_bord_size:
            return True

        return False

    def check_full_bord(self):
        count = 0

        for i in self.bord_play:
            if i == f'| {self.player1} |' or i == f'| {self.player2} |':
                count += 1

        if count == len(self.bord_play):
            return True

        return False

    def stuck_row(self):
        place = 0
        count = 0
        count_x = 0
        count_o = 0

        for i in range(self.game_bord_size):
            for j in range(place, place + self.game_bord_size):
                if f'| {self.player1} |' == self.bord_play[j]:
                    count_x += 1
                if f'| {self.player2} |' == self.bord_play[j]:
                    count_o += 1
            # check if there is X and O in the row
            if count_x > 0 and count_o > 0:
                count += 1

            count_x = 0
            count_o = 0

            place = j + 1

            # check that the list will not be out of range
            if j < (self.game_bord_size ** 2 - 1):
                slot = self.bord_play[place]

        # if in 3 rows i have X and O (together in the same row) then it return True - the rows are stuck
        if count == self.game_bord_size:
            return True

        return False

    def stuck_column(self):
        place = 0
        count = 0
        count_x = 0
        count_o = 0

        for i in range(self.game_bord_size):
            for j in range(i, self.game_bord_size ** 2, self.game_bord_size):
                if f'| {self.player1} |' == self.bord_play[j]:
                    count_x += 1
                if f'| {self.player2} |' == self.bord_play[j]:
                    count_o += 1

            if count_x > 0 and count_o > 0:
                count += 1

            count_x = 0
            count_o = 0

        if count == self.game_bord_size:
            return True

        return False

    def stuck_diagonal(self):

        count = 0
        count_x = 0
        count_o = 0

        # diagonal left to right
        for i in range(0, self.game_bord_size ** 2, self.game_bord_size + 1):

            if f'| {self.player1} |' == self.bord_play[i]:
                count_x += 1
            if f'| {self.player2} |' == self.bord_play[i]:
                count_o += 1

        if count_x > 0 and count_o > 0:
            count += 1

        count_x = 0
        count_o = 0
        # diagonal right to left
        # place = self.game_bord_size -1
        for i in range(self.game_bord_size - 1, self.game_bord_size ** 2, self.game_bord_size - 1):

            if f'| {self.player1} |' == self.bord_play[i]:
                count_x += 1
            if f'| {self.player2} |' == self.bord_play[i]:
                count_o += 1

        if count_x > 0 and count_o > 0:
            count += 1

        if count == 2:
            return True

        return False




        #method:
# setting_up_list_bord



#
#
#
# check_full_bord
# check_play_again
# initialize_board


















