<?php
	
	class World {

		private $grid;
		private $size;

		public function World ($size) {
			$this->size = $size;
			$this->grid = array();
			foreach (range(0, $size*$size) as $i) {
				$this->grid[$i] = 0;
			}
		}

		public function printer () {
			foreach (range(0, $this->size-1) as $i) {
				foreach (range(0, $this->size-1) as $j) {
					echo $this->grid[$i * $this->size + $j] . " "; 
				}
				echo PHP_EOL;
			}
			echo PHP_EOL;
		}

		public function conceive_cell ($x, $y) {
			$this->grid[$x * $this->size + $y] = 1;
		}

		private function get_cell ($x, $y) {
			if ($x >= $this->size || $y >= $this->size)
				return 0;
			if ($x < 0 || $y < 0)
				return 0;
			return $this->grid[$x * $this->size + $y];
		}

		private function neighbour_count ($x, $y) {
			$c = 0;
			$c += $this->get_cell($x - 1, $y - 1); 
			$c += $this->get_cell($x - 1, $y);
			$c += $this->get_cell($x - 1, $y + 1);
			$c += $this->get_cell($x, $y - 1); 
			$c += $this->get_cell($x, $y + 1);
			$c += $this->get_cell($x + 1, $y - 1); 
			$c += $this->get_cell($x + 1, $y);
			$c += $this->get_cell($x + 1, $y + 1);
			return $c;		
		}

		public function evolve () {
			foreach (range(0, $this->size-1) as $i) {
				 foreach (range(0, $this->size-1) as $j) {
					if ($this->neighbour_count($i, $j) < 2)
						$this->grid[$i * $this->size + $j] = 0; 
					elseif ($this->neighbour_count($i, $j) > 3)
						$this->grid[$i * $this->size + $j] = 0; 
					elseif ($this->neighbour_count($i, $j) == 3)
						$this->grid[$i * $this->size + $j] = 1; 
				}
			}
		}
	}

	$world = new World(10);
	echo PHP_EOL;
	$world->printer();

	$world->conceive_cell(5, 5);
	$world->conceive_cell(5, 6);
	$world->conceive_cell(6, 5);
	$world->conceive_cell(7, 5);
 	$world->printer();

	$world->evolve();
  	$world->printer();