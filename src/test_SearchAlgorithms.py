from aicode.search.SearchAlgorithms import *
from aicode.search.Graph import Node
from VacuumWorld import *
from U2 import U2

from collections import deque

import logging
logging.basicConfig(filename='search_algorithms.log', level=logging.DEBUG)

def test_BuscaLargura():
    print('\nBusca em Largura')
    state = U2(False, False, False, False, False, ' ')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print("custo",result.g)
    assert result.g >= 17

def test_BuscaProfundidade():
    print('\nBusca em Profundidade')
    state = U2(False, False, False, False, False, ' ')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 20)
    print("custo",result.g)
    assert result.g > 17

def test_BuscaCustoUniforme():
    print('\nBusca de Custo Uniforme')
    state = U2(False, False, False, False, False, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    print("custo",result.g)
    assert result.g <= 17

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
