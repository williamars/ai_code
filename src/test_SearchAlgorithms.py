from collections import deque
from aicode.search.Graph import Node
import logging
logging.basicConfig(filename='search_algorithms.log', level=logging.DEBUG)
from aicode.search.SearchAlgorithms import *
from VacuumWorld import *

# teste para BuscaLargura
def testeBuscaLargura():
    state = VacuumWorld('right', False, False, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    assert result.g != None
    print(result.show_path())

# teste para BuscaProfundidade
def testeBuscaProfundidade():
    state = VacuumWorld('right', False, False, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 10)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    assert result.g != None
    print(result.show_path())

# teste para BuscaProfundidadeIterativa
def testeBuscaProfundidadeIterativa():
    state = VacuumWorld('right', False, False, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    assert result.g != None
    print(result.show_path())

# teste para CustoUniforme
def testeCustoUniforme():
    state = VacuumWorld('right', False, False, '')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    assert result.g != None
    print(result.show_path())






