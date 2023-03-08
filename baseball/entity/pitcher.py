from baseball.entity.pitcher_stats import PitcherStats
from baseball.entity.pitch_types_list import Pitch_types_list
from baseball.entity.pitcher_ex_point import PitcherExPoint
from enum import IntEnum, auto


class Pitcher:

    def __init__(self):
        super().__init__()
        self.speed = 1
        self.max_stamina = 1
        self.now_stamina = 1
        self.control = 1
        self.henka = 1
        self.pitch_types = {}
        self.pitcher_stats = PitcherStats()
        self.pitcher_ex_point = PitcherExPoint()

    def set_speed(self, speed: int):
        if speed < 1 or speed > 100:
            raise ValueError("invalid speed value")
        self.speed = speed
        return self

    def set_max_stamina(self, stamina: int):
        if stamina < 1 or stamina > 100:
            raise ValueError("invalid stamina value")
        self.max_stamina = stamina
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

    def add_pitch_types(self, ball_name: str, point: int):
        if ball_name not in Pitch_types_list:
            raise ValueError("invalid ball name")
        if ball_name in self.pitch_types:
            raise ValueError("already exist ball name in pitch types")
        if point < 1 or point > 100:
            raise ValueError("invalid pitch type value")
        self.pitch_types[ball_name] = point
        self.pitcher_ex_point.add_pitch_types_key(ball_name)
        return self

    # 複数種類加算される可能性を踏まえて辞書型で経験値追加の記述を行う
    def get_ex_point(self, points: dict):
        for key in points.keys():
            if key == PitcherStatus.speed:
                self.speed += self.pitcher_ex_point.add_speed_point(points[key])
            elif key == PitcherStatus.max_stamina:
                self.max_stamina += self.pitcher_ex_point.add_max_stamina_point(points[key])
            elif key == PitcherStatus.control:
                self.control += self.pitcher_ex_point.add_control_point(points[key])
            elif key == PitcherStatus.henka:
                self.henka += self.pitcher_ex_point.add_henka_point(points[key])
            elif key in self.pitch_types.keys():
                self.pitch_types[key] += self.pitcher_ex_point.add_pitch_types_point(key, points[key])
            else:
                raise ValueError("invalid key in pitcher ex_point dict")


class PitcherStatus(IntEnum):
    speed = auto()
    max_stamina = auto()
    control = auto()
    henka = auto()
    pitch_types = auto()
