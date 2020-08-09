import numpy as np

class SetRules:
    def applyRules(self, grid, neighbours):
        ret_grid = grid.copy()
        
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if(neighbours[i][j] > 3 or neighbours[i][j] < 2):
                    ret_grid[i][j] = 0
                elif(grid[i][j] == 1 and (neighbours[i][j] == 2 or neighbours[i][j] == 3)):
                    ret_grid[i][j] = 1
                elif(grid[i][j] == 0 and (neighbours[i][j]==3)):
                    ret_grid[i][j] = 1

        return ret_grid

