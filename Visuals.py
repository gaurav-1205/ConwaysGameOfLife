import pygame
import numpy as np

class Visuals:
    def __init__(self, rows, cols):
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.YELLOW = (255, 255, 0)
        self.RED = (255, 0, 0)
        self.GRAY = (128, 128, 128)

        self.max_height = 840
        self.max_width = 1260

        self.MARGIN = 1

        self.rows = rows
        self.cols = cols

        self.WIDTH = min((self.max_width//cols)-self.MARGIN, (self.max_height//rows)-self.MARGIN)
        self.HEIGHT = self.WIDTH 


    def InitializeInputGrid(self, name='random'):
        flag = 0
        if(name == 'john_conway'):
            grid = np.load('./saved_configs/john_conway.npy')
            flag = 1
        elif(name == 'tumbler'):
            grid = np.load('./saved_configs/tumbler.npy')
            flag = 1
        elif(name == 'spaceship'):
            grid = np.load('./saved_configs/spaceship.npy')
            flag = 1
        elif(name == 'small_exploder'):
            grid = np.load('./saved_configs/small_exploder.npy')
            flag = 1
        elif(name == 'gosper_glider_gun'):
            grid = np.load('./saved_configs/gosper_glider_gun.npy')
            flag = 1
        elif(name == 'glider'):
            grid = np.load('./saved_configs/glider.npy')
            flag = 1
        elif(name == 'exploder'):
            grid = np.load('./saved_configs/exploder.npy')
            flag = 1
        elif(name == '10_cell_row'):
            grid = np.load('./saved_configs/10_cell_row.npy')
            flag = 1
        elif(name == 'random'):
            grid = np.random.random((self.rows, self.cols))
            grid[grid >= 0.6] = 1
            grid[grid < 0.6] = 0
        elif(name == 'custom'):
            grid = []
            for row in range(self.rows):
                grid.append([])
                for column in range(self.cols):
                    grid[row].append(0) 
            grid = np.array(grid)

        if(flag==1):
            grid = self.checkConsistency(grid)
        return grid
        
    def checkConsistency(self, grid):
        grid_rows = grid.shape[0]
        grid_cols = grid.shape[1]
        
        self.rows = max(grid_rows, self.rows)
        self.cols = max(grid_cols, self.cols)
        
        self.WIDTH = min((self.max_width//self.cols)-self.MARGIN,(self.max_height//self.rows)-self.MARGIN)
        self.HEIGHT = self.WIDTH

        new_grid = np.zeros((self.rows, self.cols))
        diff1 = self.rows - grid_rows
        diff2 = self.cols - grid_cols
        new_grid[diff1//2: diff1//2 + grid_rows, diff2//2: diff2//2 + grid_cols] = grid

        return new_grid

    def SetInput(self, grid):
        
        rows = grid.shape[0]
        cols = grid.shape[1]

        pygame.init()

        WINDOW_SIZE = [cols*(self.WIDTH+self.MARGIN), rows*(self.HEIGHT+self.MARGIN)]
        screen = pygame.display.set_mode(WINDOW_SIZE)

        pygame.display.set_caption("Game of Life")

        done = False

        clock = pygame.time.Clock()

        while not done:
            for event in pygame.event.get():  
                if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN)):  
                    done = True  
                elif event.type == pygame.MOUSEBUTTONDOWN:                    
                    pos = pygame.mouse.get_pos()
                    
                    column = pos[0] // (self.WIDTH + self.MARGIN)
                    row = pos[1] // (self.HEIGHT + self.MARGIN)
                    
                    if(grid[row][column]==1):
                        grid[row][column] = 0
                    else:
                        grid[row][column] = 1
                    print("Grid coordinates: ", row, column)

            screen.fill(self.BLACK)

            for row in range(rows):
                for column in range(cols):
                    color = self.GRAY
                    if grid[row][column] == 1:
                        color = self.YELLOW
                    pygame.draw.rect(screen,
                                    color,
                                    [(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                                    (self.MARGIN + self.HEIGHT) * row + self.MARGIN,
                                    self.WIDTH,
                                    self.HEIGHT])

            clock.tick(60)
            pygame.display.update()

        pygame.quit()
        return grid

    def displayAnim(self, state, itns, rules):

        WINDOW_SIZE = [self.cols*(self.WIDTH+self.MARGIN),self.rows*(self.HEIGHT+self.MARGIN)]
        screen = pygame.display.set_mode(WINDOW_SIZE)

        pygame.display.set_caption("Game of Life")

        done = False

        clock = pygame.time.Clock()

        all_states = np.zeros((itns+1, self.rows, self.cols))
        prev_state = None

        while not done:
            for event in pygame.event.get():  
                if (event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN)): 
                    done = True  

            screen.fill(self.BLACK)

            for i in range(itns):
                for row in range(self.rows):
                    for column in range(self.cols):
                        color = self.GRAY
                        if state.grid[row][column] == 1:
                            color = self.YELLOW
                        pygame.draw.rect(screen,
                                        color,
                                        [(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                                        (self.MARGIN + self.HEIGHT) * row + self.MARGIN,
                                        self.WIDTH,
                                        self.HEIGHT])

                fps = 10
                if(self.rows > 100 or self.cols > 100):
                    fps = 30
                clock.tick(fps)

                pygame.display.update()

                prev_state = state.get_copy()
                all_states[i] = prev_state.grid
                state = state.apply_rules(rules)

            break
        return all_states

