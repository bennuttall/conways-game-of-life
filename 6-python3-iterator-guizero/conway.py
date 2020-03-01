from itertools import product
from random import choice
from time import sleep
from guizero import App, CheckBox


class GameOfLife:
    def __init__(self, width, height):
        self.app = App(title="Conway's GUI of life", width=500, height=500, layout="grid")
        self.app.repeat(100, self.evolve_world)
        self.size = (width, height)
        self.random_world()
        self.create_checkboxes()

    def create_checkboxes(self):
        width, height = self.size
        self.checkboxes = [
            [CheckBox(self.app, grid=[x, y]) for x in range(width)]
            for y in range(height)
        ]

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

    def draw_cell(self, x, y):
        cell = (x, y)
        return 'O' if cell in self.live_cells else ' '

    def show(self):
        self.app.display()


def main():
    game = GameOfLife(10, 10)
    game.show()

if __name__ == '__main__':
    main()
