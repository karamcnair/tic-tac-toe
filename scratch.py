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


