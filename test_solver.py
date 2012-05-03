import unittest
import solver

class TestSolver(unittest.TestCase):

    def setUp(self):
        pass

    def test_acepts_board_nine_by_nine(self):
        board = [ [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        s = solver.Solver()
        s.solve(board)

if __name__ == '__main__':
    unittest.main()
