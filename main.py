import boards
import os
from collections import deque

# TEST 

def clear():
    os.system('cls')


class Board:
    board = None

    @classmethod
    def load_board(cls, difficulty):
        cls.board = boards.boards[difficulty]

    @classmethod
    def show_board(cls):
        row_length = len(cls.board[0])
        row_string = ''
        num_count = 0
        for row in cls.board:
            for num in row:
                row_string += str(num) + '  '
                num_count += 1
                if num_count % row_length == 0:
                    print(row_string)
                    row_string = ''
                    num_count = 0


    @classmethod
    def find_empty(cls):
        # 1) find the next empty spot
        for chosen_row_index, chosen_row in enumerate(cls.board):
            for chosen_column_idx, chosen_num in enumerate(chosen_row):
                if cls.board[chosen_row_index][chosen_column_idx] == 0:  # 2) find the lowest available number
                    return chosen_row_index, chosen_column_idx

    @classmethod
    def check_horizontal(cls, row_index, column_index):
        number_to_check = cls.board[row_index][column_index]
        for idx, element in enumerate(cls.board[row_index]):
            if idx != column_index and element == number_to_check:
                return False
            return True

    @classmethod
    def check_vertical(cls, row_index, column_index):
        number_to_check = cls.board[row_index][column_index]
        for row_idx, row in enumerate(cls.board):
            for column_idx, element in enumerate(row):
                if column_idx == column_index:
                    if row_index != row_idx and element == number_to_check:
                        return False
        return True

    @classmethod
    def check_square(cls, row_index, column_index):
        pass

    @classmethod
    def is_valid(cls, row_index, column_index):
        valid = True
        if cls.board[row_index][column_index] == 0:
            valid = False

        if not cls.check_horizontal(row_index, column_index):
            valid = False

        if not cls.check_vertical(row_index, column_index):
            valid = False

        # if not cls.check_square(row_index, column_index):
        #     valid = False

        return valid

    # This stack keeps track of what spots we have been so we can back track
    back_track_stack = deque()

    @classmethod
    def solve(cls):
        # We always move to the next empty (0) spot on the board
        current_row, current_column = cls.find_empty()

        # Once we find an empty spot, add it to the stack so we can go in reverse if our tests fails
        cls.back_track_stack.append((current_row, current_column))

        # We add 1 to the empty spot until it is valid
        while not cls.is_valid(current_row, current_column):

            # If the number gets to 9 and still isn't valid, we need to backtrack
            if cls.board[current_row][current_column] == 9:

                # Reset the current spot to 0
                cls.board[current_row][current_column] = 0

                # Remove the current spot from the stack
                cls.back_track_stack.pop()

                # Then set the current spot to be the previous
                current_row, current_column = cls.back_track_stack[-1]

            # If our number is less than 9, we can add 1 and check it again
            cls.board[current_row][current_column] = cls.board[current_row][current_column] + 1

        # If we got here the current spot was valid and we repeat the process
        cls.solve()




def select_difficulty():
    choices = ['1']  # add 2 and 3 here later

    a = ''
    while a not in choices:
        clear()
        print('Select Difficulty:')
        print('-----------------')
        print('1 <--- Easy')
        print('2 <--- Medium')
        print('3 <--- Hard\n')
        a = input('--->')

    Board.load_board(a)


if __name__ == '__main__':
    select_difficulty()
    Board.show_board()
    input("press enter to solve")
    Board.solve()
