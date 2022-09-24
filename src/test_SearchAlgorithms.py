from aicode.search.SearchAlgorithms import BuscaLargura, BuscaProfundidade, BuscaProfundidadeIterativa
from VacuumWorld import VacuumWorld

def test_BuscaLargura():
    state = VacuumWorld('right', False, False, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if (result == None):
      print('Sem solução!')
    assert result.g != 0  and result.show_path() == " ; clean ; Move Left ; clean"

def test_BuscaProfundidade():
    state = VacuumWorld('right', False, False, '')
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 10)
    if (result == None):
      print('Sem solução!')
    assert result.g != 0 and result.show_path() == " ; clean ; clean ; clean ; clean ; clean ; clean ; clean ; clean ; Move Left ; clean"

def test_BuscaProfundidadeIterativa():
    state = VacuumWorld('right', False, False, '')
    algorithm = BuscaProfundidadeIterativa()
    result = algorithm.search(state)
    if (result == None):
      print('Sem solução!')
    assert result.g != 0 and result.show_path() == " ; clean ; Move Left ; clean"