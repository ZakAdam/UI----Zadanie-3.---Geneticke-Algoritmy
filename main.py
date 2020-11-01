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


def RaL_posun(pole, riadky, stlpce, y, x, cislo):
    if cislo != (riadky + stlpce - 1) and pole[y][x + 1] == 0:
        for i in range(x + 1, stlpce):
            if pole[y][i] == 0:
                pole[y][i] = 88
            else:
                break
    elif cislo != 10 and pole[y][x - 1] == 0:
        for i in range(x - 1, 0):
            if pole[y][i] == 0:
                pole[y][i] = i
            else:
                break


def posun_fitness(population, riadky, stlpce):
    new_mapa = mapa.copy()
    for i in population:
        if i < riadky:
            for j in range(0, stlpce):
                if new_mapa[i][j] == 0:
                    new_mapa[i][j] = i
                else:
                    break
        if i > 9:
            for j in range(0, riadky):
                if new_mapa[9 - j][i - 10] == 0:
                    new_mapa[9 - j][i - 10] = i
                else:
                    """
                    if i != 21 and new_mapa[riadky - j][i - 9] == 0:
                        print(i, j)
                        for k in range(i - 9, stlpce):
                            print("v cykle je " + str(9 - j) + ", ," + str(k))
                            if new_mapa[riadky - j][k] == 0:
                                new_mapa[riadky - j][k] = i
                            else:
                                break
                        break
                    else:
                        break
                    """
                    RaL_posun(new_mapa, riadky, stlpce, riadky - j, i - 10, i)
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
