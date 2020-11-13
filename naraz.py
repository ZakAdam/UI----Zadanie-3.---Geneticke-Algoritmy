def naraz(gen, mapa, riadky, stlpce):
    smer = gen.get_smer()
    if smer == "Up" or smer == "Down":
        if smer == "Up":
            suradnice = gen.get_posun()
            if gen.get_odbocenie:
                if suradnice[0] < (stlpce - 1) and mapa[suradnice[1] + 1][suradnice[0] + 1] == 0:
                    gen.set_smer("Right")
                    gen.set_y_posun(1)
                    return 1
                if suradnice[0] > 0 and mapa[suradnice[1] + 1][suradnice[0] - 1] == 0:
                    gen.set_smer("Left")
                    gen.set_y_posun(1)
                    return 1
                if gen.y_posun + 1 == riadky - 1:
                    return 2
            else:
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

        else:
            suradnice = gen.get_posun()
            if gen.get_odbocenie:
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
            else:
                if suradnice[0] < (stlpce - 1) and mapa[suradnice[1] - 1][suradnice[0] + 1] == 0:
                    gen.set_smer("Right")
                    gen.set_y_posun(-1)
                    return 1
                if 0 < suradnice[0] and mapa[suradnice[1] - 1][suradnice[0] - 1] == 0:
                    gen.set_smer("Left")
                    gen.set_y_posun(-1)
                    return 1
                if gen.y_posun - 1 == 0:
                    return 2
        if suradnice[0] == (stlpce - 1) or suradnice[0] == 0:  # pripad, že je to bod na hranici
            return 2

    else:
        if smer == "Right":
            suradnice = gen.get_posun()
            if gen.get_odbocenie:
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
                if 0 < suradnice[1] < (riadky - 1) and mapa[suradnice[1] + 1][suradnice[0] - 1] == 0:
                    gen.set_smer("Down")
                    gen.set_x_posun(-1)
                    return 1
                if 0 < suradnice[1] < (riadky - 1) and mapa[suradnice[1] - 1][suradnice[0] - 1] == 0:
                    gen.set_smer("Up")
                    gen.set_x_posun(-1)
                    return 1
                if gen.x_posun - 1 == 0:
                    return 2

        else:
            suradnice = gen.get_posun()
            if gen.get_odbocenie:
                if suradnice[1] < (riadky - 1) and mapa[suradnice[1] + 1][suradnice[0] + 1] == 0:   #Left - Left
                    gen.set_smer("Down")
                    gen.set_x_posun(1)
                    return 1
                if 0 < suradnice[1] and mapa[suradnice[1] - 1][suradnice[0] + 1] == 0:
                    gen.set_smer("Up")
                    gen.set_x_posun(1)
                    return 1
                if gen.x_posun + 1 == stlpce - 1:                      # hranicny stav
                    return 2
            else:
                if 0 < suradnice[1] and mapa[suradnice[1] - 1][suradnice[0] + 1] == 0:
                    gen.set_smer("Up")
                    gen.set_x_posun(1)
                    return 1
                if suradnice[1] < (riadky - 1) and mapa[suradnice[1] + 1][suradnice[0] + 1] == 0:   #Left - Left
                    gen.set_smer("Down")
                    gen.set_x_posun(1)
                    return 1
                if gen.x_posun + 1 == stlpce - 1:  # hranicny stav
                    return 2
        if suradnice[1] == (riadky - 1) or suradnice[1] == 0:   # pripad, že je to bod na hranici
            return 2

    return 3