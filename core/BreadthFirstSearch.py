from Queue import Queue

class BreadthFirstSearch(object):
    """ BFS algorithm """ 
    def __init__(self, word1, word2, Graph):
        self.word1 = word1
        self.word2 = word2
        self.graph = Graph

    def set_word1(self, node_name):
        self.word1 = self.word1.node_name

    def get_word1(self):
        return self.word1

    def set_word2(self, node_name):
        self.word2 = self.word2.node_name

    def get_word2(self):
        return self.word2

    def set_graph(self):
        pass

    def get_graph(self):
        return self.word2

    def bfs(self):
        parents = {}
        q = Queue()
        q.enqueue(self.word1)
        parents[self.word1.node_name] = None

        while(not q.empty()):
            node = q.dequeue()
            for neighbour in node.node_neighbours:
                n = neighbour.node_name

                if n not in parents:
                    parents[n] = node.node_name
                    if n == self.word2.node_name:
                        return parents
                    q.enqueue(self.graph[neighbour.node_name])
        return parents
