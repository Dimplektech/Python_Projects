from player import RandomComputerPlayer, HumanPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # we will use single list to represent 3x3 board
        self.current_winner = None  # keep the track of the Winner

    def print_board(self):
     
        rows = []           
        for i in range(3):
            start_index = i * 3
            end_index = (i + 1)*3
            row = self.board[start_index:end_index] # slice out the row
            rows.append(row) # Add the rows to rows List

        for row in rows:
            print(' | ' + ' | '.join(row) + ' | ') # Print each line in Tic tac formatted as Tic-Toc-Toe line.


    @staticmethod
    def print_board_nums():        
        # 0 | 1 | 2 etc tells us what number corroseponds to what box
        # number_board = [[str(i) for i range(j*3, (j+1*3)] for j in range(3)]
        # for row in number_board:    
        #     print('| ' + '| '.join(row) + ' |')         

        number_board = []  # This will hold the rows of number
        for j in range(3):
            row = []  # This will hold the numbers for the current row
            for i in range(j*3, (j+1) * 3):
                row.append(str(i))  # Convert the number into string and then add  to the row.

            number_board.append(row)  # Add the row to the number_board list.

        for row in number_board:
            print('| ' + '| '.join(row) + ' |')  # Print each row  formatted with the number.

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']    
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     #['x', 'x', 'o'] --> [(0,'x'), (1, 'x'), (2,'o')]
        #     if spot == ' ':
        #         moves.append(i)
        # return moves   

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # if valid move, then make move (assign square to letter)
        # then return true. if Invalid the return False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # Winner if 3 in a row anywhere ... we have to check al of these!!
        # frist check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        # Check to column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagnols
        # but only if the square is even number(0, 2, 4, 6, 8)
        # These only move possible to win a diagonol

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # Left to right Diagonal
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left Diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        ## If all of these failed
        return False    


def play(game, x_player, o_player, print_game=True):
    # return the winner of the game(the letter)! or None for tie
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    # iterate while the game has still empty squares
    # ( we dont have to worry about winner because we'll just retrn that which breaks the loop)
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # lets define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter +f" make a move to square {square}")
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  

            # After we made a move , we need to alternate the letters
            letter = 'O' if letter =='X' else 'X' # switches player

    if print_game:
        print('Its a Tie!!')


if  __name__ == "__main__":
    x_player = HumanPlayer('X')
    o_player =  RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)