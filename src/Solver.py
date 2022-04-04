from Constant import *
from Node import *
from PriorityQueue import *

def getEmptySpacePosition(puzzle):
    for i in range (4):
        for j in range (4):
            if (puzzle[i, j] == 0):
                return i, j

def isMoveSafe(x, y):
	return x >= 0 and x < 4 and y >= 0 and y < 4

def isSolvable(puzzle):
    sum = 0
    x = 0 
    kurang = [0 for i in range (16)]
    for row in range (4):
        for col in range (4):
            count = 0
            if puzzle[row, col] == 0:
                if (row + col) % 2 == 1:
                    sum += 1
                    x = 1
                count += 16 - (4 * row + col + 1)
            else:
                for k in range (4 * row + col + 1, 16):
                    subRow = k // 4
                    subCol = k % 4
                    if puzzle[row, col] > puzzle[subRow, subCol] and puzzle[subRow, subCol] != 0:
                        count += 1
            sum += count
            kurang[puzzle[row, col]] = count
    print()
    print("KURANG(i): ")
    for i in range (1, 16):
        print("Kurang(" + str(i) +  ") = " + str(kurang[i]))
    print("Kurang(16) = " + str(kurang[0]))
    print()
    print("X = " + str(x))
    print()
    print("Sum(KURANG(i)) + X = " + str(sum))
    print()
    if (sum % 2 == 0):
        print("Puzzle dapat diselesaikan!")
        print()
        return True
    else:
        print("Puzzle tidak dapat diselesaikan!")
        print()
        return False

def calcCost(puzzle):
    sum = 0
    for row in range (4):
        for col in range (4):
            if (puzzle[row, col] and 
                puzzle[row, col] != target[row, col]):
                sum += 1
    return sum 

def printPuzzle(puzzle):
    print()
    for i in range (4):
        for j in range (4):
            if (puzzle[i, j] != 0):
                if (puzzle[i , j] < 10):
                    print(" " + str(puzzle[i, j]), end=" ")
                else:
                    print(puzzle[i, j], end=" ")
            else:
                print("  ", end=" ")
        print()

def printPath(root, i):
    if root == None:
        print()
        print("Jumlah langkah = " + str(i - 1))
        return
	
    printPath(root.parent, i + 1)
    printPuzzle(root.puzzle)

def solve(puzzle):
    total_node = 0
    pq = PriorityQueue()

    root = Node(None, puzzle, getEmptySpacePosition(puzzle), 0, calcCost(puzzle))
    pq.enqueue(root)
    total_node += 1

    while not pq.isEmpty():
        currNode = pq.dequeue()

        if np.array_equal(currNode.puzzle, target):
            print("Total simpul yang dibangkitkan = " + str(total_node))
            return currNode
        else:
            row, col = currNode.position

            for x, y in move:
                newRow, newCol = row + x, col + y
                if (isMoveSafe(newRow, newCol)):
                    tempPuzzle = np.copy(currNode.puzzle)
                    tempPuzzle[row, col], tempPuzzle[newRow, newCol] = tempPuzzle[newRow, newCol], tempPuzzle[row, col]
                    if not np.array_str(tempPuzzle) in visited.keys():
                        child = Node(currNode, tempPuzzle, (newRow, newCol), currNode.level + 1, calcCost(tempPuzzle))
                        pq.enqueue(child)
                        visited[np.array_str(tempPuzzle)] = child
                        total_node += 1