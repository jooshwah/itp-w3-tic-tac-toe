from .exceptions import InvalidMovementException

class Game(object):

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        
        self.next_player = self.player_1

    def is_finished(self):
        return self.has_winner() or self.is_tied()
    
    def has_winner(self):
        if self.get_winner() is not None:
            return True
        return False
       
    def is_tied(self):
        for i in range(3):
            row = self.board.get_row(i)
            self.board.initial_board
            for elem in row:
                if elem is None:
                    return False
        return True

    def get_winner(self):
        for i in range(3):
            row = self.board.get_row(i) #[x,x,x]
            col = self.board.get_column(i) 
            if row.count('X') == 3:
                return 'X'
            elif row.count('0') == 3:
                return 'O'
            elif col.count('X') == 3:
                return 'X'
            elif col.count('0') == 3:
                return 'O'
            
        for i in range(2):        
            diag = self.board.get_diagonal(i)
            if diag.count('X') == 3:
                return 'X'
            elif diag.count('O') == 3: 
                return 'O'
        return None            

    def next_turn(self):
        return self.next_player

    def move(self, player, row, col):
        movement_is_invalid = (
            row not in range(3) or 
            col not in range(3) or 
            player != self.next_player or 
            self.is_finished()is True
        )
        if movement_is_invalid:
            raise InvalidMovementException()
        else:
            for i in range(3):
                for j in range(3):
                    if i == row and j == col:
                        if self.board.get_row(i)[j] == 'X' or self.board.get_row(i)[j] == 'O':
                            raise InvalidMovementException()
    
                        else:
                            self.board.move(player, row, col)
                            self.next_player = 'X' if player == 'O' else 'O'
                                

                                
                        
                            
BOARD_TEMPLATE = """
     |     |
  {}  |  {}  |  {}
_____|_____|_____
     |     |
  {}  |  {}  |  {}
_____|_____|_____
     |     |
  {}  |  {}  |  {}
     |     |
"""


class Board(object):
    def __init__(self, initial_board=None):
        if initial_board != None:
            self.initial_board = initial_board
        else:
           self.initial_board = [
               [None, None, None],
               [None, None, None],
               [None, None, None]
           ]

    def move(self, figure, row, col):
        self.initial_board[row][col] = figure
        
    def __str__(self):
        return BOARD_TEMPLATE.format(
            self.initial_board[0][0] or '-',
            self.initial_board[0][1] or '-',
            self.initial_board[0][2] or '-',
            
            self.initial_board[1][0] or '-',
            self.initial_board[1][1] or '-',
            self.initial_board[1][2] or '-',
            
            self.initial_board[2][0] or '-',
            self.initial_board[2][1] or '-',
            self.initial_board[2][2] or '-')

    def get_row(self, row_number):
        return self.initial_board[row_number]

    def get_column(self, col_number):
        col_list = []
        
        if col_number == 0:
            col_list.append(self.initial_board[0][0])
            col_list.append(self.initial_board[1][0])
            col_list.append(self.initial_board[2][0])
        elif col_number == 1:
            col_list.append(self.initial_board[0][1])
            col_list.append(self.initial_board[1][1])
            col_list.append(self.initial_board[2][1])
        elif col_number == 2:
            col_list.append(self.initial_board[0][2])
            col_list.append(self.initial_board[1][2])
            col_list.append(self.initial_board[2][2])
            
        return col_list

    def get_diagonal(self, row_number):
        col_list = []
        
        if row_number == 0:
            col_list.append(self.initial_board[0][0])
            col_list.append(self.initial_board[1][1])
            col_list.append(self.initial_board[2][2])
        elif row_number == 1:
            col_list.append(self.initial_board[0][2])
            col_list.append(self.initial_board[1][1])
            col_list.append(self.initial_board[2][0])
        
        return col_list