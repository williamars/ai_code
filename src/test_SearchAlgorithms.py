from collections import deque
from aicode.search.Graph import Node
import logging
logging.basicConfig(filename='search_algorithms.log', level=logging.DEBUG)
from aicode.search.SearchAlgorithms import *
from VacuumWorld import *

# teste para BuscaLargura
def testeBuscaLargura():
    state = VacuumWorld('right', False, True, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    assert result.g != None and result.g == 2
    print(result.show_path())

# teste para BuscaProfundidade
def testeBuscaProfundidade():
    state = VacuumWorld('right', True, False, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 300)
    print(result.g)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    assert result.g != None and result.g == 300
    print(result.show_path())

# teste para BuscaProfundidadeIterativa
def testeBuscaProfundidadeIterativa():
    state = VacuumWorld('left', True, False, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    assert result.g != None and result.g == 3
    print(result.show_path())







