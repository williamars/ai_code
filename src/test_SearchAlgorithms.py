from aicode.search.SearchAlgorithms import *
from U2 import U2

def test_BuscaLargura():
    print('Busca de Custo Uniforme')
    state = U2(False, False, False, False, False, ' ')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    assert result != None

def test_BuscaProfundidade():
    print('Busca de Custo Uniforme')
    state = U2(False, False, False, False, False, ' ')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 20)
    assert result != None

def test_BuscaCustoUniforme():
    print('Busca de Custo Uniforme')
    state = U2(False, False, False, False, False, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    assert result != None