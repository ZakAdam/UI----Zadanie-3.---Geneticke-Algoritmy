def naraz(gen, mapa, riadky, stlpce):                       # funkcia na prehladavanie pri narazeni
    smer = gen.get_smer()                                   # zistime smer
    if smer == "Up" or smer == "Down":                      # ak je hore alebo dole
        if smer == "Up":                                    # ak je hore
            suradnice = gen.get_posun()                     # zisti suradnice
            if gen.get_odbocenie():                         # zisti hodnotu odbocenia
                if suradnice[0] < (stlpce - 1) and mapa[suradnice[1] + 1][suradnice[0] + 1] == 0:
                    gen.set_smer("Right")                   # skontroluj smer doprava a nastav ho
                    gen.set_y_posun(1)                      # prestav premennu posun
                    return 1                                # vrat hodnotu 1
                if suradnice[0] > 0 and mapa[suradnice[1] + 1][suradnice[0] - 1] == 0:
                    gen.set_smer("Left")                    # analogicky pre odbocenie do lava
                    gen.set_y_posun(1)
                    return 1
                if gen.y_posun + 1 == riadky - 1:           # ak sme nenasli cestu a sme na kraji
                    return 2                                # vrat 2
            else:                                           # to iste iba v opacnom poradi prehladavanie odbocenia
                if suradnice[0] > 0 and mapa[suradnice[1] + 1][suradnice[0] - 1] == 0:
                    gen.set_smer("Left")
                    gen.set_y_posun(1)
                    return 1
                if suradnice[0] < (stlpce - 1) and mapa[suradnice[1] + 1][suradnice[0] + 1] == 0:
                    gen.set_smer("Right")
                    gen.set_y_posun(1)
                    return 1
                if gen.y_posun + 1 == riadky - 1:
                    return 2

        else:                                               # ak je smer dole
            suradnice = gen.get_posun()                     # zisti posun
            if gen.get_odbocenie():                         # dalej rovnako ako hore
                if 0 < suradnice[0] and mapa[suradnice[1] - 1][suradnice[0] - 1] == 0:
                    gen.set_smer("Left")
                    gen.set_y_posun(-1)
                    return 1
                if suradnice[0] < (stlpce - 1) and mapa[suradnice[1] - 1][suradnice[0] + 1] == 0:
                    gen.set_smer("Right")
                    gen.set_y_posun(-1)
                    return 1
                if gen.y_posun - 1 == 0:                    # ak sme nenasli cestu a sme na kraji
                    return 2                                # vrat 2
            else:                                           # to iste, len v opacnom poradi
                if suradnice[0] < (stlpce - 1) and mapa[suradnice[1] - 1][suradnice[0] + 1] == 0:
                    gen.set_smer("Right")
                    gen.set_y_posun(-1)
                    return 1
                if 0 < suradnice[0] and mapa[suradnice[1] - 1][suradnice[0] - 1] == 0:
                    gen.set_smer("Left")
                    gen.set_y_posun(-1)
                    return 1
                if gen.y_posun - 1 == 0:                    # ak sme na kraji bez cesty
                    return 2                                # vrat 2
        if suradnice[0] == (stlpce - 1) or suradnice[0] == 0:  # pripad, že je to bod na hranici, bez cesty
            return 2                                        # vrat 2

    else:                                                   # ak je smer doprava alebo dolava
        if smer == "Right":                                 # rovnaky postup ako hore
            suradnice = gen.get_posun()
            if gen.get_odbocenie():
                if 0 < suradnice[1] < (riadky - 1) and mapa[suradnice[1] - 1][suradnice[0] - 1] == 0:
                    gen.set_smer("Up")
                    gen.set_x_posun(-1)
                    return 1
                if 0 < suradnice[1] < (riadky - 1) and mapa[suradnice[1] + 1][suradnice[0] - 1] == 0:
                    gen.set_smer("Down")
                    gen.set_x_posun(-1)
                    return 1
                if gen.x_posun - 1 == 0:                    # ak sme na kraji
                    return 2                                # vrat 2
            else:                                           # opacne poradie
                if 0 < suradnice[1] < (riadky - 1) and mapa[suradnice[1] + 1][suradnice[0] - 1] == 0:
                    gen.set_smer("Down")
                    gen.set_x_posun(-1)
                    return 1
                if 0 < suradnice[1] < (riadky - 1) and mapa[suradnice[1] - 1][suradnice[0] - 1] == 0:
                    gen.set_smer("Up")
                    gen.set_x_posun(-1)
                    return 1
                if gen.x_posun - 1 == 0:                    # ak sme na kraji
                    return 2                                # vrat 2

        else:                                               # ak je smer dolava
            suradnice = gen.get_posun()
            if gen.get_odbocenie():
                if suradnice[1] < (riadky - 1) and mapa[suradnice[1] + 1][suradnice[0] + 1] == 0:
                    gen.set_smer("Down")
                    gen.set_x_posun(1)
                    return 1
                if 0 < suradnice[1] and mapa[suradnice[1] - 1][suradnice[0] + 1] == 0:
                    gen.set_smer("Up")
                    gen.set_x_posun(1)
                    return 1
                if gen.x_posun + 1 == stlpce - 1:           # hranicny stav
                    return 2                                # vrat 2
            else:                                           # opacne poradie
                if 0 < suradnice[1] and mapa[suradnice[1] - 1][suradnice[0] + 1] == 0:
                    gen.set_smer("Up")
                    gen.set_x_posun(1)
                    return 1
                if suradnice[1] < (riadky - 1) and mapa[suradnice[1] + 1][suradnice[0] + 1] == 0:
                    gen.set_smer("Down")
                    gen.set_x_posun(1)
                    return 1
                if gen.x_posun + 1 == stlpce - 1:           # hranicny stav
                    return 2                                # vrat 2
        if suradnice[1] == (riadky - 1) or suradnice[1] == 0:   # pripad, že je to bod na hranici
            return 2                                        # vrat 2

    return 3                                                # ak nie je dalsia cesta a bod nie je na hranici, vrat 3


def backtracking(mapa, delete, riadky, stlpce):             # funkcia na spatne vymazavanie zaseknutych ciest
    for i in range(0, riadky):                              # prejdi celu mapu
        for j in range(0, stlpce):
            if mapa[i][j] == delete:                        # ak sa hodnota v poli rovna hladanej hodnote
                mapa[i][j] = 0                              # tak ju premaz na 0
    return mapa                                             # a vrat takto upravenu mapu
