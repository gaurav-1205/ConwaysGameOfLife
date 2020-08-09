import numpy as np
import matplotlib.pyplot as plt
import Board
import Representation as rep
import SetRules
import time
from Visuals import Visuals


def getInput():
    configs = {
        1: "10_cell_row",
        2: "exploder",
        3: "glider",
        4: "gosper_glider_gun",
        5: "john_conway",
        6: "small_exploder",
        7: "spaceship",
        8: "tumbler",
        9: "random",
        10: "custom"
    }
    rows = int(input("Enter number of rows "))
    cols = int(input("Enter number of cols "))
    
    for key, val in configs.items():
        print(str(key) + ". " + val)

    option = int(input("Select Option "))
    return rows, cols, configs[option]


rows, cols, name = getInput()

visualizer = Visuals(rows, cols)
selection = visualizer.InitializeInputGrid(name=name)
selection = np.array(visualizer.SetInput(selection))
# np.save('./saved_configs/john_conway', selection)

rules = SetRules.SetRules()
game = Board.Board(rep.Representation(selection), rules)
t = time.time()
result = game.begin_game(5000, visualizer)
print(time.time()-t)




