from Puzzle8 import Puzzle8
from datetime import datetime

tabuleiro_trivial = [[1,2,3],[8,4,0],[7,6,5]]
tabuleiro_facil = [[8,1,3],[0,7,2],[6,5,4]]
tabuleiro_dificil0 = [[8,3,6],[7,5,4],[2,1,0]]
tabuleiro_dificil1 = [[7,8,6],[2,3,5],[1,4,0]]
tabuleiro_dificil2 = [[7,8,6],[2,3,5],[0,1,4]]
tabuleiro_dificil3 = [[3,1,2],[5,4,8],[0,6,7]]
tabuleiro_impossivel1 = [[3,4,8],[1,2,5],[7,0,6]]
tabuleiro_impossivel2 = [[5,4,0],[6,1,8],[7,3,2]]
tabuleiro_impossivel3 = [[1,7,2],[3,9,5],[6,4,8]]
tabuleiro_impossivel4 = [[3,1,2],[5,4,8],[0,7,6]]
tabuleiro_invertido = [[8,7,6],[5,0,4],[3,2,1]]

def test_trivial():
    print('trivial')    
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_trivial, '')
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; esquerda"

def test_facil():
    print('facil')    
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_facil, '')
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; direita ; direita ; baixo ; esquerda ; esquerda ; cima ; cima ; direita ; baixo"

def test_facil2():
    print('facil')    
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_facil, '')
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; direita ; direita ; baixo ; esquerda ; esquerda ; cima ; cima ; direita ; baixo"

def test_dificil0():
    print('dificil 0')    
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_dificil0, '')
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; cima ; esquerda ; esquerda ; baixo ; direita ; cima ; direita ; cima ; esquerda ; esquerda ; baixo ; baixo ; direita ; cima ; direita ; baixo ; esquerda ; cima ; cima ; esquerda ; baixo ; direita"
                
def test_dificil1():
    print('dificil 1')
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_dificil1, '')
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; cima ; esquerda ; baixo ; esquerda ; cima ; cima ; direita ; direita ; baixo ; esquerda ; esquerda ; baixo ; direita ; cima ; cima ; esquerda ; baixo ; baixo ; direita ; cima ; cima ; esquerda ; baixo ; direita"

def test_dificil2():
    print('dificil 2')
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_dificil2, '')
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; cima ; cima ; direita ; baixo ; esquerda ; baixo ; direita ; cima ; direita ; cima ; esquerda ; esquerda ; baixo ; baixo ; direita ; cima ; direita ; baixo ; esquerda ; cima ; cima ; esquerda ; baixo ; direita"

def test_dificil3():
    print('dificil 3')
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_dificil3, '')
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; direita ; direita ; cima ; esquerda ; esquerda ; baixo ; direita ; cima ; esquerda ; cima ; direita ; direita ; baixo ; baixo ; esquerda ; cima ; esquerda ; cima ; direita ; baixo ; direita ; cima ; esquerda ; esquerda ; baixo ; direita"

def test_impossivel1():
    print('impossivel 1')
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_impossivel1, '')
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == "Nao tem solucao"

def test_impossivel2():
    print('impossivel 2')
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_impossivel2, '')
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == "Nao tem solucao"

def test_impossivel3():
    print('impossivel 3')
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_impossivel3, '')
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == "Nao tem solucao"

def test_tabuleiro_invertido():
    print('invertido')
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_dificil2, '')
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r.count(";") <= 25
   