
class Board(object):
    """ It's easier to deal with list operations on a 1D
    So instead I'll 'mock' the indexes for the columns & rows.
    """

    # some helper variables for identifying each possible winning trio.
    row = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    col = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
    downDiag = [0, 4, 8]
    upDiag = [6, 4, 2]

    def __init__(self):
        self.isWon = False
        self.squares = [' ',' ',' ', ' ',' ',' ', ' ',' ',' ']
    

    def display(self):
        for i in self.row[0]:
            print self.squares[i] + '|',
        print ""
        for i in self.row[1]:
            print self.squares[i] + '|',
        print ""
        for i in self.row[2]:
            print self.squares[i] + '|', 
        print ""

    def empties(self):
        indexes = [i for i, x in enumerate(self.squares) if x == ' ']
        return indexes
        #todo - use in computer play selection

    def hasEmpties(self):
        if ' ' in self.squares:
            return True
        else:
            return False

    # if all the values in this 'row' are the same, it's a win
    # (this is safe b/c this is only called on trios the most recent play 
    # was made in - no risk of ' ' ' ' ' ', but just in case...

    # need to be able to take an array of 3 values & make sure they're a winning 'row'
    def win(self, trio_values):
        if ' ' in trio_values:
            return False
        return all (x == trio_values[0] for x in trio_values)


    # this function checks a specific trio on a specific board (squares) for a win 
    def trio_wins(self, squares, trio_indexes):
        trio_values = [squares[x] for x in trio_indexes]
        return self.win(trio_values)

    # this function checks if ANY wins arise from playing 'play_index' being played
    # on the current board. We need it anyway because we need to test the human entries
    def wins_game(self, squares, play_index):
        play_row = play_index / 3
        play_col = play_index % 3

        # probably GET the rows here instead so 

        if self.trio_wins(squares, Board.row[play_row]):
            return True
        elif self.trio_wins(squares, Board.col[play_col]):
            return True
        elif play_index in Board.upDiag:
            if self.trio_wins(squares, Board.upDiag):
                return True
            elif play_index in Board.downDiag:
                return self.trio_wins(squares, Board.downDiag)
        return False

    def won(self, play_index):
        return self.wins_game(self.squares, play_index)