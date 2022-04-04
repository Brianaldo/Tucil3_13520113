import numpy as np

target = np.array([[ 1,  2,  3,  4],
                   [ 5,  6,  7,  8],
                   [ 9, 10, 11, 12],
                   [13, 14, 15,  0]])

move = np.array([[-1,  0], # up
                 [ 1,  0], # down
                 [ 0, -1], # left
                 [ 0,  1]] # right
                ) 

visited = {}