from baseball.domain.player.batter.batter_stats import BatterStats
from baseball.domain.player.batter.batter_position import BatterPosition
from baseball.domain.player.batter.batter_ex_point import BatterExPoint
from enum import IntEnum, auto


class Batter:

    def __init__(self):
        super().__init__()
        self.contact = 1
        self.power = 1
        self.run = 1
        self.defence = 1
        self.throw = 1
        self.batting_eye = 1
        self.c_lead = 1
        self.batter_position = BatterPosition()
        self.batter_stats = BatterStats()
        self.batter_ex_point = BatterExPoint()

    def set_contact(self, contact: int):
        if contact < 1 or contact > 100:
            raise ValueError("invalid contact value")
        self.contact = contact
        return self

    def set_power(self, power: int):
        if power < 1 or power > 100:
            raise ValueError("invalid power value")
        self.power = power
        return self

    def set_run(self, run: int):
        if run < 1 or run > 100:
            raise ValueError("invalid run value")
        self.run = run
        return self

    def set_defence(self, defence: int):
        if defence < 1 or defence > 100:
            raise ValueError("invalid defence value")
        self.defence = defence
        return self

    def set_throw(self, throw: int):
        if throw < 1 or throw > 100:
            raise ValueError("invalid throw value")
        self.throw = throw
        return self

    def set_batting_eye(self, batting_eye: int):
        if batting_eye < 1 or batting_eye > 100:
            raise ValueError("invalid batting_eye value")
        self.batting_eye = batting_eye
        return self

    def set_c_lead(self, c_lead: int):
        if c_lead < 1 or c_lead > 100:
            raise ValueError("invalid c_lead value")
        self.c_lead = c_lead
        return self

    # 複数種類加算される可能性を踏まえて辞書型で経験値追加の記述を行う
    def get_ex_point(self, points: dict):
        for key in points.keys():
            if key == BatterStatus.contact:
                self.contact += self.batter_ex_point.add_contact_point(points[key])
            elif key == BatterStatus.power:
                self.power += self.batter_ex_point.add_power_point(points[key])
            elif key == BatterStatus.run:
                self.run += self.batter_ex_point.add_run_point(points[key])
            elif key == BatterStatus.defence:
                self.defence += self.batter_ex_point.add_defence_point(points[key])
            elif key == BatterStatus.throw:
                self.throw += self.batter_ex_point.add_throw_point(points[key])
            elif key == BatterStatus.batting_eye:
                self.batting_eye += self.batter_ex_point.add_batting_eye_point(points[key])
            elif key == BatterStatus.c_lead:
                self.c_lead += self.batter_ex_point.add_c_lead_point(points[key])
            else:
                raise ValueError("invalid key in batter ex_point dict")


class BatterStatus(IntEnum):
    contact = auto()
    power = auto()
    run = auto()
    defence = auto()
    throw = auto()
    batting_eye = auto()
    c_lead = auto()
