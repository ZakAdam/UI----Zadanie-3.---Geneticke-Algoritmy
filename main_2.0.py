import naraz
import gen_class
from tabulate import tabulate
from copy import deepcopy
import random


with open("mapa.txt") as f:
    mapa = [[int(num) for num in line.split(",")] for line in f]
    riadky = len(mapa)
    stlpce = len(mapa[0])
    kamene = 0
    for h in range(0, riadky):
        for p in range(0, stlpce):
            if mapa[h][p] < 0:
                kamene += 1
    print(kamene)
    pocet_genov = riadky + stlpce + kamene


with open("config_file.txt") as file:
    zaznamy = []
    for line in file:
        riadok = line.strip()
        g = 1
        cislo = riadok[0]
        while riadok[g].isdigit():
            cislo = str(cislo) + str(riadok[g])
            g += 1
        print(cislo)
        zaznamy.append(cislo)

    print("------------------------------------------------")
    print(zaznamy)
    pocet_generacii = int(zaznamy[0])
    pocet_jedincov = int(zaznamy[1])
    typ_krizenia = int(zaznamy[2])
    vyber_rodicov = int(zaznamy[3])
    cislo = "0." + zaznamy[4]
    mutation_chance = float(cislo)
    typ_mutacie = int(zaznamy[5])
    cislo = "0." + zaznamy[6]
    swap_rate = float(cislo)
    cislo = "0." + zaznamy[7]
    mutation_rate = float(cislo)
    cislo = "0." + zaznamy[8]
    otocenie = float(cislo)
    print("------------------------------------------------")


def turnaj(zoznam_fitness):
    first = random.randint(0, len(zoznam_fitness) - 1)
    second = random.randint(0, len(zoznam_fitness) - 1)

    if zoznam_fitness[first] > zoznam_fitness[second]:
        return first
    else:
        return second


def ruleta(zoznam_fitness):
    suc = sum(zoznam_fitness)
    hranica = suc * random.random()
    sucet = 0
    for i in range(0, len(zoznam_fitness)):
        sucet = sucet + zoznam_fitness[i]
        if sucet > hranica:
            return i
    return random.randint(0, len(zoznam_fitness) - 1)


def nova_krv(new_population, pozicie, j):
    populacia = []
    for _ in range(0, pocet_genov):
        start = random.randint(1, pozicie)
        populacia.append(gen_class.Gene(start, riadky, stlpce, random.random()))
    new_population[j] = populacia


def krizenie(prvy_rodic, druhy_rodic):
    if typ_krizenia == 1:
        split_point = random.randint(1, len(prvy_rodic) - 1)
        prve_pomocne = druhy_rodic[split_point:]
        druhe_pomocne = prvy_rodic[split_point:]

        prve_dieta = prvy_rodic[:split_point] + prve_pomocne
        druhe_dieta = druhy_rodic[:split_point] + druhe_pomocne

        return prve_dieta, druhe_dieta

    else:
        split_point1 = random.randint(1, len(prvy_rodic) - 1)
        split_point2 = random.randint(1, len(prvy_rodic) - 1)
        if split_point1 > split_point2:
            split_point1, split_point2 = split_point2, split_point1
        prve_dieta = []
        druhe_dieta = []
        for i in range(0, len(prvy_rodic)):
            if i < split_point1 or i > split_point2:
                prve_dieta.append(prvy_rodic[i])
                druhe_dieta.append(druhy_rodic[i])
            else:
                prve_dieta.append(druhy_rodic[i])
                druhe_dieta.append(prvy_rodic[i])
        #prve_dieta.append(gen_class.Gene(random.randint(1, 44), 10, 12, random.random()))
        #druhe_dieta.append(gen_class.Gene(random.randint(1, 44), 10, 12, random.random()))
        return prve_dieta, druhe_dieta


def mutation(jedinec, obvod):
    for i in range(0, len(jedinec)):
        nahoda = random.random()
        if nahoda < mutation_rate:
            nahrada = random.randint(1, obvod)
            sanca = random.random()
            new = gen_class.Gene(nahrada, riadky, stlpce, sanca)
            jedinec[i] = new

        if nahoda < swap_rate:
            druhy = random.randint(0, len(jedinec) - 1)
            jedinec[i], jedinec[druhy] = jedinec[druhy], jedinec[i]

        if nahoda < otocenie:
            jedinec[i].odbocenie = not jedinec[i].odbocenie
    return jedinec


