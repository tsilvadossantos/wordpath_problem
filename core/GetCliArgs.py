import argparse

class GetArgs(object):
    """Get command line arguments"""
    def __init__(self):
        parser = argparse.ArgumentParser(description='Word ladder Puzzle - Find the path between a start and end word')
        parser.add_argument('--file', type=str, help='path to target file', required=True, nargs='+')
        parser.add_argument('--word1', type=str, help='word to start the path', required=True, nargs='+')
        parser.add_argument('--word2', type=str, help='word to end the path', required=True, nargs='+')
        self.args = parser.parse_args()
        self.f = self.args.file
        self.w1 = self.args.word1
        self.w2 = self.args.word2

    def get_args(self):
        return self.f, self.w1, self.w2
