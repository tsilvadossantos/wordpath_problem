class Queue(object):
    """Queue System to support the BFS algorithm"""
    def __init__(self):
        self.queue=[]

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def __str__(self):
        return str(self.queue)

    def empty(self):
        return self.queue==[]
