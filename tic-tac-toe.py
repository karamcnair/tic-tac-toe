
class Board(object):
    """ It's easier to deal with list operations on a 1D
    So instead I'll 'mock' the indexes for the columns & rows.
    """
    squares = [' ',' ',' ', ' ',' ',' ', ' ',' ',' ']
    i = 0

    # some helper variables for identifying each possible winning trio.
    row = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    col = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
    downDiag = [0, 4, 8]
    upDiag = [6, 4, 2]

    def __init__(self):
        self.i = 0

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
        print 'empties = ' + `indexes`
        #todo - use in computer thing

    def hasEmpties(self):
        if ' ' in self.squares:
            return True
        else:
            return False

    def wins(self, win_trio):
        win_squares = [self.squares[x] for x in win_trio]
        print "win_squares = "  + `win_squares`
        return all (x == win_squares[0] for x in win_squares)

    # todo - check for wins
    def won(self, play_index):
        play_row = play_index / 3
        play_col = play_index % 3
        print "row " + `play_row` + ", col " + `play_col`
        winner = False

        if self.wins(self.row[play_row]) or self.wins(self.col[play_col]):
            return True
        elif play_index in self.upDiag:
            return self.wins(self.upDiag)
            # todo needs to be or= not just overwrite
        if play_index in self.downDiag:
            winner = self.wins(self.downDiag)
        return winner



class Player(object):
    token = ''
    human = False
    def __init__(self, token, human=False):
        self.token = token
        self.human = human

    # how do I want to deal with 'win'. I want it to be 
    def play(self, board):

        if self.human:
            # get input from keyboard to play
            play_index = 0
        else:
            empties = board.empties()
            # use algorithm to play (remember you need to flip 
            # regarding tokens so can check 'wins' for other player)
            play_index = board.i
            board.i += 1

        board.squares[play_index] = self.token
        print 'player.token = ' + self.token
        return play_index

# Main
board = Board()

# set up players (any humans?)
player1 = Player("X")
player2 = Player("O")

# show the initial board
board.display()

currentPlayer = player1
winner = None

while board.hasEmpties() and winner is None:
  print "======="
  print "======="

  play = currentPlayer.play(board)
  board.display()

  if board.won(play):
    winner = currentPlayer
    print "Congrats to Player " + currentPlayer.token + "!" 
  elif board.hasEmpties() == False:
    print "Congrats to the cat. Meow! " 
  else:
    currentPlayer = player2 if currentPlayer == player1 else player1


