import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import imageio
import PIL.Image
import Visuals

class Board:
    def __init__(self, initial_state, rules):
        self.initial_state = initial_state
        self.rules = rules

    def begin_game(self, itns, visualizer, boundary):
        state = self.initial_state
        all_states = visualizer.displayAnim(state, itns, self.rules, boundary)
        return all_states

    def save_animation(self, array, filename):
        array = np.uint8(np.clip(array, 0, 1)*255.0)
        frames = []
        for frame in range(array.shape[0]):
            img = PIL.Image.fromarray(array[frame])
            img = img.resize((500, 500))
            frames.append(img)
        img.save(filename, save_all=True, duration=33.33,
                append_images=frames, loop=0, size=(500, 500))

