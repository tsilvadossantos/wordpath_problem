class File(object):
    """Read file and return a list of data"""
    def __init__(self, filename):
        self.__filename = filename
        self.__list_of_words = []

    def read_file(self):
        try:
            with open(self.__filename, "r") as r:
                for line in r:
                    self.__list_of_words.append(str(line.strip()).lower())
        except IOError:
            return False
        return self.__list_of_words
