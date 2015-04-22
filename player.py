import board

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
            play_index = empties[len(empties)-1]
            print "Human playing "+ self.my_token + " in location " + `play_index`


        else:
            play_index = self.computer_play(board)
            print "Computer playing "+ self.my_token + " in location " + `play_index`

        # this is the part that ties the 'wins' check to having actually played
        # need to figure out/refactor 'wins' with a 'candidate' trio instead.

        board.squares[play_index] = self.my_token
        return play_index

    def computer_play(self, board):

        # where CAN I play?
        empties = board.empties()

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
            if board.wins_game(temp_squares, play_index):
                return play_index
            else:
                temp_squares[play_index] = self.oppo_token
                # keep track of opponent wins to block!
                if board.wins_game(temp_squares, play_index):
                    oppo_wins.append(play_index)
                else:
                    # this is kinda bogus b/c it might be one with an opponent but I don't want to drill into that yet
                    my_partials.append(play_index)
 
        # if my opponent has ANY win plays, I have to block. (If more than one, I lose anyway)
        if len(oppo_wins) > 0:
            return oppo_wins[0]
        if len(my_partials) > 0:
            return my_partials[0]
        return empties[0]           
