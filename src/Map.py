
from aicode.search.SearchAlgorithms import BuscaProfundidadeIterativa
from aicode.search.SearchAlgorithms import BuscaCustoUniforme
from aicode.search.SearchAlgorithms import BuscaGananciosa
from aicode.search.SearchAlgorithms import AEstrela
from aicode.search.Graph import State
import time
import networkx as nx
import csv

class Map(State):
    def __init__(self, actual, objective, custo, op):
        self.actual = actual
        self.objective = objective
        self.custo = custo
        self.operator = op
    
    def sucessors(self):
        sucessors = []

        for possibilitie in Map.area[self.actual]:
            custo = possibilitie[0]
            city = possibilitie[1]
            sucessors.append(Map(actual=city, objective=self.objective, custo=custo, op=f"to {city}"))

        return sucessors
    
    def is_goal(self):
        return (self.actual == self.objective)
    
    def description(self):
        return "City Problem"
    
    def h(self):
        return int(Map.g.edges[self.actual, self.objective]['distance'])
        # return int(Map.g[self.actual][self.objective]["distance"])
        # return 0
        # return 1
        # print(int(Map.g[self.actual][self.objective]["distance"]))

    def cost(self):
        #return the cost to get at city "city"
        return self.cost_value
    
    def print(self):
        return str(self.operator)
    
    def env(self):
        return self.city
        #return self.city+"#"+str(self.cost())

    def h(self):
        return int(Map.g.edges[self.city,self.goal]['distance'])
        #return random.randint(1,10)
        #return 1

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
        return str(self.actual)

    @staticmethod
    def createHeuristics():
        #
        # O arquvo MapHeuristics.csv considera apenas os objetivos "o" e "x"
        # TODO modificar o arquivo para considerar todas as cidades. talvez modificar
        # a estrutura do arquivo considerando uma estrutura otimizada
        #
        Map.g = nx.Graph()
        f = csv.reader(open("src/data/MapHeuristics.csv","r"))
        for row in f:
            Map.g.add_edge(row[0], row[1], distance = row[2])

   
def main():
    initial_city = "i"
    final_city = "x"    
    # Map.createArea()
    # print('Busca de Custo Uniforme')
    # state = Map(actual=initial_city, objective=final_city, custo=0, op="")
    # algorithm = BuscaCustoUniforme()
    # result = algorithm.search(state)
    # if result != None:
    #     print('Achou!')
    #     print(result.show_path())
    # else:
    #     print('Nao achou solucao')

    
    Map.createArea()
    Map.createHeuristics()

    print('Busca por algoritmo A*: sair de i e chegar em x')
    state = Map(actual=initial_city, objective=final_city, custo=0, op='')
    algorithm = AEstrela()
    #algorithm = BuscaCustoUniforme()
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
   
    Map.createArea()
    Map.createHeuristics()

    print('Busca Gananciosa')
    state = Map(actual=initial_city, objective=final_city, custo=0, op='')
    algorithm = BuscaGananciosa()
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
    
if __name__ == '__main__':
    main()

'''
Implementações
Implemente um agente, usando o algoritmo de busca em largura, para encontrar um caminho entre a cidade i e o.

Perguntas:

Qual foi o tempo de processamento até a implementação encontrar uma solução?
A árvore de busca gerada é "inteligente"?
A solução encontrada é ótima?
Usando a mesma implementação, encontre um caminho entre a cidade b e o.

Perguntas:

Qual foi o tempo de processamento até a implementação encontrar uma solução?
A árvore de busca gerada é "inteligente"?
A solução encontrada é ótima?
Usando o algoritmo de custo uniforme
Utilize o algoritmo de custo uniforme para encontrar uma solução para os problemas abaixo:

da cidade i para a cidade o
da cidade b para a cidade o
da cidade i para a cidade x
Perguntas:

Qual foi o tempo de processamento até a implementação encontrar uma solução?
A árvore de busca gerada é "inteligente"?
A solução encontrada é ótima?
'''
