#!/usr/bin/env python

import unittest

class Test(unittest.TestCase):
	def test_live_cell_is_alive(self):
		cell = Cell(neighbours=1, state='Live')
		self.assertTrue(cell.is_alive())

	def test_live_cell_dies_if_fewer_than_two_neighbours(self):
		cell = Cell(neighbours=1, state='Live')
		cell.tick()
		self.assertFalse(cell.is_alive())

	def test_live_cell_lives_if_two_neighbours(self):
		cell = Cell(neighbours=2, state='Live')
		cell.tick()
		self.assertTrue(cell.is_alive())

	def test_live_cell_lives_if_three_neighbours(self):
		cell = Cell(neighbours=3, state='Live')
		cell.tick()
		self.assertTrue(cell.is_alive())

	def test_live_cell_dies_if_more_than_three_neighbours(self):
		cell = Cell(neighbours=4, state='Live')
		cell.tick()
		self.assertFalse(cell.is_alive())

	def test_dead_cell_is_born_if_three_neighbours(self):
		cell = Cell(neighbours=3, state='Dead')
		cell.tick()
		self.assertTrue(cell.is_alive())

	def test_dead_cell_with_two_neighbours_stays_dead(self):
		cell = Cell(neighbours=2, state='Dead')
		cell.tick()
		self.assertFalse(cell.is_alive())

class Cell:
	def __init__(self,neighbours,state):
		self.neighbours = neighbours
		self.state = state

	def tick(self):
		if self.state == 'Live':
			self.state = 'Live' if (self.neighbours == 2 or self.neighbours == 3) else 'Dead'

	def is_alive(self):
		return self.state == 'Live'
		

if __name__ == '__main__':
	unittest.main()
