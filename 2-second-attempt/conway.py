from random import *
from time import *


def evolve_cell(alive, neighbours):
    return neighbours == 3 or (alive and neighbours == 2)


def count_neighbours(alive_cells, position):
    r, c = position
    neighbours = [(r - 1, c - 1), (r - 1, c + 0), (r - 1, c + 1),
                  (r + 0, c - 1),                 (r + 0, c + 1),
                  (r + 1, c - 1), (r + 1, c + 0), (r + 1, c + 1)]
    return sum(cell in alive_cells for cell in neighbours)


def evolve(alive_cells, size):
    new_alive_cells = set()
    rows, cols = size
    for r in range(rows):
        for c in range(cols):
            cell = (r, c)
            alive = cell in alive_cells
            neighbours = count_neighbours(alive_cells, cell)
            if evolve_cell(alive, neighbours):
                new_alive_cells.add(cell)
    return new_alive_cells
