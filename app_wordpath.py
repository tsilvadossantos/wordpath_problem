__author__ = 'Thiago dos Santos'
__email__ = 'thiago.santos@msn.com'

from core.GetCliArgs import GetArgs
from core.GraphBuild import GraphBuild
from core.BreadthFirstSearch import  BreadthFirstSearch
from core.WordsPath import WordsPath
from core.DataCollection import DataCollection

if __name__ == '__main__':
    graph_dict = {}

    #get the cli arguments
    cli_args = GetArgs()
    arg1, arg2, arg3 = cli_args.get_args()
    filepath, word1, word2 = arg1[0], arg2[0], arg3[0]

    #generate word graph
    g = GraphBuild(graph_dict)
    g.generate_word_graph(filepath)

    #Data collected, validated and displayed
    dc = DataCollection(word1, word2, graph_dict)
    if dc.data_validation() is True:
        predecessors = BreadthFirstSearch(dc.get_word1(), dc.get_word2(), dc.graph_dict).bfs()
        path = WordsPath(dc.get_word1(), dc.get_word2(), predecessors).get_path()
        for string_found in path:
            dc.set_output_data(string_found)
        print dc.get_output_data()[:-2]
    else:
        print 'ERROR: There is no path available from "{}" to "{}"'.format(word1, word2)
