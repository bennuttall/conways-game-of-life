from conway import *
import unittest


class Test(unittest.TestCase):
    def test_count_neighbours_of_cell_in_empty_grid(self):
        alive_cells = set()
        size = (1, 1)
        game = Game(size, alive_cells)
        cell = (0, 0)
        neighbours = game.count_neighbours(cell)
        self.assertEqual(neighbours, 0)

    def test_count_neighbours_of_middle_cell_in_3x3_grid(self):
        alive_cells = set([(0, 1), (1, 0), (1, 2), (2, 1)])
        '''
            0 1 0
            1 0 1
            0 1 0
        '''
        size = (3, 3)
        game = Game(size, alive_cells)
        cell = (1, 1)
        neighbours = game.count_neighbours(cell)
        self.assertEqual(neighbours, 4)

    def test_count_neighbours_of_top_corner_cell_in_3x3_grid(self):
        alive_cells = set([(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 1)])
        '''
            1 1 1
            1 0 1
            0 1 0
        '''
        size = (1, 1)
        game = Game(size, alive_cells)
        cell = (0, 0)
        neighbours = game.count_neighbours(cell)
        self.assertEqual(neighbours, 2)

    def test_evolve_3x3_grid(self):
        alive_cells = [(0, 1), (0, 2), (1, 0), (2, 1)]
        '''
            0 1 1           0 1 0
            1 0 0    ==>    1 0 1
            0 1 0           0 0 0
        '''
        size = (3, 3)
        game = Game(size, alive_cells)
        evolved = game.evolve()
        expected = set([(0, 1), (1, 0), (1, 2)])
        self.assertEqual(evolved, expected)


if __name__ == '__main__':
    unittest.main()
