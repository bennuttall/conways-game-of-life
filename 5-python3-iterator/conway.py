#!/usr/bin/python3

from random import choice
from itertools import product
from time import sleep


class GameOfLife(object):
    def __init__(self, height, width):
        self.size = (height, width)
        self.random_world()

    def __str__(self):
        width, height = self.size
        return '\n'.join(
            ' '.join(
                self.draw_cell(x, y)
                for x in range(width)
            )
            for y in range(height)
        )

    def __iter__(self):
        return self

    def __next__(self):
        self.evolve_world()
        return self

    def evolve_cell(self, cell):
        alive = cell in self.live_cells
        neighbours = self.count_neighbours(cell)
        return neighbours == 3 or (alive and neighbours == 2)

    def count_neighbours(self, cell):
        x, y = cell
        neighbours = [(x - 1, y - 1), (x + 0, y - 1), (x + 1, y - 1),
                      (x - 1, y + 0),                 (x + 1, y + 0),
                      (x - 1, y + 1), (x + 0, y + 1), (x + 1, y + 1)]
        return sum(neighbour in self.live_cells for neighbour in neighbours)

    def evolve_world(self):
        width, height = self.size
        grid = product(range(width), range(height))
        self.live_cells = {cell for cell in grid if self.evolve_cell(cell)}

    def random_world(self):
        width, height = self.size
        grid = product(range(width), range(height))
        self.live_cells = {cell for cell in grid if choice((0, 1))}

    def draw_cell(self, x, y):
        return 'O' if (x, y) in self.live_cells else ' '


def main():
    game = GameOfLife(60, 40)
    for i in game:
        sleep(0.5)
        print(i)

if __name__ == '__main__':
    main()
