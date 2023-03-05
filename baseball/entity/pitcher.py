from baseball.entity.pitcher_stats import PitcherStats


class Pitcher:

    def __init__(self):
        super().__init__()
        self.speed = 1
        self.stamina = 1
        self.control = 1
        self.henka = 1
        self.pitcher_stats = PitcherStats()

    def set_speed(self, speed: int):
        if speed < 1 or speed > 100:
            raise ValueError("invalid speed value")
        self.speed = speed
        return self

    def set_stamina(self, stamina: int):
        if stamina < 1 or stamina > 100:
            raise ValueError("invalid stamina value")
        self.stamina = stamina
        return self

    def set_control(self, control: int):
        if control < 1 or control > 100:
            raise ValueError("invalid control value")
        self.control = control
        return self

    def set_henka(self, henka: int):
        if henka < 1 or henka > 100:
            raise ValueError("invalid henka value")
        self.henka = henka
        return self
