import sys, os
import unittest
sys.path.append(os.path.abspath('../core'))
from File import File
from DataCollection import DataCollection
from GraphBuild import GraphBuild

class FileTestCase(unittest.TestCase):
    """Test a given filepath."""

    def setUp(self):
        self.f1 = File('/usr/share/dict/words')
        self.f2 = File('/usr/share/dict/fake_file')

    def test_file_exists(self):
        """Assert a given file exists"""
        self.assertTrue(self.f1.read_file())

    def test_file_not_exists(self):
        """Assert a given file does not exist"""
        self.assertFalse(self.f2.read_file())

class DataValidationTestCase(unittest.TestCase):
    """Assert Word Path"""
    def setUp(self):
        self.graph_dict = {}
        self.filepath, self.word11, self.word21 = '/usr/share/dict/words', 'lead', 'gold'
        self.word12, self.word22 = 'NotinDict', 'gold'
        self.word13, self.word23 = 'lead', 'NotinDict'

    def test_wordpath_exists(self):
        """Assert first word has a path two a second given word"""
        #generate word graph
        g = GraphBuild(self.graph_dict)
        g.generate_word_graph(self.filepath)
        dc = DataCollection(self.word11, self.word21, self.graph_dict)
        self.assertTrue(dc.data_validation())

    def test_wordpath_from_first_word(self):
        """Assert first word has no path two a second word"""
        #generate word graph
        g = GraphBuild(self.graph_dict)
        g.generate_word_graph(self.filepath)
        dc = DataCollection(self.word12, self.word22, self.graph_dict)
        self.assertFalse(dc.data_validation())

    def test_wordpath_to_second_word(self):
        """Assert second word is not path-able"""
        #generate word graph
        g = GraphBuild(self.graph_dict)
        g.generate_word_graph(self.filepath)
        dc = DataCollection(self.word13, self.word23, self.graph_dict)
        self.assertFalse(dc.data_validation())

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
