

class Board:
    def __init__(self):
        self.size = 3
        self.board = []
        filler = 0

        for _ in range(self.size):
            self.board.append( [filler for _ in range(self.size)] )


    def __str__(self):
        print_board = ''

        for i in range( self.size ):
            print_board += str(self.board[i])
            print_board += "| \n"

        return print_board


class UltimateBoard:
    def __init__(self):
        self.board_list = []
        self.big_board_size = 9


        for _ in range(self.big_board_size):
            self.board_list.append(Board())

    def __str__(self):
        print_board = ''

        print_board += str(self.board_list[0])
        # for i in range(self.big_board_size):
        #     if i % 3 == 2:
        #         print_board += str(self.board_list[i])
        #     else: 
        #         # print_board += str(self.board_list[i])
        #         print_board += "__________\n"

    #     for i in range(9):
    #         print("-")
    #         for j in range(9):
    #             print(board[i][j], end=" ")
    #             if j % 3 == 2:
    #                 print("|", end=" ")
    #         print()
    #         if i % 3 == 2:
    #             print("-" * 23) 

        return print_board


class Game:
    def __init__(self):
        self.player = 1
        self.winner = None 

    def check_move(self):
        new_list = [1,2,3,4,5,6,7,8,9]
        diagonal = new_list[2::3-1][:-1]
        for i in range(3):
            each_line = new_list[i*3:(i+1)*3]
            print(each_line)
        print(diagonal)

    def check_board(self):
        pass

def user_input():
    num = input('Enter a number: ')

def main():
    new_board = UltimateBoard()
    print(new_board)
    

if __name__ == "__main__":
    main()