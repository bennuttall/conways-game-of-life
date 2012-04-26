#!/usr/bin/env python

import unittest

class Test(unittest.TestCase):
	def test_live_cell_is_alive(self):
		grid = Grid(1)
		cell = Cell(grid=grid, state='Live')
		self.assertTrue(cell.is_alive())

	def test_live_cell_with_fewer_than_two_neighbours_dies(self):
		grid = Grid(1)
		cell = Cell(grid=grid, state='Live')
		cell = cell.tick()
		self.assertFalse(cell.is_alive())

	def test_live_cell_with_two_neighbours_lives(self):
		grid = Grid(2)
		cell = Cell(grid=grid, state='Live')
		cell = cell.tick()
		self.assertTrue(cell.is_alive())

	def test_live_cell_with_three_neighbours_lives(self):
		grid = Grid(3)
		cell = Cell(grid=grid, state='Live')
		cell = cell.tick()
		self.assertTrue(cell.is_alive())

	def test_live_cell_with_more_than_three_neighbours_dies(self):
		grid = Grid(4)
		cell = Cell(grid=grid, state='Live')
		cell = cell.tick()
		self.assertFalse(cell.is_alive())

	def test_dead_cell_with_exactly_three_neighbours_is_born(self):
		grid = Grid(3)
		cell = Cell(grid=grid, state='Dead')
		cell = cell.tick()
		self.assertTrue(cell.is_alive())

class Cell:
	def __init__(self,grid,state):
		self.grid = grid
		self.state = state

	@property
	def neighbours(self):
		return self.grid.num_neighbours(self)

	def is_alive(self):
		return self.state == 'Live'
		
	def tick(self):
		if self.state == 'Live':
			if self.neighbours == 2 or self.neighbours == 3:
				return self
			else:
				return Cell(self.neighbours, 'Dead')
		else:
			if self.neighbours == 3:
				return Cell(self.neighbours, 'Live')

class Grid():
	def __init__(self, population):
		#self.neighbours = neighbours
		self.population = population

	def num_neighbours(self, x, y):
		neighbours = self.population[x-1][y-1]
		neighbours += self.population[x-1][y]
		neighbours += self.population[x-1][y+1]
		neighbours += self.population[x][y-1]
		#neighbours += self.population[x,y]
		neighbours += self.population[x][y+1]
		neighbours += self.population[x+1][y-1]
		neighbours += self.population[x+1][y]
		neighbours += self.population[x+1][y+1]
		return neighbours

if __name__ == '__main__':
	unittest.main()
