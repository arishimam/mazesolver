import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)  

        self.assertEqual(len(m1.cells), num_rows)
        self.assertEqual(len(m1.cells[0]), num_cols)

    def test_maze_break_entrance_exit(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)  

        self.assertEqual(m1.cells[0][0].has_top_wall, False)
        self.assertEqual(m1.cells[len(m1.cells)-1][len(m1.cells[0])-1].has_bottom_wall, False)




if __name__ == "__main__":
    unittest.main()
