from itertools import product
from random import choice
from time import sleep
from guizero import App, CheckBox


class GameOfLife:
    def __init__(self, width, height):
        self.app = App(title="Conway's GUI of Life", width=1100, height=950, layout="grid")
        self.app.repeat(500, self.evolve_world)
        self.size = (width, height)
        self.random_world()
        self.create_checkboxes()

    def __call__(self):
        self.app.display()

    def get_checkbox(self, x, y):
        def update():
            cell = (x, y)
            if cell in self.live_cells:
                self.live_cells.remove(cell)
            else:
                self.live_cells.add(cell)

        cb = CheckBox(self.app, grid=[x, y], text='', command=update)
        return cb

    def create_checkboxes(self):
        width, height = self.size
        self.checkboxes = [
            [self.get_checkbox(x, y) for x in range(width)]
            for y in range(height)
        ]
        for x in range(width):
            for y in range(height):
                self.checkboxes[y][x].value = (x, y) in self.live_cells

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
        for x in range(width):
            for y in range(height):
                self.checkboxes[y][x].value = 1 if (x, y) in self.live_cells else 0

    def random_world(self):
        width, height = self.size
        world = product(range(width), range(height))
        self.live_cells = {cell for cell in world if choice([0, 1])}

main = GameOfLife(30, 30)

if __name__ == '__main__':
    main()
