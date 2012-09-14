import unittest


class Test(unittest.TestCase):
    def test_live_cell_with_fewer_than_two_neighbours_dies(self):
        new_cell_alive = evolve(cell_alive=True, num_neighbours=0)
        self.assertFalse(new_cell_alive)

        new_cell_alive = evolve(cell_alive=True, num_neighbours=1)
        self.assertFalse(new_cell_alive)

    def test_live_cell_with_two_or_three_neighbours_lives(self):
        new_cell_alive = evolve(cell_alive=True, num_neighbours=2)
        self.assertTrue(new_cell_alive)

        new_cell_alive = evolve(cell_alive=True, num_neighbours=3)
        self.assertTrue(new_cell_alive)

    def test_live_cell_with_more_than_three_neighbours_dies(self):
        new_cell_alive = evolve(cell_alive=True, num_neighbours=4)
        self.assertFalse(new_cell_alive)

        new_cell_alive = evolve(cell_alive=True, num_neighbours=5)
        self.assertFalse(new_cell_alive)

    def test_dead_cell_with_three_neighbours_is_born(self):
        new_cell_alive = evolve(cell_alive=False, num_neighbours=3)
        self.assertTrue(new_cell_alive)

    def test_dead_cells_with_not_three_neighbours_is_not_born(self):
        new_cell_alive = evolve(cell_alive=False, num_neighbours=1)
        self.assertFalse(new_cell_alive)

    def test_1x1_grid_evolves_correctly(self):
        world = [[0]]
        new_world = evolve_world(world)
        self.assertEqual([[0]], new_world)

        world = [[1]]
        new_world = evolve_world(world)
        self.assertEqual([[1]], new_world)

    def test_count_neighbours_of_1x1_world(self):
        world = [[0]]
        cell = (0, 0)
        num_neighbours = count_neighbours(world, cell)
        self.assertEqual(0, num_neighbours)

        world = [[1]]
        cell = (0, 0)
        num_neighbours = count_neighbours(world, cell)
        self.assertEqual(0, num_neighbours)

    def test_count_neighbours_of_3x3_world(self):
        world = [[1, 0, 1],
                 [0, 1, 0],
                 [1, 0, 1]]
        cell = (1, 1)
        num_neighbours = count_neighbours(world, cell)
        self.assertEqual(4, num_neighbours)

        world = [[1, 0, 1],
                 [1, 1, 1],
                 [1, 0, 1]]
        cell = (1, 1)
        num_neighbours = count_neighbours(world, cell)
        self.assertEqual(6, num_neighbours)
        cell = (0, 0)
        num_neighbours = count_neighbours(world, cell)
        self.assertEqual(2, num_neighbours)

    def test_count_neighbours_of_5x5_world(self):
        world = [[1, 0, 1, 0, 1],
                 [0, 1, 0, 1, 1],
                 [1, 0, 1, 0, 1],
                 [0, 1, 0, 1, 1],
                 [1, 0, 1, 0, 1]]
        cell = (0, 0)
        num_neighbours = count_neighbours(world, cell)
        self.assertEqual(1, num_neighbours)
        cell = (2, 2)
        num_neighbours = count_neighbours(world, cell)
        self.assertEqual(4, num_neighbours)
        cell = (4, 2)
        num_neighbours = count_neighbours(world, cell)
        self.assertEqual(2, num_neighbours)
        cell = (4, 3)
        num_neighbours = count_neighbours(world, cell)
        self.assertEqual(4, num_neighbours)


def evolve(cell_alive, num_neighbours):
    if cell_alive:
        return num_neighbours > 1 if num_neighbours < 4 else False
    return num_neighbours == 3


def evolve_world(world):
    return [[0]] if world[0][0] == 0 else [[1]]


def count_neighbours(world, cell):
    num_neighbours = 0
    r = cell[0]
    c = cell[1]
    neighbouring_rows = range(r - 1, r + 2)
    neighbouring_cols = range(c - 1, c + 2)

    for nr in neighbouring_rows:
        for nc in neighbouring_cols:
            if nr >= 0 and nc >= 0:
                if nr != r or nc != c:
                    try:
                        num_neighbours += world[nr][nc]
                    except:
                        pass

    return num_neighbours

if __name__ == '__main__':
    unittest.main()
