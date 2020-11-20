class Gene:                                             # trieda pre objekty typu gen
    def __init__(self, start, riadky, stlpce, sanca):   # konštruktor
        self.start = start                              # do startu zapisem start
        if riadky < start <= stlpce + riadky:           # zistim suradnice
            self.smer = "Up"                            # nastavim smer
            self.povodny_smer = "Up"                    # rovnako povodny smer
            self.x = start - riadky - 1                 # suradnicu x
            self.y = riadky - 1                         # suradnicu y
        elif riadky + stlpce + riadky < start <= riadky + stlpce + riadky + stlpce:
            self.smer = "Down"                          # analogicky dalej
            self.povodny_smer = "Down"
            self.x = stlpce - (start - riadky*2 - stlpce)
            self.y = 0
        elif start <= riadky:
            self.smer = "Right"
            self.povodny_smer = "Right"
            self.x = 0
            self.y = start - 1
        elif riadky + stlpce < start <= riadky + stlpce + riadky:
            self.smer = "Left"
            self.povodny_smer = "Left"
            self.x = stlpce - 1
            self.y = riadky - (start - riadky - stlpce)
        self.x_posun = self.x                           # x_posun nastavím na x
        self.y_posun = self.y                           # y_posun nastavim na y

        if sanca > 0.5:                                 # odbocenie podla vstupnej hodnoty
            self.odbocenie = True                       # bud na True
        else:
            self.odbocenie = False                      # alebo False

    def get_smer(self):                                 # metoda na hodnotu smeru
        return self.smer

    def get_suradnice(self):                            # metoda na hodnotu suradnic
        return self.x, self.y

    def get_posun(self):                                # metoda na hondotu posunu
        return self.x_posun, self.y_posun

    def set_smer(self, smer):                           # metoda na nastavenie smeru
        self.smer = smer

    def set_x_posun(self, hodnota):                     # na nastavenie x_posunu
        self.x_posun = self.x_posun + hodnota

    def set_y_posun(self, hodnota):                     # na nastavenie y_posunu
        self.y_posun = self.y_posun + hodnota

    def reset_posun(self, x, y):                        # na reset posunu
        self.x_posun = x
        self.y_posun = y

    def get_odbocenie(self):                            # na ziskanie odbocenia
        return self.odbocenie
