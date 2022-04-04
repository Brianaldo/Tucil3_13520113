class Node:
    # Class Attribute:
    # parent      : Node Reference
    # puzzle      : np.array([[x, x, x],
    #                         [x, x, x],
    #                         [x, x, x]])
    # position    : np.array([x, y])
    # level       : integer
    # cost        : integer
    def __init__(self, parent, puzzle, position, level, cost):
        self.parent = parent
        self.puzzle = puzzle
        self.position = position
        self.level = level
        self.cost = cost + level

    # Less than definition (>)
    def __gt__(self, next):
        return self.cost > next.cost