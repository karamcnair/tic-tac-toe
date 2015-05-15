import board
import player

class Tictactoe(object):

    # Main
    board = board.Board()

    # set up players (any humans?)
    player1 = player.Player("X", "O", True)
    player2 = player.Player("O", "X")

    # show the initial board
    board.display()

    currentPlayer = player1
    winner = None

if __name__ == '__main__':

    while board.hasEmpties() and winner is None:
        print "======= + Player " + currentPlayer.my_token + " is a ",
        if currentPlayer.human:
            print "human" 
        else:
            print "computer"
            print "======="

        playIndex = currentPlayer.play(board)
        board.display()

        if board.won(playIndex):
            winner = currentPlayer
            print "Congrats to Player " + currentPlayer.my_token + "!" 
        elif board.hasEmpties() == False:
            print "Congrats to the cat. Meow! " 
        else:
            currentPlayer = player2 if currentPlayer == player1 else player1


