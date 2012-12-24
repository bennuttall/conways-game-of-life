# Conway's Game of Life

Various Python implementations of the Game of Life, with different coding styles using a range of approaches

## The game

- Cells exist in a square grid, and at any point in the game are either alive or dead.
- On each iteration of the game, cells evolve according to the number of live neighbouring cells:
    - Any live cell with fewer than two neighbours dies (underpopulation)
    - Any live cell with two or three neighbours lives on
    - Any live cell with more than three neighbours dies (overpopulation)
    - Any dead cell with exactly three neighbours becomes alive (reproduction)

en.wikipedia.org/wiki/Conway's_Game_of_Life
