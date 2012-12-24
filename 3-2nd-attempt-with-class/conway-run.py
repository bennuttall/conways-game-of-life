from conway import *
from time import sleep
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument("-r",
            "--rows",
            help="height of the grid",
            type=int,
            default=25)
    parser.add_argument("-c",
            "--cols",
            help="width of the grid",
            type=int,
            default=25)
    parser.add_argument("--char",
            help="character to represent cell",
            default='O')
    args = parser.parse_args()

    rows = args.rows
    cols = args.cols
    cell_char = args.char
    size = (rows, cols)

    glider = [(30, 31), (31, 32), (32, 30), (32, 31), (32, 32)]
    glider_gun = [
        (1, 26),
        (2, 24), (2, 26),
        (3, 14), (3, 15), (3, 22), (3, 23), (3, 36), (3, 37),
        (4, 13), (4, 17), (4, 22), (4, 23), (4, 36), (4, 37),
        (5, 2), (5, 3), (5, 12), (5, 18), (5, 22), (5, 23),
        (6, 2), (6, 3), (6, 12), (6, 16), (6, 18), (6, 19), (6, 24), (6, 26),
        (7, 12), (7, 18), (7, 26),
        (8, 13), (8, 17),
        (9, 14), (9, 15)
                    ]

    alive_cells = Game.random_start(size)
    game = Game(size, alive_cells, cell_char)
    while True:
        print game
        game.evolve()
        sleep(0.2)


if __name__ == '__main__':
    main()
