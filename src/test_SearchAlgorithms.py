from aicode.search.SearchAlgorithms import BuscaProfundidade, BuscaLargura, AEstrela
from VacuumWorldGeneric import *
from Map import Map
import time
import networkx as nx


def test_BuscaLargura():
    Map.createArea()
    Map.createHeuristics()

    print('Busca por algoritmo Busca Largura: sair de l e chegar em h')
    state = Map('l', 0, 'l', 'h')
    algorithm = BuscaLargura()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
        print(result.g)
    else:
        print('Nao achou solucao')
    print((tf-ts))
    assert (tf-ts) < 1
    assert result != None and result.show_path().count(";") == 2 and result.g == 5

def test_BuscaProfundidade():
    Map.createArea()
    Map.createHeuristics()

    print('Busca por algoritmo Busca Profundidade: sair de l e chegar em h -- em até 2 ações')
    state = Map('l', 0, 'l', 'h')
    algorithm = BuscaProfundidade()
    ts = time.time()
    result = algorithm.search(state,2)
    tf = time.time()
    if result != None:
        print(result.show_path())
        print(result.g)
    else:
        print('Nao achou solucao')
    assert (tf-ts) < 1
    assert result != None and result.show_path().count(";") == 2 and result.g == 5

    print('Busca por algoritmo Busca Profundidade: sair de l e chegar em h -- em até 3 ações')
    state = Map('l', 0, 'l', 'h')
    algorithm = BuscaProfundidade()
    ts = time.time()
    result = algorithm.search(state,3)
    tf = time.time()
    if result != None:
        print(result.show_path())
        print(result.g)
    else:
        print('Nao achou solucao')
    assert (tf-ts) < 1
    assert result != None and result.show_path().count(";") == 3 and result.g == 7

def test_BuscaAEstrela():
    Map.createArea()
    Map.createHeuristics()

    print('Busca por algoritmo Busca A*: sair de l e chegar em x')
    state = Map('l', 0, 'l', 'x')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
        print(result.g)
    else:
        print('Nao achou solucao')
    assert (tf-ts) < 1
    assert result != None and result.show_path().count(";") == 4 and result.g == 7

    print('Busca por algoritmo Busca A*: sair de c e chegar em x')
    state = Map('c', 0, 'c', 'x')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
        print(result.g)
    else:
        print('Nao achou solucao')
    assert (tf-ts) < 1
    assert result != None and result.show_path().count(";") == 6 and result.g == 14
    
    