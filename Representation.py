import numpy as np
from scipy.signal import convolve2d
import SetRules

class Representation:
    def __init__(self, grid, boundary='fill'):
        self.grid = grid
        self.neighbours = convolve2d(self.grid, np.ones((3,3)), mode='same', boundary=boundary)-self.grid

    def get_copy(self):
        return Representation(self.grid.copy())

    def get_neighbours(self, boundary='fill'):
        val = convolve2d(self.grid, np.ones((3,3)), mode='same', boundary=boundary)-self.grid
        return val

    def equals(self, other):
        if other is None:
            return False
        return self.grid == other.grid

    def apply_rules(self, rules):
        neighbours = self.get_neighbours()
        self.grid = rules.applyRules(self.grid, neighbours)
        return self
