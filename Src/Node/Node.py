import itertools
import numpy as np


class Node(object):
    id_iter = itertools.count()
    heuristic = 0

    def __init__(self, tiles, parent=-1):
        self.tiles = tiles
        self.parent = parent
        self.id = next(Node.id_iter)

    def compute_heuristics(self, goal_state = np.array( [[1,2,3],[4,5,6],[7,8,0]])):
        for i in range(1, 9):
            x, y = np.where(self.tiles == i)
            x1, y1 = np.where(goal_state == i)
            self.heuristic += (abs(x1 - x) + abs(y1 - y))
