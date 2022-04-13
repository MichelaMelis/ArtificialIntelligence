import itertools
import numpy as np
import copy


class Node(object):
    id_iter = itertools.count()


    def __init__(self, tiles, parent=-1):
        self.tiles = tiles #state
        self.parent = parent #parent-node
        self.id = next(Node.id_iter) #id of the node
        self.heuristics = 0 #heuristics associated to a certain node
        self.depth = 0
        self.eval = 0

    #def compute_depth(self,Stack, P):
        #while not (P.id == 0):
          #for x in Stack:
              #if x.id == P.parent:
                 #P = x
                 #self.depth += 1



    def compute_heuristics(self, goal_state = np.array( [[1,2,3],[4,5,6],[7,8,0]])): #Manhattan distance used to compute the heuristic
        for i in range(1, 9):
            x, y = np.where(self.tiles == i)
            x1, y1 = np.where(goal_state == i)
            self.heuristics += (abs(x1 - x) + abs(y1 - y))


    def compute_eval(self):
        self.eval = self.depth + self.heuristics



    def get_tiles(self, id):
        if self.id == id:
            return self.tiles
        else:
            return None

    def get_parent_id(self, id):
        if self.id == id:
            return self.parent
        else:
            return None