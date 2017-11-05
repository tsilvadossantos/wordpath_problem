class DataCollection(object):
    """Generate data collection and validation"""
    def __init__(self, word1, word2, graph_dict):
        self.word1 = word1
        self.word2 = word2
        self.graph_dict = graph_dict
        self.output_data = ''

    def set_word1(self):
        self.word1 = self.graph_dict[self.word1]

    def get_word1(self):
        return self.word1

    def set_word2(self):
        self.word2=self.graph_dict[self.word2]

    def get_word2(self):
        return self.word2

    def set_graph_dict(self):
        pass

    def get_graph_dict(self):
        return self.graph_dict

    def set_output_data(self, string_found):
        self.output_data += string_found + '->'

    def get_output_data(self):
        return self.output_data

    def data_validation(self):
        if self.word1 in self.graph_dict:
            self.set_word1()
            if self.word2 in self.graph_dict:
                self.set_word2()
                return True
            else:
                 return False
        else:
            return False
