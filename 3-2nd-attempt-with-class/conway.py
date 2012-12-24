from random import randint


class Game:
    def __init__(self, size, alive_cells, cell_char='O'):
        self.size = tuple(size)
        self.alive_cells = set(alive_cells)
        self.cell_char = cell_char

    def __str__(self):
        rows, cols = self.size
        grid = ''
        for r in range(rows):
            for c in range(cols):
                cell = (r, c)
                grid += 'O ' if cell in self.alive_cells else '  '
            grid += "\n"
        return grid

    def evolve_cell(self, cell):
        alive = cell in self.alive_cells
        neighbours = self.count_neighbours(cell)
        return neighbours == 3 or (alive and neighbours == 2)

    def count_neighbours(self, cell):
        r, c = cell
        neighbours = [(r - 1, c - 1), (r - 1, c + 0), (r - 1, c + 1),
                      (r + 0, c - 1),                 (r + 0, c + 1),
                      (r + 1, c - 1), (r + 1, c + 0), (r + 1, c + 1)]
        return sum(cell in self.alive_cells for cell in neighbours)

    def evolve(self):
        new_alive_cells = set()
        rows, cols = self.size
        for r in range(rows):
            for c in range(cols):
                cell = (r, c)
                alive = cell in self.alive_cells
                if self.evolve_cell(cell):
                    new_alive_cells.add(cell)
        self.alive_cells = new_alive_cells
        return new_alive_cells

    @staticmethod
    def random_start(size):
        rows, cols = size
        alive_cells = set()
        for r in range(rows):
            for c in range(cols):
                if randint(0, 1):
                    cell = (r, c)
                    alive_cells.add(cell)
        return alive_cells