def mutation_2(jedinec, obvod):
    nahoda = random.random()
    pozicia = random.randint(0, len(jedinec) - 1)
    if nahoda < mutation_rate:
        nahrada = random.randint(0, obvod)
        sanca = random.random()
        new = gen_class.Gene(nahrada, riadky, stlpce, sanca)
        jedinec[pozicia] = new

    if nahoda < swap_rate:
        druhy = random.randint(0, len(jedinec) - 1)
        jedinec[pozicia], jedinec[druhy] = jedinec[druhy], jedinec[pozicia]

    if nahoda < otocenie:
        jedinec[pozicia].odbocenie = not jedinec[pozicia].odbocenie
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


def check(gen):
    if 0 <= gen.x_posun < stlpce and 0 <= gen.y_posun < riadky:
        return True
    return False


def hrabanie(population, fitness_zoznam, volanie):
    new_mapa = deepcopy(mapa)
    for i in range(0, len(population)):
        gen = population[i]
        if volanie == 2:
            gen.set_smer(gen.povodny_smer)
            gen.reset_posun(gen.x, gen.y)
        suradnice = gen.get_suradnice()
        if new_mapa[suradnice[1]][suradnice[0]] != 0:
            continue
        new_mapa[suradnice[1]][suradnice[0]] = gen.start
        posun(gen)
        suradnice = gen.get_posun()
        while check(gen):
            if new_mapa[suradnice[1]][suradnice[0]] != 0:
                value = naraz.naraz(gen, new_mapa, riadky, stlpce)
                if value == 3:
                    new_mapa = naraz.backtracking(new_mapa, gen.start, riadky, stlpce)
                    break
                elif value == 1:
                    posun(gen)
                    suradnice = gen.get_posun()
                else:
                    break
            new_mapa[suradnice[1]][suradnice[0]] = gen.start
            posun(gen)
            suradnice = gen.get_posun()

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
    fitness_zoznam = []
    zoznam_objektov = {}
    number_of_genes = riadky + stlpce
    genes = []
    for i in range(1, number_of_genes * 2 + 1):
        genes.append(i)
    for j in range(0, pocet_jedincov):
        population = random.sample(genes, pocet_genov)
        tmp = []
        for l in population:
            sanca = random.random()
            tmp.append(gen_class.Gene(l, riadky, stlpce, sanca))
        zoznam_objektov[j] = hrabanie(tmp, fitness_zoznam, 1)

    maximum = fitness_zoznam[0]
    minimum = fitness_zoznam[0]
    sumacia = 0
    for value in fitness_zoznam:
        if value > maximum:
            maximum = value
        elif value < minimum:
            minimum = value
        sumacia += value

    print(fitness_zoznam)
    print("\nMax. prvok: " + str(maximum) + " Min. prvok " + str(minimum) + " primer " + str(sumacia/pocet_jedincov))

    new_population = {}


##########################################################################################################
    k = 1
    generacia = 1
    while k <= pocet_generacii:
        new_population.clear()
        j = 0
        for i in range(0, int(pocet_jedincov / 2) - 1):
            if vyber_rodicov == 1:
                prvy_rodic = turnaj(fitness_zoznam)
                druhy_rodic = turnaj(fitness_zoznam)

            else:
                prvy_rodic = ruleta(fitness_zoznam)
                druhy_rodic = ruleta(fitness_zoznam)

            deti = krizenie(zoznam_objektov.get(prvy_rodic), zoznam_objektov.get(druhy_rodic))
            new_population[j] = deti[0]
            new_population[j + 1] = deti[1]
            j += 2

        nova_krv(new_population, number_of_genes * 2, j)

        zoznam_objektov.clear()
        fitness_zoznam.clear()
        j = 0
        for key in new_population:
            zoznam_objektov[j] = hrabanie(new_population[key], fitness_zoznam, 2)
            sanca = random.random()
            if sanca < mutation_chance:
                if typ_mutacie == 1:
                    zoznam_objektov[j] = mutation_2(zoznam_objektov[j], len(genes))
                else:
                    zoznam_objektov[j] = mutation(zoznam_objektov[j], len(genes))
            j += 1

        maximum = fitness_zoznam[0]
        minimum = fitness_zoznam[0]
        sumacia = 0
        for value in fitness_zoznam:
            if value > maximum:
                maximum = value
            elif value < minimum:
                minimum = value
            sumacia += value

        print("\nGenerácia č.: " + str(generacia) + " Max. prvok: " + str(maximum) + " Min. prvok " + str(minimum) +
              " primer " + str(sumacia / pocet_jedincov))
        print(fitness_zoznam)

        if k == pocet_generacii:
            dalej = input("\n\nChcete pokracovat dalsich " + str(pocet_generacii) + " generacii?")
            if dalej == "1":
                k = 0
            else:
                exit(0)
        k += 1
        generacia += 1


if __name__ == "__main__":
    main()

