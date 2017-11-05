from WordsPath import WordsPath
from Node import Node
from File import File

class GraphBuild(object):
    """Build a graph of words"""
    def __init__(self, graph_dict):
        self.graph_dict = graph_dict

    def generate_word_graph(self, filepath):
        w = {}
        f = File(filepath)
        words = f.read_file()

        for word in words:
            for i in range(len(word)):
                wild_card = word[:i] + '*' + word[i + 1:]
                if wild_card in w:
                    w[wild_card].append(word)
                else:
                    w[wild_card] = [word]
        for key in w:
            wordlist = w[key]
            for w1 in wordlist:
                for w2 in wordlist:
                    if w1 != w2:
                        self.insert_word_to_graph(w1, w2)

    def insert_word_to_graph(self, word1, word2):
        if word1 not in self.graph_dict:
            node = Node(word1)
            node.node_neighbours.append(Node(word2))
            self.graph_dict[word1] = node
        else:
            node_neighbours = self.graph_dict[word1].node_neighbours
            if word2 not in [x.node_name for x in node_neighbours]:
                node_neighbours.append(Node(word2))

        if word2 not in self.graph_dict:
            node = Node(word2)
            node.node_neighbours.append(Node(word1))
            self.graph_dict[word2] = node
        else:
            node_neighbours = self.graph_dict[word2].node_neighbours
            if word1 not in [x.node_name for x in node_neighbours]:
                node_neighbours.append(Node(word1))
