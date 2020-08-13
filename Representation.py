import numpy as np
from scipy.signal import convolve2d
import Rules

class Representation:
    def __init__(self, grid):
        self.grid = grid
        self.neighbours = None

    def get_copy(self):
        return Representation(self.grid.copy())

    def get_neighbours(self, boundary='fill'):
        val = convolve2d(self.grid, np.ones((3,3)), mode='same', boundary=boundary)-self.grid
        return val

    def equals(self, other):
        if other is None:
            return False
        return self.grid == other.grid

    def apply_rules(self, rules, boundary):
        self.neighbours = self.get_neighbours(boundary)
        self.grid = rules.applyRules(self)
        return self
