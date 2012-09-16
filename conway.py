import unittest


class Test(unittest.TestCase):
    def test_live_cell_with_fewer_than_two_neighbours_dies(self):
        new_cell_alive = evolve_cell(cell_alive=True, num_neighbours=0)
        self.assertFalse(new_cell_alive)

        new_cell_alive = evolve_cell(cell_alive=True, num_neighbours=1)
        self.assertFalse(new_cell_alive)

    def test_live_cell_with_two_or_three_neighbours_lives(self):
        new_cell_alive = evolve_cell(cell_alive=True, num_neighbours=2)
        self.assertTrue(new_cell_alive)

        new_cell_alive = evolve_cell(cell_alive=True, num_neighbours=3)
        self.assertTrue(new_cell_alive)

    def test_live_cell_with_more_than_three_neighbours_dies(self):
        new_cell_alive = evolve_cell(cell_alive=True, num_neighbours=4)
        self.assertFalse(new_cell_alive)

        new_cell_alive = evolve_cell(cell_alive=True, num_neighbours=5)
        self.assertFalse(new_cell_alive)

    def test_dead_cell_with_three_neighbours_is_born(self):
        new_cell_alive = evolve_cell(cell_alive=False, num_neighbours=3)
        self.assertTrue(new_cell_alive)

    def test_dead_cells_with_not_three_neighbours_is_not_born(self):
        new_cell_alive = evolve_cell(cell_alive=False, num_neighbours=1)
        self.assertFalse(new_cell_alive)

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
        cell = (0, 1)
        num_neighbours = count_neighbours(world, cell)
        self.assertEqual(3, num_neighbours)
        cell = (1, 1)
        num_neighbours = count_neighbours(world, cell)
        self.assertEqual(4, num_neighbours)
        cell = (2, 2)
        num_neighbours = count_neighbours(world, cell)
        self.assertEqual(1, num_neighbours)

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
                 [0, 1, 1, 1, 1],
                 [1, 0, 0, 0, 1]]
        cell = (0, 0)
        num_neighbours = count_neighbours(world, cell)
        self.assertEqual(1, num_neighbours)
        cell = (2, 2)
        num_neighbours = count_neighbours(world, cell)
        self.assertEqual(5, num_neighbours)
        cell = (4, 3)
        num_neighbours = count_neighbours(world, cell)
        self.assertEqual(4, num_neighbours)

    def test_1x1_world_evolves_correctly(self):
        world = [[0]]
        new_world = evolve_world(world)
        self.assertEqual([[0]], new_world)

        world2 = [[1]]
        new_world2 = evolve_world(world2)
        self.assertEqual([[0]], new_world2)

    def test_3x3_world_evolves_correctly(self):
        world = [[1, 0, 1],
                 [0, 1, 0],
                 [1, 0, 1]]

        new_world = evolve_world(world)
        expected = [[0, 1, 0],
                    [1, 0, 1],
                    [0, 1, 0]]
        self.assertEqual(expected, new_world)

        new_world2 = evolve_world(new_world)
        expected2 = [[0, 1, 0],
                     [1, 0, 1],
                     [0, 1, 0]]
        self.assertEqual(expected2, new_world2)

    def test_5x5_world_evolves_correctly(self):
        world = [[1, 0, 1, 0, 1],
                 [0, 1, 0, 1, 1],
                 [1, 0, 1, 0, 1],
                 [0, 1, 1, 1, 1],
                 [1, 0, 0, 0, 1]]

        new_world = evolve_world(world)
        expected = [[0, 1, 1, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0],
                    [1, 0, 1, 0, 1],
                    [0, 1, 1, 0, 1]]
        self.assertEqual(expected, new_world)

        new_world2 = evolve_world(new_world)
        expected2 = [[0, 1, 0, 1, 0],
                     [1, 0, 0, 1, 0],
                     [1, 0, 0, 1, 0],
                     [1, 0, 1, 0, 0],
                     [0, 1, 1, 0, 0]]
        self.assertEqual(expected2, new_world2)
        

def evolve_cell(cell_alive, num_neighbours):
    if cell_alive:
        return num_neighbours > 1 if num_neighbours < 4 else False
    return num_neighbours == 3


def evolve_world(world):
    rows = len(world)
    cols = len(world[0])

    new_world = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(0)
        new_world.append(new_row)

    for r in range(rows):
        for c in range(cols):
            cell = (r, c)
            cell_alive = world[r][c]
            num_neighbours = count_neighbours(world, cell)
            new_cell = 1 if evolve_cell(cell_alive, num_neighbours) else 0
            new_world[r][c] = new_cell

    return new_world


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
