import naraz
import gen_class
from tabulate import tabulate
from copy import deepcopy                                        # na vytvárenie kópie 2D poľa
import random


with open("mapa.txt") as f:                                     # načítanie mapy a počet kamenov
    mapa = [[int(num) for num in line.split(",")] for line in f]
    riadky = len(mapa)
    stlpce = len(mapa[0])
    kamene = 0
    for h in range(0, riadky):                                  # zistí počet kamoňov
        for p in range(0, stlpce):
            if mapa[h][p] < 0:
                kamene += 1
    pocet_genov = riadky + stlpce + kamene                      # globalna premenná pre počet génov


with open("config_file.txt") as file:                           # načítanie dát z konfiguračného suboru
    zaznamy = []
    for line in file:
        riadok = line.strip()
        g = 1
        cislo = riadok[0]
        while riadok[g].isdigit():
            cislo = str(cislo) + str(riadok[g])
            g += 1
        zaznamy.append(cislo)

    pocet_generacii = int(zaznamy[0])                           # globálne premenné pre jednotlivé údaje
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


def turnaj(zoznam_fitness):                                     # funkcia turnaj pre túto metódu výberu rodičov
    first = random.randint(0, len(zoznam_fitness) - 1)          # prvý náhodne zvolený jedinec
    second = random.randint(0, len(zoznam_fitness) - 1)         # druhý náhodne zvolený jedinec

    if zoznam_fitness[first] > zoznam_fitness[second]:          # zistím, ktorý je väčší
        return first                                            # a ten vrátim
    else:
        return second                                           # alebo ten druhý


def ruleta(zoznam_fitness):                                     # funkcia na výber podla metody ruleta
    suc = sum(zoznam_fitness)                                   # spočítam celkovú sumu fitness hodnôt
    hranica = suc * random.random()                             # vyberiem náhodnú hodnotu
    sucet = 0
    for i in range(0, len(zoznam_fitness)):                     # prechádzam celé pole fitness
        sucet = sucet + zoznam_fitness[i]                       # opat sčitujem sumu fitness
        if sucet > hranica:                                     # ak suma prekročí hore zvolenú hranicu
            return i                                            # tak vrát adresu hodnoty pri ktorej sa to stalo
    return random.randint(0, len(zoznam_fitness) - 1)           # ak sa nenašla žiadna v poli vrát nejakú inu náhodnu


def nova_krv(new_population, pozicie, j):                       # funkcia na vytvorenie novej krvy
    populacia = []                                              # vytvorim noveho jedinca
    for _ in range(0, pocet_genov):                             # v cykle doňho vložím nové gény
        start = random.randint(1, pozicie)
        populacia.append(gen_class.Gene(start, riadky, stlpce, random.random()))
    new_population[j] = populacia                               # túto novú populáciu vložím do generácie


def krizenie(prvy_rodic, druhy_rodic):                          # funkcia na vytváranie nových detí
    if typ_krizenia == 1:                                       # zvolený typ križenia je jednobodový
        split_point = random.randint(1, len(prvy_rodic) - 1)    # vyberia sa bod delenia, náhodne
        prve_pomocne = druhy_rodic[split_point:]                # do pomocnych premenných sa zapíše pole za bodom
        druhe_pomocne = prvy_rodic[split_point:]                # to isté, z druhého pola

        prve_dieta = prvy_rodic[:split_point] + prve_pomocne    # do dietata1 sa vloží rodic1 po bod a rodic2 za bodom
        druhe_dieta = druhy_rodic[:split_point] + druhe_pomocne # analogicky

        return prve_dieta, druhe_dieta                          # vrátim vytvorené deti

    else:                                                       # ak je typ kríženia dvojbodový
        split_point1 = random.randint(1, len(prvy_rodic) - 1)   # vybereiem dva body delenia
        split_point2 = random.randint(1, len(prvy_rodic) - 1)   # druhý bod delenia
        if split_point1 > split_point2:                         # skontrolujem ich poradie
            split_point1, split_point2 = split_point2, split_point1  # ak je zle, tak ho vymenim
        prve_dieta = []                                         # vytvorim prve dieta
        druhe_dieta = []                                        # vytvorim druhe dieta
        for i in range(0, len(prvy_rodic)):                     # prejdem celých rodičov
            if i < split_point1 or i > split_point2:            # ak som pred bodom1 alebo za bodom2
                prve_dieta.append(prvy_rodic[i])                # do dietata1 dam rodica1
                druhe_dieta.append(druhy_rodic[i])              # to iste pre dieta2
            else:                                               # ak som za bodom1 a pred bodom2
                prve_dieta.append(druhy_rodic[i])               # tak do dietata1 dam rodica2
                druhe_dieta.append(prvy_rodic[i])               # do dietat2 dam rodica1
        return prve_dieta, druhe_dieta                          # vratim vytvorené deti


