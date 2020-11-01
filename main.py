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


def vypis(sachovnica, riadky, stlpce):
    for i in range(riadky):
        for j in range(stlpce):
            print(sachovnica[i][j], end=" ")
        print("\n")


def posun_fitness(population, riadky, stlpce):
    new_mapa = mapa.copy()
    for i in population:
        if i < 10:
            for j in range(0, stlpce):
                if new_mapa[i][j] == 0:
                    new_mapa[i][j] = i
                else:
                    break
        if i > 9:
            for j in range(0, riadky):
                if new_mapa[9-j][i-10] == 0:
                    new_mapa[9-j][i-10] = i
                else:
                    break
    vypis(new_mapa, riadky, stlpce)


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
