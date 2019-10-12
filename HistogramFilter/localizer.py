import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = [[0.0 for j in range(len(grid[0]))] for i in range(len(grid))]

    #
    # TODO - implement this in part 2
    #
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            hit = (grid[i][j] == color)
            new_beliefs[i][j] = beliefs[i][j] * (hit * p_hit + (1-hit) * p_miss)
    total = sum(map(sum, new_beliefs))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            new_beliefs[i][j] /= total
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for j in range(width)] for i in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % height
            new_j = (j + dx ) % width
            # pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)