class WordsPath(object):
    """Generate word path"""
    def __init__(self, word1, word2, parents):
        self.word1 = word1
        self.word2 = word2
        self.parents = parents

    def set_word1(self, node_name):
        self.word1 = self.word1.node_name

    def get_word1(self):
        return self.word1

    def set_word2(self, node_name):
        self.word2 = self.word2.node_name

    def get_word2(self):
        return self.word2

    def set_parents(self):
        pass

    def get_parents(self):
        return self.word2

    def get_path(self):
        word2=self.word2.node_name
        path=[word2]
        if word2 in self.parents:
            node=self.parents[word2]
            while(node!=self.word1.node_name):
                path.append(node)
                node=self.parents[node]
        else:
            return False
        path.append(self.word1.node_name)
        return path[::-1]
