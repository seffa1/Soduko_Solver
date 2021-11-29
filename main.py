import boards
import os
from collections import deque
import sys
import timeit
import time
import faulthandler
import psutil


def clear():
    os.system('cls')


class Board:
    board = None

    @classmethod
    def load_board(cls, difficulty):
        cls.board = boards.boards[difficulty]

    @classmethod
    def show_board(cls):
        print(f'Back Track Count: {cls.back_track_count}')
        print(f'Iteration Count: {cls.iteration_count}')
        print(f'Stack Length: {len(cls.back_track_stack)}')
        print(f'Recurse Depth: {cls.recurse_depth}')
        print(f'MB used: {cls.process.memory_info()[0] // (1024 * 1024)}')
        row_length = len(cls.board[0])
        row_string = ''
        row_line_counter = 0
        column_line_counter = 0
        num_count = 0
        for row in cls.board:
            for num in row:
                row_string += str(num) + '  '
                row_line_counter += 1
                if row_line_counter % 3 == 0:
                    row_string += '| '
                    row_line_counter = 0
                num_count += 1
                if num_count % row_length == 0:

                    print(row_string)
                    row_string = ''
                    num_count = 0
                    column_line_counter += 1
                    if column_line_counter % 3 == 0:
                        print('- - - - - - - - - - - - - - - -')
                        column_line_counter = 0

    @classmethod
    def find_empty(cls):
        # 1) find the next empty spot
        for chosen_row_index, chosen_row in enumerate(cls.board):
            for chosen_column_idx, chosen_num in enumerate(chosen_row):
                if cls.board[chosen_row_index][chosen_column_idx] == 0:  # 2) find the lowest available number
                    return chosen_row_index, chosen_column_idx
        return None

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
        # The number we are checking against
        input_number = cls.board[row_index][column_index]

        # Finds the minimum row/column index of the 3x3 square our input is in using // to round down to it
        box_row_index = row_index // 3
        box_column_index = column_index // 3

        # Now we iterate through the indexes of the 3x3 box we are in, and put those index into our board
        # Then check if a number is the same but in a different square than our input
        for row in range(box_row_index * 3, box_row_index * 3 + 3):
            for column in range(box_column_index * 3, box_column_index * 3 + 3):
                if cls.board[row][column] == input_number and (row_index, column_index) != (row, column):
                    return False
        return True

    @classmethod
    def is_valid(cls, row_index, column_index):
        valid = True
        if cls.board[row_index][column_index] == 0:
            valid = False

        if not cls.check_horizontal(row_index, column_index):
            valid = False

        if not cls.check_vertical(row_index, column_index):
            valid = False

        if not cls.check_square(row_index, column_index):
            valid = False

        return valid

    # Variables to aid in showing the algo in action
    sleep = .01
    back_track_count = 0
    iteration_count = 0
    show_algo = False
    process = psutil.Process(os.getpid())

    # This stack keeps track of what spots we have been so we can back track
    back_track_stack = deque()

    @classmethod
    def solve(cls):
        while cls.find_empty() is not None:
            if cls.show_algo:
                clear()
                cls.show_board()
                time.sleep(cls.sleep)

            # We always move to the next empty (0) spot on the board
            current_row, current_column = cls.find_empty()

            # Once we find an empty spot, add it to the stack so we can go in reverse if our tests fails
            cls.back_track_stack.append((current_row, current_column))

            # We add 1 to the empty spot until it is valid
            while not cls.is_valid(current_row, current_column):

                # If the number gets to 9 and still isn't valid, we need to backtrack
                while cls.board[current_row][current_column] == 9:
                    # Count the amount of times we backtrac
                    cls.back_track_count += 1

                    # Reset the current spot to 0
                    cls.board[current_row][current_column] = 0
                    if cls.show_algo:
                        clear()
                        cls.show_board()
                        time.sleep(cls.sleep)

                    # Remove the current spot from the stack
                    cls.back_track_stack.pop()

                    # Then set the current spot to be the previous
                    current_row, current_column = cls.back_track_stack[-1]

                # If our number is less than 9, we can add 1 and check it again
                if cls.board[current_row][current_column] < 9:
                    cls.board[current_row][current_column] = cls.board[current_row][current_column] + 1
                    cls.iteration_count += 1
                    if cls.show_algo:
                        clear()
                        cls.show_board()
                        time.sleep(cls.sleep)




def select_difficulty():
    choices = ['1', '2', '3']  # add 2 and 3 here later

    a = ''
    while a not in choices:
        clear()
        sys.setrecursionlimit(10000)
        print(f'recurrsion limit: {sys.getrecursionlimit()}')

        print('Select Difficulty:')
        print('-----------------')
        print('1 <--- Easy')
        print('2 <--- Medium')
        print('3 <--- Hard\n')
        a = input('--->')

    Board.load_board(a)


if __name__ == '__main__':
    faulthandler.enable()
    select_difficulty()
    Board.show_board()
    input("press enter to solve")
    print("Show algo in action?")
    a = ''
    while a not in ['y', 'n']:
        a = input("y/n ---->")

    if a == 'y':
        Board.show_algo = True

    tic = time.perf_counter()
    Board.solve()
    toc = time.perf_counter()
    solve_time = toc - tic

    Board.show_board()
    print(f'Solved puzzle in {solve_time}')
    print("Press enter to quit")
