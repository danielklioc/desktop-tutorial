BOARD_SIZE = 9
ROW_SIZE = 3 


class Board:
    """ Class for little board as array of 9 elements
    """
    def __init__(self):
        self.size = BOARD_SIZE
        filler = 0
        self.board: list(int) = [filler for _ in range(self.size)]
        
    def __getitem__(self, place):
        return self.board[place]
    
    def __setitem__(self, place, value):
        self.board[place] = value
        

    def __str__(self):
        print_board = ""
        for i in range( ROW_SIZE ):
            print_board += " ".join(map(str, self.board[i*ROW_SIZE:ROW_SIZE*(i+1)]))
            print_board += "| \n"
            
            # print_board = " ".join(map(str, self.board[0:3]))
            # print_board += "| \n"
            # print_board += " ".join(map(str, self.board[3:6]))
            # print_board += "| \n"
            # print_board += " ".join(map(str, self.board[6:9]))
        
        return print_board

class Game:
    def __init__(self):
        self.player = 1
        self.winner = None 
        
        
    def user_input(self, message):
        num = input(message)
        return int( num )
    
    
    def check_move(self, ultimate_board, place_numb):
        # if not 0 <= board_numb < 9:
        #     print("Invalid board number! Please enter a number between 1 and 9.")
        #     return False

        if not 0 <= place_numb < 9:
            print("Invalid place number! Please enter a number between 1 and 9.")
            return False

        if ultimate_board[place_numb] != 0:
            print("That place is already occupied! Please choose another place.")
            return False
            
        return True
    
    
    def check_win(self, board):
        print(sum(board[0:3]))
        if sum(board[0:3]) == 3:
            self.winner = 1
        elif sum(board[0::3]) == -3:
            self.winner = 2
        


def main():
    new_board = Board()
    game = Game()
    
    while game.winner is None:
    
        print(f"Current player: {game.player}")
        # board_numb = game.user_input("Enter board number from 1 to 9:") - 1 
        place_numb= game.user_input("Enter place number from 1 to 9: ") - 1 
            
        if game.check_move(new_board,  place_numb):
            if game.player == 1:
                new_board[place_numb] = 1
            if game.player == 2:
                new_board[place_numb] = -1
            else :
                print("Not valid Player")

            game.player = 1 if game.player == 2 else 2
            print(new_board)
            
            game.check_win(new_board)
            
            
        else:
            print("Invalid move! Please enter a number between 1 and 9.")
            
    print(f"Player {game.winner} wins!")
    
    
if __name__ == "__main__":
    main()