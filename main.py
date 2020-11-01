import random

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


def posun_fitness(population, riadky, stlpce):
    new_mapa = mapa.copy()
    for i in population:
        if i < 10:
            for j in range(0, stlpce):
                if new_mapa[i][j] == 0:
                    new_mapa[i][j] = i
                else:
                    break
    print(new_mapa)


if __name__ == "__main__":
    riadky = len(mapa)
    stlpce = len(mapa[0])
    print(riadky)
    print(stlpce)
    number_of_genes = riadky + stlpce  # TODO add aj geny pre kamene
    genes = []
    for i in range(0, number_of_genes):
        genes.append(i)
    population = random.sample(genes, 20)
    print(population)
    posun_fitness(population, riadky, stlpce)
