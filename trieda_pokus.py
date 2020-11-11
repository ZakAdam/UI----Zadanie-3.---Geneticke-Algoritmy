import random
import gen_class
from tabulate import tabulate
from copy import copy, deepcopy

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


def naraz(gen, mapa, riadky, stlpce):
    smer = gen.get_smer()
    if smer == "Up" or smer == "Down":
        if smer == "Up":
            suradnice = gen.get_posun()
            if suradnice[0] < (stlpce - 1) and mapa[suradnice[1] + 1][suradnice[0] + 1] == 0:
                gen.set_smer("Right")
                gen.set_y_posun(1)
                return 1
            elif suradnice[0] > 0 and mapa[suradnice[1] + 1][suradnice[0] - 1] == 0:
                gen.set_smer("Left")
                gen.set_y_posun(1)
                return 1

        else:
            suradnice = gen.get_posun()
            if 0 < suradnice[0] and mapa[suradnice[1] - 1][suradnice[0] - 1] == 0:
                gen.set_smer("Left")
                gen.set_y_posun(-1)
                return 1
            elif suradnice[0] < (stlpce - 1) and mapa[suradnice[1] - 1][suradnice[0] + 1] == 0:
                gen.set_smer("Right")
                gen.set_y_posun(-1)
                return 1
        if suradnice[0] == (stlpce - 1) or suradnice[0] == 0:  # pripad, že je to bod na hranici
            return 2

    else:
        if smer == "Right":
            suradnice = gen.get_posun()
            if 0 < suradnice[1] < (riadky - 1) and mapa[suradnice[1] - 1][suradnice[0] - 1] == 0:
                gen.set_smer("Up")
                gen.set_x_posun(-1)
                return 1
            else:
                if 0 < suradnice[1] < (riadky - 1) and mapa[suradnice[1] + 1][suradnice[0] - 1] == 0:
                    gen.set_smer("Down")
                    gen.set_x_posun(-1)
                    return 1

        else:
            suradnice = gen.get_posun()
            if suradnice[1] < (riadky - 1) and mapa[suradnice[1] + 1][suradnice[0] + 1] == 0:   #Left - Left
                gen.set_smer("Down")
                gen.set_x_posun(1)
                return 1
            else:
                if 0 < suradnice[1] and mapa[suradnice[1] - 1][suradnice[0] + 1] == 0:
                    gen.set_smer("Up")
                    gen.set_x_posun(1)
                    return 1
        if suradnice[1] == (riadky - 1) or suradnice[1] == 0:            # pripad, že je to bod na hranici
            return 2

    return 3


def posun(gen):
    if gen.get_smer() == "Up":
        gen.set_y_posun(-1)
    elif gen.get_smer() == "Down":
        gen.set_y_posun(1)
    elif gen.get_smer() == "Right":
        gen.set_x_posun(1)
    elif gen.get_smer() == "Left":
        gen.set_x_posun(-1)


def check(gen, riadky, stlpce):
    if 0 <= gen.x_posun < stlpce and 0 <= gen.y_posun < riadky:
        return True
    return False


def hrabanie(population, riadky, stlpce, fitness_zoznam):
    new_mapa = deepcopy(mapa)
    koniec = False
    for i in population:
        gen = gen_class.Gene(i, riadky, stlpce)
        suradnice = gen.get_suradnice()
        if new_mapa[suradnice[1]][suradnice[0]] != 0:
            continue
        new_mapa[suradnice[1]][suradnice[0]] = i
        posun(gen)
        suradnice = gen.get_posun()
        while check(gen, riadky, stlpce):
            if new_mapa[suradnice[1]][suradnice[0]] != 0:
                value = naraz(gen, new_mapa, riadky, stlpce)
                if value == 3:
                    print("Tento gen nenasiel cestu von :(  --> " + str(i))
                    koniec = True
                    break
                elif value == 1:
                    posun(gen)
                    suradnice = gen.get_posun()
                else:
                    break
            new_mapa[suradnice[1]][suradnice[0]] = i
            posun(gen)
            suradnice = gen.get_posun()
        if koniec:
            break

    fitness = 0
    for i in range(0, riadky):
        for j in range(0, stlpce):
            if new_mapa[i][j] != 0:
                fitness += 1
    print("Fitness danho jedinca je: " + str(fitness))
    if fitness == riadky * stlpce:
        print(tabulate(new_mapa))
        print("NASIEL SI ODPOVED!!!")
        exit(0)
    fitness_zoznam.append(fitness)
    print(tabulate(new_mapa))


def main():
    riadky = len(mapa)
    stlpce = len(mapa[0])
    pocet_jedincov = 20
    fitness_zoznam = []
    print(riadky)
    print(stlpce)
    number_of_genes = riadky + stlpce  # TODO add aj geny pre kamene
    genes = []
    for j in range(0, pocet_jedincov):
        for i in range(1, number_of_genes * 2 + 1):
            genes.append(i)
        population = random.sample(genes, number_of_genes)
        print(population)
        hrabanie(population, riadky, stlpce, fitness_zoznam)

    max = fitness_zoznam[0]
    min = fitness_zoznam[0]
    sum = 0
    for value in fitness_zoznam:
        if value > max:
            max = value
        elif value < min:
            min = value
        sum += value

    print(fitness_zoznam)
    print("\nMax. prvok: " + str(max) + " Min. prvok " + str(min) + " primer " + str(sum/pocet_jedincov))


if __name__ == "__main__":
    main()