def mutation(jedinec, obvod):                                   # funkcia na viacnasobnú mutáciu
    for i in range(0, len(jedinec)):                            # pre všetky gény jedinca
        nahoda = random.random()                                # vygeneruj náhodné číslo
        if nahoda < mutation_rate:                              # ak je cislo menšie ako sanca na uplnu zmenu genu
            nahrada = random.randint(1, obvod)                  # vytvor náhradný gén
            sanca = random.random()                             # novú šancu na odbocenie pren
            new = gen_class.Gene(nahrada, riadky, stlpce, sanca)    # vytvor ho
            jedinec[i] = new                                    # zapíš ho do jedinca

        if nahoda < swap_rate:                                  # ak cislo menej ako sanca na zmenu poradia
            druhy = random.randint(0, len(jedinec) - 1)         # vyber druhého na výmenu poradia
            jedinec[i], jedinec[druhy] = jedinec[druhy], jedinec[i] # vymen ich

        if nahoda < otocenie:                                   # ak je cislo mensie ako sanca na zmenu otocenia
            jedinec[i].odbocenie = not jedinec[i].odbocenie     # zneguj hodnotu otocenia v gene
    return jedinec                                              # vrát daneho jedinca


def mutation_2(jedinec, obvod):                                 # funkcia na jednu mutáciu
    nahoda = random.random()                                    # vygeneruj náhodné číslo
    pozicia = random.randint(0, len(jedinec) - 1)               # náhodný gen v jedincovi
    if nahoda < mutation_rate:                                  # rovnake postupy ako hore
        nahrada = random.randint(0, obvod)
        sanca = random.random()
        new = gen_class.Gene(nahrada, riadky, stlpce, sanca)
        jedinec[pozicia] = new

    if nahoda < swap_rate:
        druhy = random.randint(0, len(jedinec) - 1)
        jedinec[pozicia], jedinec[druhy] = jedinec[druhy], jedinec[pozicia]

    if nahoda < otocenie:
        jedinec[pozicia].odbocenie = not jedinec[pozicia].odbocenie
    return jedinec                                              # vrat upraveneho jedinca


def posun(gen):                                                 # funkcia na posun mnícha po mape
    if gen.get_smer() == "Up":                                  # ak je smer hore
        gen.set_y_posun(-1)                                     # tak posun suradnicu y = y-1
    elif gen.get_smer() == "Down":                              # ak je smer dole
        gen.set_y_posun(1)                                      # tak posun suradnicu y = y + 1
    elif gen.get_smer() == "Right":                             # ak je smer doprava
        gen.set_x_posun(1)                                      # posun suradnicu x = x + 1
    elif gen.get_smer() == "Left":                              # ak je smer dolava
        gen.set_x_posun(-1)                                     # tak posun suradnicu x = x - 1


def check(gen):                                                 # funkcia na kotrolu posunu
    if 0 <= gen.x_posun < stlpce and 0 <= gen.y_posun < riadky: # ak su suradnice posunu v hraniciach mapy
        return True                                             # tak vrat True
    return False                                                # inak vrat False


def hrabanie(population, fitness_zoznam, volanie):              # funkcia na hrabanie mapy
    new_mapa = deepcopy(mapa)                                   # vytvor kópiu mapy
    for i in range(0, len(population)):                         # pre kadý gén v jedincovi
        gen = population[i]                                     # načítaj den do premennej gen
        if volanie == 2:                                        # ak to neni 1. generácia
            gen.set_smer(gen.povodny_smer)                      # tak nastav sme na povodne suradnice
            gen.reset_posun(gen.x, gen.y)                       # a zresetuj posun
        suradnice = gen.get_suradnice()                         # zisti nove suradnice
        if new_mapa[suradnice[1]][suradnice[0]] != 0:           # skontroluj ci su platne
            continue
        new_mapa[suradnice[1]][suradnice[0]] = gen.start        # ak ano, tak tam zapíš hodnotu gen.start
        posun(gen)                                              # zavolaj funkciu posun pre posun na nove suradnice
        suradnice = gen.get_posun()                             # zisti tieto suradnice
        while check(gen):                                       # ak sme stále v hraniciach mapy
            if new_mapa[suradnice[1]][suradnice[0]] != 0:       # ak je pole v mape nie je volne
                value = naraz.naraz(gen, new_mapa, riadky, stlpce)  # zavolaj funkciu naraz
                if value == 3:                                  # ak ta vrati 3
                    new_mapa = naraz.backtracking(new_mapa, gen.start, riadky, stlpce)  # zavolaj funkciu backtracking
                    break                                       # a vyjdi z cyklu
                elif value == 1:                                # ak vráti 1
                    posun(gen)                                  # tak sa našla nova cesta a pokračujeme
                    suradnice = gen.get_posun()
                else:                                           # inak
                    break                                       # vystupime z cyklu
            new_mapa[suradnice[1]][suradnice[0]] = gen.start    # posun v cykle
            posun(gen)
            suradnice = gen.get_posun()

    fitness = 0                                                 # vyratam fitness
    for i in range(0, riadky):
        for j in range(0, stlpce):
            if new_mapa[i][j] != 0:                             # pre každe pole, čo je ine ako 0
                fitness += 1                                    # zdvihni fitness o jedna
    if fitness == riadky * stlpce:                              # ak sa rovna hladanej fitness
        print(tabulate(new_mapa))                               # tak ju vypis
        print("PODARILO SA NAJST ODPOVED :)")
        exit(0)                                                 # a ukonci program
    fitness_zoznam.append(fitness)                              # inak ju zapis do zoznamu fitness hodnot
    return population                                           # vrat danu populaciu


