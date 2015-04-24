import unittest
from ttt import Tictactoe

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = Tictactoe()

    def test_new_board_has_empties(self):
        """The space is already taken."""
        self.assertTrue(self.game.board.hasEmpties())

    def test_new_board_fully_empty(self):
        """The space is already taken."""
        print len(self.game.board.empties())
        self.assertTrue(len(self.game.board.empties()) == 9)

if __name__ == '__main__':
    unittest.main()
