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


def HaD_posun(pole, riadky, stlpce, y, x, cislo):
    if cislo != riadky - 1 and pole[y + 1][x] == 0:
        for i in range(y + 1, riadky):
            if pole[i][x] == 0:
                pole[i][x] = cislo
            else:
                break
    elif cislo != 0 and pole[y - 1][x] == 0:
        for i in range(1, (y + 1)):
            if pole[y - i][x] == 0:
                pole[y - i][x] = cislo
            else:
                break
    else:
        return


def RaL_posun(pole, riadky, stlpce, y, x, cislo):
    print(y)
    if cislo != (riadky + stlpce - 1) and pole[y][x + 1] == 0:
        for i in range(x + 1, stlpce):
            if pole[y][i] == 0:
                pole[y][i] = cislo
            else:
                HaD_posun(pole, riadky, stlpce, y, i - 1, cislo)
                break
    elif cislo != 10 and pole[y][x - 1] == 0:
        for i in range(0, x - 1):
            if pole[y][x - i] == 0:
                pole[y][x - i] = -cislo
            else:
                HaD_posun(pole, riadky, stlpce, y, x - i, cislo)
                break
    else:
        return


def posun_fitness(population, riadky, stlpce):
    new_mapa = mapa.copy()
    for i in population:
        if i < riadky:
            for j in range(0, stlpce):
                if new_mapa[i][j] == 0:
                    new_mapa[i][j] = i
                else:
                    HaD_posun(new_mapa, riadky, stlpce, i, j - 1, i)
                    break
        if i > 9:
            for j in range(1, (riadky + 1)):
                if new_mapa[riadky - j][i - 10] == 0:
                    new_mapa[riadky - j][i - 10] = i
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
                    print(i, j)
                    if j != 1:
                        RaL_posun(new_mapa, riadky, stlpce, riadky - j + 1, i - 10, i)
                    break

    print(tabulate(new_mapa))


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
