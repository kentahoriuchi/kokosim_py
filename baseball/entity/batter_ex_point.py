class BatterExPoint:

    def __init__(self):
        super().__init__()
        self.contact = 0
        self.power = 0
        self.run = 0
        self.defence = 0
        self.throw = 0
        self.batting_eye = 0
        self.c_lead = 0

    def add_contact_point(self, point: int):
        self.contact += point
        if self.contact >= 100:
            up = self.contact // 100
            self.contact = self.contact % 100
            return up
        else:
            return 0

    def add_power_point(self, point: int):
        self.power += point
        if self.power >= 100:
            up = self.power // 100
            self.power = self.power % 100
            return up
        else:
            return 0

    def add_run_point(self, point: int):
        self.run += point
        if self.run >= 100:
            up = self.run // 100
            self.run = self.run % 100
            return up
        else:
            return 0

    def add_defence_point(self, point: int):
        self.defence += point
        if self.defence >= 100:
            up = self.defence // 100
            self.defence = self.defence % 100
            return up
        else:
            return 0

    def add_throw_point(self, point: int):
        self.throw += point
        if self.throw >= 100:
            up = self.throw // 100
            self.throw = self.throw % 100
            return up
        else:
            return 0

    def add_batting_eye_point(self, point: int):
        self.batting_eye += point
        if self.batting_eye >= 100:
            up = self.batting_eye // 100
            self.batting_eye = self.batting_eye % 100
            return up
        else:
            return 0

    def add_c_lead_point(self, point: int):
        self.c_lead += point
        if self.c_lead >= 100:
            up = self.c_lead // 100
            self.c_lead = self.c_lead % 100
            return up
        else:
            return 0
