from Node.Node import Node
import numpy as np

class Solver:

    def __init__(self,initial_state):
        self.initial_state = initial_state
        self.goal_state = np.array([[1,2,3],[4,5,6],[7,8,0]])
        self.P = Node(initial_state) #parent node
        self.F = []        #fringe for the nodes that wait to be expanded
        self.Stack = []    #stack where all expanded nodes will be saved
        self.Path = []     #only parents node that are in the path solution are saved
        self.cost = 0      #cost of the solution


    #auxiliary function to select which node to expand next in A*
    def select(self):
        min = self.F[0]
        for j in self.F:
            if j.heuristic <= min.heuristic:
                min = j
        self.F.remove(min)
        self.P = min
        return self.P

    #generating new possible states
    def move(self, x ,y ):

        # EXPAND THE PARENT STATE P, considering all possible moves
        # move a tile down only if the empty space is not in the first row, only on row 1 or 2
        already = 0
        if x > 0:
            C = Node(np.copy(self.P.tiles), np.copy(self.P.id))  # 0
            C.tiles[x, y] = self.P.tiles[x - 1, y]  # moving the tile
            C.tiles[x - 1, y] = 0  # empty space in
            C.compute_heuristics()
            # checking if the newly generated node has a configuration that already exists
            for j in self.Stack:
                if (j.tiles == C.tiles).all():
                    already = 1
                    break

            if already == 0:
                self.F.append(C)  # adding a new child to the fringe only if has not the same configuration

        already = 0

        # move a tile up only if the empty space is not in the 3rd (last) row, only on row 0 or 1
        if x < 2:
            C = Node(np.copy(self.P.tiles), self.P.id)
            C.tiles[x, y] = self.P.tiles[x + 1, y]
            C.tiles[x + 1, y] = 0
            C.compute_heuristics()

            #checking if the newly generated node has a configuration that already exists
            for j in self.Stack:
                if (j.tiles == C.tiles).all():
                    already = 1
                    break
            if already == 0:
                self.F.append(C)
        already = 0

        # move a tile on the left
        if y < 2:
            C = Node(np.copy(self.P.tiles), self.P.id)
            C.tiles[x, y] = self.P.tiles[x, y + 1]
            C.tiles[x, y + 1] = 0
            C.compute_heuristics()

            # checking if the newly generated node has a configuration that already exists
            for j in self.Stack:
                if (j.tiles == C.tiles).all():
                    already = 1
                    break
            if already == 0:
                self.F.append(C)
        already = 0

        # move a tile on the right
        if y > 0:
            C = Node(np.copy(self.P.tiles), self.P.id)
            # print(C.id)
            # print(C.parent)
            C.tiles[x, y] = self.P.tiles[x, y - 1]
            C.tiles[x, y - 1] = 0
            C.compute_heuristics()

            # checking if the newly generated node has a configuration that already exists
            for j in self.Stack:
                if (j.tiles == C.tiles).all():
                    already = 1
                    break

            if already == 0:
                self.F.append(C)
        already = 0

    #successor function that chooses which node will be expanded next
    def successor(self):
        # BFS explores the first states, the one located at the beginning of the frontier
        #self.P = self.F[0]  # new state P, exploring a new child from the fringe, the first one
        #self.F = self.F[1:]  # updating the fringe, removing the explored child node
        #self.Stack.append(self.P)  # appending

        # DFS explores the last state of the fringe, the one located at the end of the frontier
         self.P = self.F[-1] #new state P, exploring a new child from the fringe, the last one
         self.F = self.F[:-1] #updating the fringe, removing the explored child node
         self.Stack.append(self.P) #appending

        # A* selects the node in the fringe characterised by the lowest value of the heuristics function associated to each node
        #self.P = self.select()
        #self.Stack.append(self.P)

    def solve_puzzle(self):
         # first visited state
         self.Stack.append(self.P)


         while not (self.goal_state == self.P.tiles).all():
            # finding the position of the empty space
            x, y = np.where(self.P.tiles == 0) # riga, colonna
            Solver.move(self,x,y)
            self.successor()

         print("A solution has been found")

         # recall the optimal path
         # restart from the final state (goal)

         self.Path.append(self.P)  # sequence of all states explored

         # looping to find the parent of the state, until the parent state becomes equal to the initial state

         while not (self.initial_state == self.P.tiles).all():
            for x in self.Stack:
               if x.id == self.P.parent:
                  self.P = x
                  self.Path.append(self.P)
                  self.cost += 1

         # flip the path to reverse it, since I want to go from initial_state to goal_state
         self.Path.reverse()

         print("Path of the solution:")
         [print(x.id) for x in self.Path]

         print("Cost of the solution: ", self.cost)
         print("Number of nodes expanded:" ,len(self.Path))


