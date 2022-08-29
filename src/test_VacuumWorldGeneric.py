from aicode.search.SearchAlgorithms import BuscaLargura
from aicode.search.SearchAlgorithms import BuscaProfundidade
from aicode.search.SearchAlgorithms import BuscaProfundidadeIterativa
from VacuumWorldGeneric import *

def test_largura_simple_0():
    file_map_path = 'data/vacuum_simple_0.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    print('Busca em Largura')
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    assert result.show_path() == ""

def test_largura_simple_1():
    file_map_path = 'data/vacuum_simple_1.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    print('Busca em Largura')
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    assert result.show_path() == " ; limpar"

def test_largura_simple_2():
    file_map_path = 'data/vacuum_simple_2.txt'
    lin = 0
    col = 0
    mapa = convert_file_to_map(file_map_path)
    print(mapa)
    print('Busca em Largura')
    state = VacuumWorldGeneric(mapa, lin, col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    print(f'Solução = {result.show_path()}')
    assert result.show_path() == " ; dir ; dir ; baixo ; limpar"