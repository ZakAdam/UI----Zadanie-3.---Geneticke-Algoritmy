import naraz
import gen_class
from tabulate import tabulate
from copy import deepcopy
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


def turnaj(zoznam_fitness):
    first = random.randint(0, len(zoznam_fitness) - 1)
    second = random.randint(0, len(zoznam_fitness) - 1)

    if zoznam_fitness[first] > zoznam_fitness[second]:
        print("Prvy je: " + str(zoznam_fitness[first]) + " Druhy je: " + str(zoznam_fitness[second]) + " vrateny je prvy")
        return first
    else:
        print("Prvy je: " + str(zoznam_fitness[first]) + " Druhy je: " + str(zoznam_fitness[second]) + " vrateny je druhyyyyyyy")
        return second


def krizenie(prvy_rodic, druhy_rodic):
    prve_pomocne = druhy_rodic[len(druhy_rodic)//2:]
    druhe_pomocne = prvy_rodic[len(prvy_rodic)//2:]

    prve_dieta = prvy_rodic[:len(prvy_rodic) // 2] + prve_pomocne
    druhe_dieta = druhy_rodic[:len(druhy_rodic) // 2] + druhe_pomocne

    return prve_dieta, druhe_dieta

"""
def naraz(gen, mapa, riadky, stlpce):
    smer = gen.get_smer()
    if smer == "Up" or smer == "Down":
        if smer == "Up":
            suradnice = gen.get_posun()
            if suradnice[0] < (stlpce - 1) and mapa[suradnice[1] + 1][suradnice[0] + 1] == 0:
                gen.set_smer("Right")
                gen.set_y_posun(1)
                return 1
            if suradnice[0] > 0 and mapa[suradnice[1] + 1][suradnice[0] - 1] == 0:
                gen.set_smer("Left")
                gen.set_y_posun(1)
                return 1
            if gen.y_posun - 1 == riadky - 1:
                return 2

        else:
            suradnice = gen.get_posun()
            if 0 < suradnice[0] and mapa[suradnice[1] - 1][suradnice[0] - 1] == 0:
                gen.set_smer("Left")
                gen.set_y_posun(-1)
                return 1
            if suradnice[0] < (stlpce - 1) and mapa[suradnice[1] - 1][suradnice[0] + 1] == 0:
                gen.set_smer("Right")
                gen.set_y_posun(-1)
                return 1
            if gen.y_posun - 1 == 0:
                return 2
        if suradnice[0] == (stlpce - 1) or suradnice[0] == 0:  # pripad, že je to bod na hranici
            return 2

    else:
        if smer == "Right":
            suradnice = gen.get_posun()
            if 0 < suradnice[1] < (riadky - 1) and mapa[suradnice[1] - 1][suradnice[0] - 1] == 0:
                gen.set_smer("Up")
                gen.set_x_posun(-1)
                return 1
            if 0 < suradnice[1] < (riadky - 1) and mapa[suradnice[1] + 1][suradnice[0] - 1] == 0:
                gen.set_smer("Down")
                gen.set_x_posun(-1)
                return 1
            if gen.x_posun - 1 == 0:
                return 2

        else:
            suradnice = gen.get_posun()
            if suradnice[1] < (riadky - 1) and mapa[suradnice[1] + 1][suradnice[0] + 1] == 0:   #Left - Left
                gen.set_smer("Down")
                gen.set_x_posun(1)
                return 1
            if 0 < suradnice[1] and mapa[suradnice[1] - 1][suradnice[0] + 1] == 0:
                gen.set_smer("Up")
                gen.set_x_posun(1)
                return 1
            if gen.x_posun - 1 == stlpce - 1:                      # hranicny stav
                return 2
        if suradnice[1] == (riadky - 1) or suradnice[1] == 0:   # pripad, že je to bod na hranici
            return 2

    return 3
"""


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
    for i in range(0, len(population)):
        gen = population[i]
        print(gen.start)
        if gen.get_odbocenie():
            print("Looool")
        suradnice = gen.get_suradnice()
        if new_mapa[suradnice[1]][suradnice[0]] != 0:
            continue
        new_mapa[suradnice[1]][suradnice[0]] = gen.start
        posun(gen)
        suradnice = gen.get_posun()
        while check(gen, riadky, stlpce):
            if new_mapa[suradnice[1]][suradnice[0]] != 0:
                value = naraz.naraz(gen, new_mapa, riadky, stlpce)
                if value == 3:
                    print("Tento gen nenasiel cestu von :(  --> " + str(gen.start))
                    print("Suradnice su: " + str(gen.x) + str(gen.y))
                    koniec = True
                    break
                elif value == 1:
                    posun(gen)
                    suradnice = gen.get_posun()
                else:
                    break
            new_mapa[suradnice[1]][suradnice[0]] = gen.start
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
    return population


def hrabanie_2(population, riadky, stlpce, fitness_zoznam):
    new_mapa = deepcopy(mapa)
    koniec = False
    for i in range(0, len(population)):
        gen = population[i]
        gen.set_smer(gen.povodny_smer)
        gen.reset_posun(gen.x, gen.y)
        suradnice = gen.get_suradnice()
        print(suradnice)
        print(gen.get_posun())
        if new_mapa[suradnice[1]][suradnice[0]] != 0:
            continue
        new_mapa[suradnice[1]][suradnice[0]] = gen.start
        posun(gen)
        suradnice = gen.get_posun()
        print(suradnice)
        while check(gen, riadky, stlpce):
            print("mo")
            if new_mapa[suradnice[1]][suradnice[0]] != 0:
                value = naraz.naraz(gen, new_mapa, riadky, stlpce)
                if value == 3:
                    print("Tento gen nenasiel cestu von :(  --> " + str(gen.start))
                    koniec = True
                    break
                elif value == 1:
                    posun(gen)
                    suradnice = gen.get_posun()
                else:
                    break
            new_mapa[suradnice[1]][suradnice[0]] = gen.start
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
    print(population)
    return population


def main():
    riadky = len(mapa)
    stlpce = len(mapa[0])
    pocet_jedincov = 20
    pocet_generacii = 100
    fitness_zoznam = []
    zoznam_objektov = {}
    print(riadky)
    print(stlpce)
    number_of_genes = riadky + stlpce  # TODO add aj geny pre kamene
    genes = []
    for i in range(1, number_of_genes * 2 + 1):
        genes.append(i)
    for j in range(0, pocet_jedincov):
        population = random.sample(genes, number_of_genes)
        tmp = []
        for l in population:
            sanca = random.random()
            print(sanca)
            tmp.append(gen_class.Gene(l, riadky, stlpce, sanca))
        print(tmp)
        zoznam_objektov[j] = hrabanie(tmp, riadky, stlpce, fitness_zoznam)

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

    prvy_rodic = turnaj(fitness_zoznam)
    print(prvy_rodic)
    druhy_rodic = turnaj(fitness_zoznam)
    print(druhy_rodic)
    print(zoznam_objektov)
    print(zoznam_objektov.get(prvy_rodic))
    print(zoznam_objektov.get(druhy_rodic))
    deti = krizenie(zoznam_objektov.get(prvy_rodic), zoznam_objektov.get(druhy_rodic))
    print(deti[0])
    print(deti[1])

    new_population = {}
    j = 0
    for i in range(0, int(pocet_jedincov/2)):
        prvy_rodic = turnaj(fitness_zoznam)
        druhy_rodic = turnaj(fitness_zoznam)
        deti = krizenie(zoznam_objektov.get(prvy_rodic), zoznam_objektov.get(druhy_rodic))
        new_population[j] = deti[0]
        new_population[j+1] = (deti[1])
        j += 2


    print(new_population.get(0)[1].get_suradnice())
    hrabanie_2(new_population[0], riadky, stlpce, fitness_zoznam)

    """
    for i in range(1, pocet_generacii):
        

        for j in range(0, pocet_jedincov):
            zoznam_objektov[j] = hrabanie(population, riadky, stlpce, fitness_zoznam)
    """


if __name__ == "__main__":
    main()

