from random import randint
from time import sleep


class Life:
    def __init__(self, size=None, start=None, char='O'):
        self.size = size if size else (10, 10)
        self.live_cells = start if start else self.random()
        self.char = char

    def __str__(self):
        char = self.char
        rows, cols = self.size
        grid = ""
        for r in range(rows):
            row = ""
            for c in range(cols):
                cell = (r, c)
                cell_alive = cell in self.live_cells
                cell_char = self.char + ' ' if cell_alive else '  '
                row += cell_char
            row += "\n"
            grid += row
        return grid

    def random(self):
        live_cells = set()
        rows, cols = self.size
        for row in range(rows):
            for col in range(cols):
                if randint(0, 1) == 1:
                    cell = (row, col)
                    live_cells.add(cell)
        return live_cells

    def count_neighbours(self, cell):
        r, c = cell
        neighbours = [(r - 1, c - 1), (r - 1, c + 0), (r - 1, c + 1),
                      (r + 0, c - 1),                 (r + 0, c + 1),
                      (r + 1, c - 1), (r + 1, c + 0), (r + 1, c + 1)]
        return sum(neighbour in self.live_cells for neighbour in neighbours)

    def evolve_cell(self, cell):
        alive = cell in self.live_cells
        neighbours = self.count_neighbours(cell)
        return neighbours == 3 or (alive and neighbours == 2)

    def evolve(self):
        rows, cols = self.size
        new_live_cells = set()
        for row in range(rows):
            for col in range(cols):
                cell = (row, col)
                if self.evolve_cell(cell):
                    new_live_cells.add(cell)
        self.live_cells = new_live_cells


def main():
    size = (60, 60)
    life = Life(size)
    print life
    while True:
        life.evolve()
        print life
        sleep(0.2)

if __name__ == '__main__':
    main()
