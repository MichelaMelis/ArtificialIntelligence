import numpy as np
from solution.Solver import Solver


initial_state = np.array([[4,1,2], [0,8,7],  [6,3,5]] )
#strategy = "BFS"
#strategy = "DFS"
strategy = "A*"


# check if a given instance of 8 puzzle is solvable or not

# A utility function to count
# inversions in given array 'arr[]'
def getInvCount(arr):
    inv_count = 0
    empty_value = 0
    for i in range(0, 9):
        for j in range(i+1 , 9):
            if arr[j] != empty_value and arr[i] != empty_value and arr[i] > arr[j]:
                inv_count += 1
    return inv_count

# This function returns true
# if given 8 puzzle is solvable.
def isSolvable(puzzle):
    # Count inversions in given 8 puzzle
    inv_count = getInvCount([j for sub in puzzle for j in sub])
    # return true if inversion count is even.
    return (inv_count % 2 == 0)


if (isSolvable(initial_state)):
    print("Solvable")
else:
    exit("Not Solvable")


Solution = Solver(initial_state,strategy)
Solution.solve_puzzle()
print(strategy)


