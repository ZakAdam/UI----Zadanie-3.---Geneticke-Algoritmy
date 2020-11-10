import random
from tabulate import tabulate

mapa = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

"""
def check(poloha):
    if 0 <= poloha < riadky and 0 < poloha < stlpce:
"""


class Gene:                                                     #TODO pozor na ten 0ty riadok pre Y a X
    def __init__(self, start):
        self.start = start
        if riadky < start <= stlpce + riadky:
            self.smer = "Up"
            self.x = start - riadky - 1
            self.y = riadky - 1
        elif riadky + stlpce + riadky < start <= riadky + stlpce + riadky + stlpce:
            self.smer = "Down"
            self.x = stlpce - (start - riadky*2 - stlpce)
            self.y = 0
        elif start <= riadky:
            self.smer = "Right"
            self.x = 0
            self.y = start - 1
        elif riadky + stlpce < start <= riadky + stlpce + riadky:
            self.smer = "Left"
            self.x = stlpce - 1
            self.y = riadky - (start - riadky - stlpce)
        else:
            self.smer = "Noneeeee"
            self.x = 0
            self.y = 0

    def get_smer(self):
        return self.smer

    def get_suradnice(self):
        return self.x, self.y


def hrabanie(population, riadok, stlpec):
    new_mapa = mapa
    print("druha stena --> " + str(riadok + stlpec))
    for i in population:
        gen = Gene(i)
        suradnice = gen.get_suradnice()
        print(str(i) + "  ---  " + gen.get_smer() + "  ---  " + str(suradnice[0]) + " , " + str(suradnice[1]))
        new_mapa[suradnice[1]][suradnice[0]] = i

    print(tabulate(new_mapa))


if __name__ == "__main__":
    riadky = len(mapa)
    stlpce = len(mapa[0])
    print(riadky)
    print(stlpce)
    number_of_genes = riadky + stlpce  # TODO add aj geny pre kamene
    genes = []
    for i in range(0, (riadky + stlpce) * 2 + 1):
        genes.append(i)
    population = random.sample(genes, number_of_genes)
    print(population)
    hrabanie(population, riadky, stlpce)

