class Gene:
    def __init__(self, start, riadky, stlpce, sanca):
        self.start = start
        if riadky < start <= stlpce + riadky:
            self.smer = "Up"
            self.povodny_smer = "Up"
            self.x = start - riadky - 1
            self.y = riadky - 1
        elif riadky + stlpce + riadky < start <= riadky + stlpce + riadky + stlpce:
            self.smer = "Down"
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
        self.x_posun = self.x
        self.y_posun = self.y

        if sanca > 0.5:
            self.odbocenie = True
        else:
            self.odbocenie = False

    def get_smer(self):
        return self.smer

    def get_suradnice(self):
        return self.x, self.y

    def get_posun(self):
        return self.x_posun, self.y_posun

    def set_smer(self, smer):
        self.smer = smer

    def set_x_posun(self, hodnota):
        self.x_posun = self.x_posun + hodnota

    def set_y_posun(self, hodnota):
        self.y_posun = self.y_posun + hodnota

    def reset_posun(self, x, y):
        self.x_posun = x
        self.y_posun = y

    def get_odbocenie(self):
        return self.odbocenie
