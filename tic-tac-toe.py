
class Board(object):
    """ It's easier to deal with list operations on a 1D
    So instead I'll 'mock' the indexes for the columns & rows.
    """
    squares = [' ',' ',' ', ' ',' ',' ', ' ',' ',' ']
    i = 8

    # some helper variables for identifying each possible winning trio.
    row = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    col = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
    downDiag = [0, 4, 8]
    upDiag = [6, 4, 2]

    def __init__(self):
        self.i = 8

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
        print "called win-1 with " + `trio_values`
        if ' ' in trio_values:
            return False
        return all (x == trio_values[0] for x in trio_values)

    # get the board values associated with those 3 indexes 
    def get_trio(self, squares, trio_indexes):
        print "called get_trio-2"
        return [squares[x] for x in trio_indexes]

    # this function checks a specific board (squares) for a win 
    def wins_game(self, squares, trio_indexes):
        print "called wins_game-3"
        trio_values = [squares[x] for x in trio_indexes]
        print "trio values " + `trio_values`
        return self.win(trio_values)

    # this function checks if ANY wins arise from playing 'play_index' being played
    # on the current board. We need it anyway because we need to test the human entries
    def won(self, play_index):
        print "called won-4"
        play_row = play_index / 3
        play_col = play_index % 3
        print "row " + `play_row` + ", col " + `play_col`

        # probably GET the rows here instead so 

        if self.wins_game(self.squares, Board.row[play_row]):
            return True
        elif self.wins_game(self.squares, Board.col[play_col]):
            return True
        elif play_index in Board.upDiag:
            if self.wins_game(self.squares, Board.upDiag):
                return True
            elif play_index in Board.downDiag:
                return self.wins_game(self.squares, Board.downDiag)
        return False


class Player(object):
    my_token = ''
    oppo_token = ''
    human = False
    def __init__(self, my_token, oppo_token, human=False):
        self.my_token = my_token
        self.oppo_token = oppo_token
        self.human = human

    # how do I want to deal with 'win'. I want it to be 
    def play(self, board):

        if self.human:
            # get input from keyboard to play
            empties = board.empties()
            play_index = empties[0]

        else:
            play_index = self.computer_play(board)

        # this is the part that ties the 'wins' check to having actually played
        # need to figure out/refactor 'wins' with a 'candidate' trio instead.

        board.squares[play_index] = self.my_token
        print 'player.token = ' + self.my_token
        return play_index

    def computer_play(self, board):

        print "in computer_play with board " + `board.squares`

        # where CAN I play?
        empties = board.empties()
        print "empties = " + `empties`

        oppo_wins = []
        # this would be to find any possible 'better' spaces b/c I already have one lined up
        my_partials = []

        # should be prevented by preconditions, but...
        if len(empties) == 0:
            return None;

        # this feels like it would be simplest (at this point) to clone the board & test each empty for me & my opp
        for play_index in empties:
            temp_squares = list(board.squares)
            temp_squares[play_index] = self.my_token

            # the first winning position is my choice b/c it ends the game
            if wins_game(squares):
                return play_index
            else:
                temp_squares[play_index] = self.oppo_token
                # keep track of opponent wins to block!
                if wins_game(squares):
                    oppo_wins.append(play_index)
                else:
                    # this is kinda bogus b/c it might be one with an opponent but I don't want to drill into that yet
                    my_partials.append(play_index)
 
        # if my opponent has ANY win plays, I have to block. (If more than one, I lose anyway)
        if len(oppo_wins) > 1:
            return oppo_wins[0]
        if len(my_partials) > 1:
            return my_partials[0]
        return empties[0]           

# Main
board = Board()

# set up players (any humans?)
player1 = Player("X", "O")
player2 = Player("O", "X")

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
    print "Congrats to Player " + currentPlayer.my_token + "!" 
  elif board.hasEmpties() == False:
    print "Congrats to the cat. Meow! " 
  else:
    currentPlayer = player2 if currentPlayer == player1 else player1


