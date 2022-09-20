from aicode.search.SearchAlgorithms import BuscaLargura
from aicode.search.SearchAlgorithms import BuscaProfundidade
from aicode.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aicode.search.Graph import State
import sys
import numpy as np


def convert_file_to_map(file):
    with open(file, 'r') as f:
        matrix = []
        for row in f:
            linha = row[:-1].split(";")
            for i, number in enumerate(linha):
                linha[i] = int(number)
            matrix.append(linha)
    return matrix


class VacuumWorldGeneric(State):
    def __init__(self, map, row, col, op):
        self.map = map
        self.row = row
        self.col = col
        self.operator = op

    def env(self):
        return str(self.map) + ";" + str(self.row) + ";" + str(self.col) + ";" + str(self.operator)

    def sucessors(self):
        sucessors = []

        if self.map[int(self.row)][int(self.col)] == 1:
            new = np.copy(self.map)
            new[int(self.row)][int(self.col)] = 0
            sucessors.append(VacuumWorldGeneric(
                map=new, row=self.row, col=self.col, op="limpar"))

        quarto_direita = int(self.col) + 1
        quarto_esquerda = int(self.col) - 1
        quarto_baixo = int(self.row) + 1
        quarto_cima = int(self.row) - 1

        if quarto_esquerda >= 0:
            sucessors.append(VacuumWorldGeneric(
                map=self.map, row=self.row, col=quarto_esquerda, op="esq"))
        
        if quarto_direita < len(self.map[0]):
            sucessors.append(VacuumWorldGeneric(
                map=self.map, row=self.row, col=quarto_direita, op="dir"))
        
        if quarto_baixo < len(self.map):
            sucessors.append(VacuumWorldGeneric(
                map=self.map, row=quarto_baixo, col=self.col, op="baixo"))
        
        if quarto_cima >= 0:
            sucessors.append(VacuumWorldGeneric(
                map=self.map, row=quarto_cima, col=self.col, op="cima"))
        
        return sucessors

    def is_goal(self):
        for row in self.map:
            for col in row:
                if int(col) == 1:
                    return False
        return True

    def description(self):
        return "Problema do aspirador de pó genérico"

    def cost(self):
        return 1

    def print(self):
        return str(self.operator)


def main(filename, initial_row, initial_col):
    #
    # Executando busca em largura
    #
    map = convert_file_to_map(file=filename)
    state = VacuumWorldGeneric(map, initial_row, initial_col, '')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')


if __name__ == '__main__':
    filename = sys.argv[1]
    initial_row = sys.argv[2]
    initial_col = sys.argv[3]

    main(filename, initial_row, initial_col)