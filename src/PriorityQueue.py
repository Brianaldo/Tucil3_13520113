class PriorityQueue:
    # Class Attribute:
    # pq : array of Node
    #      Node terurut menurun
    def __init__(self):
        self.pq = []
    
    # isEmpty
    def isEmpty(self):
        return len(self.pq) == 0

    # enqueue
    def enqueue(self, node):
        if (self.isEmpty()):
            self.pq.append(node)
        else:
            for i in range (0, len(self.pq)):
                if (node > self.pq[i]):
                    self.pq.insert(i, node)
                    return
            self.pq.append(node)

    # dequeue
    def dequeue(self):
        return self.pq.pop()