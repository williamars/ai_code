from aicode.search.SearchAlgorithms import *
from U2 import U2

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