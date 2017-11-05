class Node(object):
    """Node abstraction to support the BFS and WordsPath class"""
    __slots__ = ('node_name', 'node_neighbours')
    
    def __init__(self, node_name):
        self.node_name = node_name
        self.node_neighbours = []

    def __str__(self):
        result = self.node_name + ' : '
        for n in self.node_neighbours:
            result += n.node_name + ', '
        return result[:-1]
