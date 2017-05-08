"""The Chess module implements the gameplay for a game of chess"""

#Authors: Trisha Justiniano and Beatrice Haro
#Email: trisha.justiniano@gmail.com, beatricelunaharo@gmail.com

#Chess Game
#Create Board
class Board:
    """Creates an 8x8 board of Positions signified as a list Positions.
    The columns are letters and the rows are numbers.

    position_list -- a List of Lists of Positions. The first list refers to the column
    and the internal lists refer to the row.
    """
    self.position_list = [[] for i in range(8)]
    def __init__(self):
        for num_letter in range(8):
            letter = chr(97+num_letter)
            for number in range(1,9):
                new_position = Position(letter, number)
                self.position_list[num_letter].append(new_position)
class Position:
    """A position is a place on the Board is named after a letter and number and
    can hold one piece.

    letter -- a Character. the column of the position
    number -- the row of the position
    piece -- the piece that is on that position
    filled -- whether there is a piece on that position"""
    def __init__(self, letter, number):
        self.letter = letter
        self.number = number
        self.piece = None
        self.filled = false

    def get_column(self):
        return self.letter

    def get_row(self):
        return self.number
    

#Create Pieces
class Piece:
    """A Piece is any object that can move around the board and hold a Position"""
    player_pieces = []
    def __init__(self, name, position, board, player):
        """Create a piece with a Position

        name -- a String. The name of the piece in piece kind and number
        position -- a Position. Where on the board the Piece is.
        poss_moves -- a list. Positions that the piece can move to"
        player = an Integer. The number indicating player0 or player1"""
        self.name = name
        self.position = position
        self.poss_moves = []
        self.player = player
        player_pieces += self.name
        position.piece = self
        position.filled = true
        column_name = position.get_column
        column_num = ord(column_name)-97
        self.curr_column = board.position_list[column_num]
        row_num = position.get_num
        self.curr_row = []
        for columns in range(8):
            self.curr_row.append(board.position_list[columns][row_num])

    def remove_piece(self, Piece):
        player_pieces -= Piece

    def set_poss_moves(self):
        self.poss_moves = []

    def move_piece(self, name, position):
        if position in self.poss_moves:
            if position.filled:
                remove(position.piece)
            self.position = position
            position.piece = self
            self.set_poss_moves
            
        else:
            print "Invalid move"

class Pawn(Piece):
    """A Pawn is a Piece that can overtake other pieces diagonally by one space
    or move forward one space, unless it is the first move by that pawn, in which
    case it may move forward two spaces."""
    def __init__(self, name, position, board, player):
        super(Pawn, self).__init__()
        self.move_count = 0

    def set_poss_moves(self):
        curr_column = self.curr_column
        curr_row = self.curr_row
        if move_count == 0:
            self.poss_moves.append(Position(curr_column, curr_row+2))
        if curr_row < 7:
            self.poss_moves.append(Position(curr_column, curr_row+1))
            if curr_column > 0 and board.position_list[column_num-1][curr_row+1].filled:
                #overtake left
                self.poss_moves.append(Position(curr_column-1, curr_row+1))
            if curr_column < 7 and board.position_list[column_num+1][curr_row+1].filled:
                self.poss_moves.append(Position(curr_column+1, curr_row+1))

    def move_piece(self, self.name, self.position):
        """Increments the move_count for a pawn"""
        if position in self.poss_moves:
            self.position = position
            position.piece = self
        else:
            print "Invalid move"
        self.move_count += 1
        

class Rook(Piece):
    """A Rook is a Piece that can move anywhere within its column or row. It can
    overtake pieces that are within its possible moves."""
    def __init__(self, name, position, board, player):
        super(Rook, self).__init__()
    def set_poss_moves(self):
        curr_column = self.curr_column
        curr_row = self.curr_row
        for i in range(8):
            self.poss_moves.append(Position(i, curr_row)
        for i in range(8):
            self.poss_moves.append(Position(curr_column, i))
        

class Bishop(Piece):
    """A Bishop is a Piece that can move diagonally e.g. 1 column and 1 row away,
    2 columns and 2 rows away, etc. It can overtake pieces that are within its
    movement range."""
    def __init__(self, name, position, board, player)::
        super(Bishop, self)__init__()

    def set_poss_moves(self):
        curr_column = self.curr_column
        curr_row = self.curr_row
        if curr_column < 7:
            for i in range(9-curr_column):
                self.poss_moves.append(Position(curr_column+i, curr_row+i))
                self.poss_moves.append(Position(curr_column+i, curr_row-i))
        if curr_column > 0:
            for i in range(1,8)::
                self.poss_moves.append(Position(curr_column-i, curr_row+i))
                self.poss_moves.append(Position(curr_column-i, curr_row-i))
class Knight(Piece):
    """A Knight is a Piece that can move in 'L' shapes. It overtakes pieces that are 
    within its movement range."""
    def __init__(self, name, position, board, player):
        super(Knight, self)__init__()

    def set_poss_moves(self):
        curr_column = self.curr_column
        curr_row = self.curr_row
         
class Queen(Piece):
    """A queen can move anywhere diagonally, in its column, or in its row. It overtakes
    pieces that are within its movement range."""
    def __init__(self, name, position, board, player):
        super(Queen, self)__init__()
    def set_poss_moves(self):
        
class King(Piece):
    """A King is a Piece that can move one Position in any direction. If the King is
    in a position to be overtaken, that player's King is in "Check". If there are no
    moves a player can make to save the King, the game ends."""
    def __init__(self, name, position, board, player):
        super(Kingt, self)__init__()

    def set_poss_moves(self):
        
#End game scenarios