def main():
    fitness_zoznam = []
    zoznam_objektov = {}                                        # inicializacia vstupnych poli
    number_of_genes = riadky + stlpce
    genes = []
    for i in range(1, number_of_genes * 2 + 1):                 # vygeneruj mozne start pozicie
        genes.append(i)
    for j in range(0, pocet_jedincov):                          # vytvor prvu generaciu
        population = random.sample(genes, pocet_genov)
        tmp = []
        for v in population:
            sanca = random.random()
            tmp.append(gen_class.Gene(v, riadky, stlpce, sanca))    # pre dane geny vytvorim objekty
        zoznam_objektov[j] = hrabanie(tmp, fitness_zoznam, 1)   # a pridam do slovnika

    maximum = fitness_zoznam[0]
    minimum = fitness_zoznam[0]
    sumacia = 0                                                 # inicializujem premenné
    for value in fitness_zoznam:                                # v cykle zistim udaje o fitness
        if value > maximum:
            maximum = value
        elif value < minimum:
            minimum = value
        sumacia += value

    print("\nGenerácia č.: 1 Max. prvok: " + str(maximum) + " Min. prvok " + str(minimum) +
          " primer " + str(sumacia / pocet_jedincov))
    print(fitness_zoznam)                                       # vypisem tieto kontrorlne udaje

    new_population = {}                                         # vytvorim novy slovnik


##########################################################################################################
    k = 2
    generacia = 2                                               # inicializujem premenne
    while k <= pocet_generacii:                                 # cyklus na nove generacie
        new_population.clear()                                  # vyčistim slovnik
        j = 0
        for i in range(0, int(pocet_jedincov / 2) - 1):         # pre polovicu poctu jedincov - 1
            if vyber_rodicov == 1:                              # podla typu vyberu rodicov
                prvy_rodic = turnaj(fitness_zoznam)             # vyberiem prveho rodica z turnaja
                druhy_rodic = turnaj(fitness_zoznam)            # takisto druheho

            else:
                prvy_rodic = ruleta(fitness_zoznam)             # vyberiem prveho rodica z rulety
                druhy_rodic = ruleta(fitness_zoznam)            # vyberiem druhe rodica z rulety

            deti = krizenie(zoznam_objektov.get(prvy_rodic), zoznam_objektov.get(druhy_rodic))  # vytvorim nove deti
            new_population[j] = deti[0]                         # zapíšem ich do geenrácie
            new_population[j + 1] = deti[1]
            j += 2

        nova_krv(new_population, number_of_genes * 2, j)        # pridám novu krv

        zoznam_objektov.clear()                                 # vyčistím premenné
        fitness_zoznam.clear()
        j = 0
        for key in new_population:                              # pre každého jedinca
            zoznam_objektov[j] = hrabanie(new_population[key], fitness_zoznam, 2)   # pohrabem záhradku
            sanca = random.random()                             # vygenerujem náhodnu šancu
            if sanca < mutation_chance:                         # ak je menšia ako zadana sanca na mutaciu z configu
                if typ_mutacie == 1:                            # podla typu mutacie
                    zoznam_objektov[j] = mutation_2(zoznam_objektov[j], len(genes)) # zmutujem
                else:
                    zoznam_objektov[j] = mutation(zoznam_objektov[j], len(genes))   # zmutujem
            j += 1

        maximum = fitness_zoznam[0]
        minimum = fitness_zoznam[0]
        sumacia = 0
        for value in fitness_zoznam:                            # opat vyratam max a min a priemerny fitness
            if value > maximum:
                maximum = value
            elif value < minimum:
                minimum = value
            sumacia += value

        print("\nGenerácia č.: " + str(generacia) + " Max. prvok: " + str(maximum) + " Min. prvok " + str(minimum) +
              " primer " + str(sumacia / pocet_jedincov))
        print(fitness_zoznam)                                   # a vypisem kontrolny vypis

        if k == pocet_generacii:                                # ak sme na konci, tak otazka
            dalej = input("\n\nChcete pokracovat dalsich " + str(pocet_generacii) + " generacii?")
            if dalej == "1":                                    # ak chceme ešte pokračovat
                k = 0                                           # tak začnem cyklus znova prechadzať
            else:
                exit(0)                                         # inak ukončim program
        k += 1
        generacia += 1                                          # zvyšovanie premenných


if __name__ == "__main__":
    main()

