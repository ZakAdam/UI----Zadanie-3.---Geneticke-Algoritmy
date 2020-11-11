import random
import gen_class
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


def naraz(gen, mapa):
    smer = gen.get_smer()
    if smer == "Up" or smer == "Down":
        if smer == "Up":
            suradnice = gen.get_posun()
            if suradnice[0] < (stlpce - 1) and mapa[suradnice[1] + 1][suradnice[0] + 1] == 0:
                print("SOMMMMM TUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU\n")
                gen.set_smer("Right")
                gen.set_y_posun(1)
                return True
            elif suradnice[0] > 0 and mapa[suradnice[1] - 1][suradnice[0] - 1] == 0:
                print("LAVICCCCCCCCAAAAAA")
                gen.set_smer("Left")
                gen.set_y_posun(1)
                return True
        else:
            suradnice = gen.get_posun()
            if 0 < suradnice[0] and mapa[suradnice[1] - 1][suradnice[0] - 1] == 0:
                print("Down do lava\n")
                gen.set_smer("Left")
                gen.set_y_posun(-1)
                return True
            elif suradnice[0] < (stlpce - 1) and mapa[suradnice[1] - 1][suradnice[0] + 1] == 0:
                gen.set_smer("Right")
                gen.set_y_posun(-1)
                return True



    else:
        if smer == "Right":
            suradnice = gen.get_posun()
            if 0 < suradnice[1] < (riadky - 1) and mapa[suradnice[1] - 1][suradnice[0] - 1] == 0:
                print("SOm v Right posune ne hore")
                gen.set_smer("Up")
                gen.set_x_posun(-1)
                return True
            else:
                if 0 < suradnice[1] < (riadky - 1) and mapa[suradnice[1] + 1][suradnice[0] - 1] == 0:
                    gen.set_smer("Down")
                    gen.set_x_posun(-1)
                    return True

        else:
            return False


def posun(gen):
    """
    if gen.get_smer() == "Up":
        gen.y_posun = gen.y_posun - 1
    elif gen.get_smer() == "Down":
        gen.y_posun = gen.y_posun + 1
    elif gen.get_smer() == "Right":
        gen.x_posun = gen.x_posun + 1
    elif gen.get_smer() == "Left":
        gen.x_posun = gen.x_posun - 1
    """
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


def hrabanie(population):
    new_mapa = mapa
    print("druha stena --> " + str(riadky + stlpce))
    for i in population:
        gen = gen_class.Gene(i, riadky, stlpce)
        suradnice = gen.get_suradnice()
        print(str(i) + "  ---  " + gen.get_smer() + "  ---  " + str(suradnice[0]) + " , " + str(suradnice[1]))
        new_mapa[suradnice[1]][suradnice[0]] = i
        posun(gen)
        suradnice = gen.get_posun()
        while check(gen):
            if new_mapa[suradnice[1]][suradnice[0]] != 0:
                if not naraz(gen, new_mapa):
                    break
                else:
                    posun(gen)
                    suradnice = gen.get_posun()
            print("New suradnice su: " + str(suradnice[0]) + " - " + str(suradnice[1]))
            new_mapa[suradnice[1]][suradnice[0]] = i
            posun(gen)
            suradnice = gen.get_posun()

    print(tabulate(new_mapa))


if __name__ == "__main__":
    riadky = len(mapa)
    stlpce = len(mapa[0])
    print(riadky)
    print(stlpce)
    number_of_genes = riadky + stlpce  # TODO add aj geny pre kamene
    genes = []
    for i in range(1, (riadky + stlpce) * 2 + 1):
        genes.append(i)
    population = random.sample(genes, number_of_genes)
    print(population)
    hrabanie(population)

