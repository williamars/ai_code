from aicode.search.SearchAlgorithms import AEstrela
import time 
from Map import *

Map.createHeuristics()
Map.createArea()

def test_a_x():
    state = Map('a',0, 'a','x')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
    else:
        print('Nao achou solucao')
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    print('')
    assert result.g == 12
    print(result.show_path())


def test_b_x():
    state = Map('b',0, 'b','x')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
    else:
        print('Nao achou solucao')
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    print('')
    assert result.g == 9
    print(result.show_path())


def test_c_o():
    state = Map('c',0, 'c','o')
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
    else:
        print('Nao achou solucao')
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    print('')
    assert result.g == 2
    print(result.show_path())