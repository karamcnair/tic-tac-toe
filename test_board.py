import unittest
from board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.emptyBoard = Board()

        ## this is bs - why is it only able to use a single board?
	
    def test_new_board_has_empties(self):
        self.assertTrue(self.emptyBoard.hasEmpties())

    def test_new_board_fully_empty(self):
        self.board = Board()
        print "number of empties = " + `len(self.emptyBoard.empties())`
        self.assertTrue(len(self.emptyBoard.empties()) == 9)

    def test_three_in_a_row_wins(self):
        self.assertTrue(self.board.win(['X', 'X', 'X']))

    def test_unmatched_three_in_a_row_doesnt_win(self):
        self.assertFalse(self.board.win(['X', 'O', 'X']))

    def test_incomplete_three_doesnt_win(self):
        self.assertFalse(self.board.win([' ', 'O', 'X'])) 

    def test_indexes_win_game(self):
        for i in self.board.row[0]:
            self.board.squares[i] = 'k'
        self.assertTrue(self.board.trio_wins(self.board.squares, self.board.row[0]))




if __name__ == '__main__':
    unittest.main()
