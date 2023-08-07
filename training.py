

class Board:
    """ Class for little boar 3 x 3 
    """
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

    def check_move(self, ultimate_board, board_numb, place_numb):
        if not 0 <= board_numb < 9:
            print("Invalid board number! Please enter a number between 1 and 9.")
            return False

        if not 0 <= place_numb < 9:
            print("Invalid place number! Please enter a number between 1 and 9.")
            return False

        if ultimate_board.board_list[board_numb].board[place_numb] != 0:
            print("That place is already occupied! Please choose another place.")
            return False
            
        return True
        
        
        # new_list = [range(9)]
        # diagonal = new_list[2::3-1][:-1]
        # for i in range(3):
        #     each_line = new_list[i*3:(i+1)*3]
        #     print(each_line)
        # print(diagonal)

    def check_win(self):
        pass

    def user_input(self, message):
        num = input(message)
        return int( num )


def main():
    new_board = UltimateBoard()
    game = Game()

    while game.winner is None:
        
        print(f"Current player: {game.player}")
        board_numb = game.user_input("Enter board number from 1 to 9:") - 1 
        place_numb= game.user_input("Enter place number from 1 to 9: ") - 1 
            
        if game.check_move(new_board, board_numb, place_numb):
            if game.player == 1:
                new_board.board_list[board_numb].board[place_numb] = 1
            if game.player == 2:
                new_board.board_list[board_numb].board[place_numb] = -1
            else :
                print("Not valid Player")
                
            game.player = 1 if game.player == 2 else 2
            print(new_board)
        else:
            print("Invalid move! Please enter a number between 1 and 9.")

    print(f"Player {game.winner} wins!")
    

if __name__ == "__main__":
    main()