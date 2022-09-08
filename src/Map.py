from aicode.search.SearchAlgorithms import BuscaCustoUniforme, BuscaLargura, BuscaProfundidadeIterativa
from aicode.search.Graph import State
import sys


class Map(State):

    def __init__(self, actual, objective, op):
        self.actual = actual
        self.objective = objective
        self.operator = op
        self.area = Map.createArea()
    
    def sucessors(self):
        sucessors = []


        #TODO
        return sucessors
    
    def is_goal(self):
        return (self.actual == self.objective)
    
    def description(self):
        return "Describe the problem"
    
    def cost(self):
        return 1

    def print(self):
        #
        # Usado para imprimir a solução encontrada. 
        # O PATH do estado inicial até o final.
        return str(self.operator)

    @staticmethod
    def createArea():
        Map.area = {
            'a':[(3,'b'),(6,'c')],
            'b':[(3,'a'),(3,'h'),(3,'k')],
            'c':[(6,'a'),(2,'g'),(3,'d'),(2,'o'),(2,'p')],
            'd':[(3,'c'),(1,'f'),(1,'e')],
            'e':[(2,'i'),(1,'f'),(1,'d'),(14,'m')],
            'f':[(1,'g'),(1,'e'),(1,'d')],
            'g':[(2,'c'),(1,'f'),(2,'h')],
            'h':[(2,'i'),(2,'g'),(3,'b'),(4,'k')],
            'i':[(2,'e'),(2,'h')],
            'l':[(1,'k')],
            'k':[(1,'l'),(3,'n'),(4,'h'),(3,'b')],
            'm':[(2,'n'),(1,'x'),(14,'e')],
            'n':[(2,'m'),(3,'k')],
            'o':[(2,'c')],
            'p':[(2,'c')],
            'x':[(1,'m')]
            }
    
    def env(self):
        #
        # IMPORTANTE: este método não deve apenas retornar uma descrição do environment, mas 
        # deve também retornar um valor que descreva aquele nodo em específico. Pois 
        # esta representação é utilizada para verificar se um nodo deve ou ser adicionado 
        # na lista de abertos.
        #
        # Exemplos de especificações adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)+"#"+str(self.cost)
        # - para o problema das cidades: return self.city+"#"+str(self.cost())
        #
        # Exemplos de especificações NÃO adequadas: 
        # - para o problema do soma 1 e 2: return str(self.number)
        # - para o problema das cidades: return self.city
        #
        None


def main(first_city, second_city):

    
    print('Busca de Custo Uniforme')
    state = Map('')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')
    
    print('Busca em Largura')
    state = Map('')
    algorithm = BuscaLargura()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    first_city = sys.argv[1]
    second_city = sys.argv[2]

    main(first_city, second_city)