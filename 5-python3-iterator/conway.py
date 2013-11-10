#!/usr/bin/python3

from itertools import product
from random import choice
from time import sleep


class GameOfLife(object):
    def __init__(self, width, height):
        self.size = (width, height)
        self.random_world()

    def __str__(self):
        width, height = self.size
        return '\n'.join(
            ' '.join(
                self.draw_cell(x, y) for x in range(width)
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
        deltas = set(product([-1, 0, 1], repeat=2)) - set([(0, 0)])
        neighbours = ((x + dx, y + dy) for (dx, dy) in deltas)
        return sum(neighbour in self.live_cells for neighbour in neighbours)

    def evolve_world(self):
        width, height = self.size
        world = product(range(width), range(height))
        self.live_cells = {cell for cell in world if self.evolve_cell(cell)}

    def random_world(self):
        width, height = self.size
        world = product(range(width), range(height))
        self.live_cells = {cell for cell in world if choice([0, 1])}

    def draw_cell(self, x, y):
        cell = (x, y)
        return 'O' if cell in self.live_cells else ' '


def main():
    game = GameOfLife(60, 40)
    for i in game:
        print(i)
        sleep(0.1)

if __name__ == '__main__':
    main()
