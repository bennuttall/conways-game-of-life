import random as rand
import time
import argparse


def evolve_cell(cell_alive, num_neighbours):
    if cell_alive:
        return num_neighbours > 1 if num_neighbours < 4 else False
    return num_neighbours == 3


def get_empty_world(rows, cols):
    new_world = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(0)
        new_world.append(new_row)
    return new_world


def evolve_world(world):
    rows = len(world)
    cols = len(world[0])

    new_world = get_empty_world(rows, cols)
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

def get_random_world(rows, cols=False):
    cols = cols if cols else rows
    world = []
    for row in range(rows):
        row = []
        for cell in range(cols):
            cell = int(round(rand.random()))
            row.append(cell)
        world.append(row)
    return world

def world_to_string(world):
    string = ''
    for row in world:
        for cell in row:
            string += 'O ' if cell else '  '
        string += "\n"
    return string

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", help="height of the grid", type=int)
    parser.add_argument("--cols", help="width of the grid", type=int)
    args = parser.parse_args()

    rows = args.rows if args.rows else 50
    cols = args.cols if args.cols else rows
    world = get_random_world(rows, cols)
    while True:
        world = evolve_world(world)
        print world_to_string(world)
        time.sleep(0.2)

if __name__ == '__main__':
    main()
