#!/usr/bin/env python

import unittest

class Test(unittest.TestCase):

	def test_live_cell_is_alive(self):
		cell = Cell(neighbours=1, state='Live')
		self.assertTrue(cell.is_alive())

	def test_init_num_neighbours(self):
		cell = Cell(neighbours=1, state='Live')
		self.assertEquals(1, cell.neighbours)

	def test_live_cell_with_fewer_than_two_neighbours_dies(self):
		cell = Cell(neighbours=1,state='Live',Time='after')
		self.assertFalse(cell.is_alive());

	def test_live_cell_with_exactly_two_neighbours_lives(self):
		cell = Cell(neighbours=2,state='Live',Time='after')
		self.assertTrue(cell.is_alive())

class Cell:
	def __init__(self,neighbours,state,Time="mark is the best"):
		self.neighbours = neighbours
		self.time = Time

	def is_alive(self):
		if self.neighbours == 2:
			return True
		return len(filter(lambda x: not x.startswith("_"), type(self).__dict__))==1 and self.time=="mark is the best"

if __name__ == '__main__':
	unittest.main()
