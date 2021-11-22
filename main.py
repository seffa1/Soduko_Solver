import boards
import os


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
    def solve(cls):
        # 1) find the first empty spot
        for row in cls.board:
            for num in row:
                if num == 0:
                    num += 1
                    while True:
                        # check horizontal
                        for i in row:
                            if num == i:
                                nu
                        # check vertical
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
