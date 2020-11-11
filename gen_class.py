class Gene:                                                     #TODO pozor na ten 0ty riadok pre Y a X
    def __init__(self, start, riadky, stlpce):
        self.start = start
        if riadky < start <= stlpce + riadky:
            self.smer = "Up"
            self.x = start - riadky - 1
            self.y = riadky - 1
        elif riadky + stlpce + riadky < start <= riadky + stlpce + riadky + stlpce:
            self.smer = "Down"
            self.x = stlpce - (start - riadky*2 - stlpce)
            self.y = 0
        elif start <= riadky:
            self.smer = "Right"
            self.x = 0
            self.y = start - 1
        elif riadky + stlpce < start <= riadky + stlpce + riadky:
            self.smer = "Left"
            self.x = stlpce - 1
            self.y = riadky - (start - riadky - stlpce)
        else:
            self.smer = "Noneeeee"
            self.x = 0
            self.y = 0
        self.x_posun = self.x
        self.y_posun = self.y

    def get_smer(self):
        return self.smer

    def get_suradnice(self):
        return self.x, self.y

    def get_posun(self):
        return self.x_posun, self.y_posun

    def set_smer(self, smer):
        self.smer = smer

    def set_suradnice(self, x, y):
        self.x = x
        self.y = y

    def set_x_posun(self, hodnota):
        self.x_posun = self.x_posun + hodnota

    def set_y_posun(self, hodnota):
        self.y_posun = self.y_posun + hodnota
