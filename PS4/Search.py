# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

# grid = [[0, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 0, 1, 0],
#         [0, 0, 1, 1, 1, 0],
#         [0, 0, 0, 0, 1, 0]]
# grid = [[0, 1],
#         [0, 0]]
grid = [[0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    entries = []
    entries.append([0, init[0], init[1]])
    print entries
    current = entries.pop(0)
    grid[current[1]][current[2]] = 1
    while current[1] != goal[0] or current[2] != goal[1]:
        # try all movements
        for deltaIndex in range(len(delta)):
            deltaXY = delta[deltaIndex]
            deltaX = deltaXY[1]
            deltaY = deltaXY[0]
            newX = current[1] + deltaX
            newY = current[2] + deltaY
            if newX >= 0 and newX <= len(grid)-1:
                if newY >= 0 and newY <= len(grid[0])-1:
                    #within bounds.
                    newPoint = grid[newX][newY]
                    if newPoint != 1:
                        entries.append([current[0] + cost, newX, newY])
        sorted(entries)
        print entries
        print grid
        if len(entries) == 0:
            return "fail"
        current = entries.pop(0)
        grid[current[1]][current[2]] = 1

    path = current
    return path

print search(grid, init, goal, cost)