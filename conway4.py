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


def evolve(cell_alive, num_neighbours):
    if cell_alive:
        return num_neighbours > 1 if num_neighbours < 4 else False
    return num_neighbours == 3

if __name__ == '__main__':
    unittest.main()
