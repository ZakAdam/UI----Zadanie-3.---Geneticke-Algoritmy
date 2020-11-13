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
        return first
    else:
        return second


def krizenie(prvy_rodic, druhy_rodic):
    split_point = random.randint(1, len(prvy_rodic) - 1)
    prve_pomocne = druhy_rodic[split_point:]
    druhe_pomocne = prvy_rodic[split_point:]

    prve_dieta = prvy_rodic[:split_point] + prve_pomocne
    druhe_dieta = druhy_rodic[:split_point] + druhe_pomocne

    return prve_dieta, druhe_dieta


def mutation(jedinec, mutation_rate, obvod, riadky, stlpce):
    for i in range(0, len(jedinec)):
        if random.random() < mutation_rate:
            nahrada = random.randint(0, obvod)
            sanca = random.random()
            new = gen_class.Gene(nahrada, riadky, stlpce, sanca)
            jedinec[i] = new
    return jedinec


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
        if new_mapa[suradnice[1]][suradnice[0]] != 0:
            continue
        new_mapa[suradnice[1]][suradnice[0]] = gen.start
        posun(gen)
        suradnice = gen.get_posun()
        while check(gen, riadky, stlpce):
            if new_mapa[suradnice[1]][suradnice[0]] != 0:
                value = naraz.naraz(gen, new_mapa, riadky, stlpce)
                if value == 3:
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
    if fitness == riadky * stlpce:
        print(tabulate(new_mapa))
        print("NASIEL SI ODPOVED!!!")
        exit(0)
    fitness_zoznam.append(fitness)
    return population


def main():
    riadky = len(mapa)
    stlpce = len(mapa[0])
    pocet_jedincov = 20
    pocet_generacii = 100
    mutation_chance = 0.3
    fitness_zoznam = []
    zoznam_objektov = {}
    print(riadky)
    print(stlpce)
    number_of_genes = riadky + stlpce  # TODO add aj geny pre kamene
    genes = []
    for i in range(1, number_of_genes * 2 + 1):
        genes.append(i)
    for j in range(0, pocet_jedincov):
        #population = random.sample(genes, number_of_genes)
        population = random.sample(genes, 30)
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

    new_population = {}

    for k in range(1, pocet_generacii):
        new_population.clear()
        #new_population = {}
        j = 0
        for i in range(0, int(pocet_jedincov / 2)):
            prvy_rodic = turnaj(fitness_zoznam)
            druhy_rodic = turnaj(fitness_zoznam)
            deti = krizenie(zoznam_objektov.get(prvy_rodic), zoznam_objektov.get(druhy_rodic))
            new_population[j] = deti[0]
            new_population[j + 1] = (deti[1])
            j += 2

        zoznam_objektov.clear()
        fitness_zoznam.clear()
        j = 0
        for key in new_population:
            zoznam_objektov[j] = hrabanie_2(new_population[key], riadky, stlpce, fitness_zoznam)
            sanca = random.random()
            if sanca < mutation_chance:
                #print(zoznam_objektov[j])
                zoznam_objektov[j] = mutation(zoznam_objektov[j], 0.15, len(genes), riadky, stlpce)
                #print(zoznam_objektov[j])
            j += 1



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
        print("\nGenerácia č.: " + str(k) + " Max. prvok: " + str(max) + " Min. prvok " + str(min) + " primer " + str(
            sum / pocet_jedincov))


if __name__ == "__main__":
    main()

