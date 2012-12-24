from conway import *
import unittest


class Test(unittest.TestCase):
    def test_live_cell_with_no_neighbours_dies(self):
        cell_alive = evolve_cell(alive=True, neighbours=0)
        self.assertFalse(cell_alive)

    def test_live_cell_with_two_neighbours_lives_on(self):
        cell_alive = evolve_cell(alive=True, neighbours=2)
        self.assertTrue(cell_alive)

    def test_live_cell_with_three_neighbours_lives_on(self):
        cell_alive = evolve_cell(alive=True, neighbours=3)
        self.assertTrue(cell_alive)

    def test_live_cell_with_four_neighbours_dies(self):
        cell_alive = evolve_cell(alive=True, neighbours=4)
        self.assertFalse(cell_alive)

    def test_dead_cell_with_three_neighbours_is_born(self):
        cell_alive = evolve_cell(alive=False, neighbours=3)
        self.assertTrue(cell_alive)

    def test_dead_cell_with_two_neighbours_stays_dead(self):
        cell_alive = evolve_cell(alive=False, neighbours=2)
        self.assertFalse(cell_alive)

    def test_dead_cell_with_four_neighbours_stays_dead(self):
        cell_alive = evolve_cell(alive=False, neighbours=4)
        self.assertFalse(cell_alive)

    def test_count_neighbours_of_cell_in_empty_grid(self):
        alive_cells = set()
        position = (0, 0)
        neighbours = count_neighbours(alive_cells, position)
        self.assertEqual(neighbours, 0)

    def test_count_neighbours_of_middle_cell_in_3x3_grid(self):
        alive_cells = set([(0, 1), (1, 0), (1, 2), (2, 1)])
        '''
            0 1 0
            1 0 1
            0 1 0
        '''
        position = (1, 1)
        neighbours = count_neighbours(alive_cells, position)
        self.assertEqual(neighbours, 4)

    def test_count_neighbours_of_top_corner_cell_in_3x3_grid(self):
        alive_cells = set([(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 1)])
        '''
            1 1 1
            1 0 1
            0 1 0
        '''
        position = (0, 0)
        neighbours = count_neighbours(alive_cells, position)
        self.assertEqual(neighbours, 2)

    def test_evolve_3x3_grid(self):
        alive_cells = set([(0, 1), (0, 2), (1, 0), (2, 1)])
        '''
            0 1 1           0 1 0
            1 0 0    ==>    1 0 1
            0 1 0           0 0 0
        '''
        size = (3, 3)
        evolved = evolve(alive_cells, size)
        expected = set([(0, 1), (1, 0), (1, 2)])
        self.assertEqual(evolved, expected)


if __name__ == '__main__':
    unittest.main()
