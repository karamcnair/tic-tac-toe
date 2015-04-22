    def computer_play(self, board):
        # where CAN I play
        empties = board.empties()
        oppo_wins = []
        my_partials = []


        # this feels like it would be simplest (at this point) to clone the board & test each empty for me & my opp


        
        # for each of them, can I win? 
        for play_index in empties:
            play_row = play_index / 3
            play_col = play_index % 3
            print "cmpt row " + `play_row` + ", cmpt col " + `play_col`

            #get the rows associated with that play_index 
            trios = [Board.row[play_row], Board.col[play_col]]

            if play_index in Board.upDiag:
            	trios.append(Board.upDiag)
            if play_index in Board.downDiag:
            	trios.append(Board.downDiag)

            # for each trio, perform the tests # we can improve this later
            for trio in trios:
            	get_trio()






