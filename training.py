

def user_input():
    num = input('Enter a number: ')

def create_board():
    # The size of the board
    board_size = 9

    # The symbol 
    empty_space = " "

    # # The empty 2D board
    row = [empty_space for _ in range(board_size)]
    board = [row[:] for _ in range(board_size)]
    return board


def print_board(board):
    print('TODO')
    #iterate through rows
    for i in range(9):
        #iterate through columns
        for j in range(9):
            # print current cell of the board, without starting newline
            print(board[i][j], end="_")

def check_move():
    print('TODO move check')

def main():
    field = 81

    board = create_board()
    print_board(board)
    

if __name__ == "__main__":
    main()