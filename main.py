import boards
import os
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
    def first_blank(cls):
        # 1) find the first empty spot
        for chosen_row_index, chosen_row in enumerate(cls.board):
            for chosen_column_idx, chosen_num in enumerate(chosen_row):
                if cls.board[chosen_row_index][chosen_column_idx] == 0:  # 2) find the lowest available number
                    return [chosen_row_index, chosen_column_idx]
                    # Now that the empty spot has been chosen
                    # We add one to it and check horizontal


                    # check vertical
                    for row_idx, row in enumerate(cls.board):
                        for column_idx, element in enumerate(row):
                            if column_idx == chosen_column_idx:
                                if element == chosen_num and chosen_row_index != row_idx:
                                    break
                    # If that check fails, add one and re-check horizontal until horizontal check passes
                    # Save this as the base case
                    # Then check vertical, if it fails, add 1 until it passes
                    # Then check square, if it fails, add 1 until it passes
                    # If all checks pass, then exit the while loop
                    # Program will then move to the next empty spot
                    # If a number fails all test and is > 9, then reset the board and make the chosen spot the base case + 1

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
    def solve(cls, first_blank):
        base_case_row = first_blank[0]
        base_case_column = first_blank[1]

        cls.board[base_case_row][base_case_column] += 1
        chosen_num = cls.board[chosen_row_index][chosen_column_idx]
        print('---------------------')
        cls.show_board()




            # check same square



        # 3) Go through each empty spot, adding the lowest possible number that's allowed
        # 4) If you run into a spot where no numbers are allowed, go back to the original spot
        # 5) Change that spot to the next lowest available number, and go back to step 3
        # 6) If every spot gets a number assigned, then you have a solution
        # 7) Save the solution as "East solution 1"
        # 8) Increment the original spot again and check for additional solutions until you've tried all possible numbers

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
