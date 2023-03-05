class PitcherExPoint:

    def __init__(self):
        super().__init__()
        self.speed = 1
        self.max_stamina = 1
        self.now_stamina = 1
        self.control = 1
        self.pitch_types = {}
        self.henka = 1

    def add_speed_point(self, point: int):
        self.speed += point
        if self.speed >= 100:
            up = self.speed // 100
            self.speed = self.speed % 100
            return up
        else:
            return 0

    def add_max_stamina_point(self, point: int):
        self.max_stamina += point
        if self.max_stamina >= 100:
            up = self.max_stamina // 100
            self.max_stamina = self.max_stamina % 100
            return up
        else:
            return 0

    def add_control_point(self, point: int):
        self.control += point
        if self.control >= 100:
            up = self.control // 100
            self.control = self.control % 100
            return up
        else:
            return 0

    def add_speed_point(self, point: int):
        self.speed += point
        if self.speed >= 100:
            up = self.speed // 100
            self.speed = self.speed % 100
            return up
        else:
            return 0

    def add_henka_point(self, point: int):
        self.henka += point
        if self.henka >= 100:
            up = self.henka // 100
            self.henka = self.henka % 100
            return up
        else:
            return 0

    def add_pitch_types_key(self, ball_name: str):
        self.pitch_types[ball_name] = 0
