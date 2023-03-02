from enum import IntEnum, auto
from baseball.entity.pitcher import Pitcher
from baseball.entity.batter import Batter


class Player:

    def __init__(self):
        self.name = "no name"
        self.grade = Grade.preattend
        self.batter = Batter()
        self.pitcher = Pitcher()
        self.school = "no data"

    def set_name(self, name: str):
        self.name = name
        return self

    def set_school(self, school: str):
        self.school = school
        return self

    def update_grade(self):
        if self.grade == Grade.first:
            self.grade = Grade.second
        elif self.grade == Grade.second:
            self.grade = Grade.third
        elif self.grade == Grade.third:
            self.grade = Grade.graduated
        elif self.grade == Grade.preattend:
            self.grade = Grade.first

    # dataclassへの変換用メソッド
    # 循環importを避けるためローカルスコープでimportを行う
    def convert_to_dataclass(self):
        from baseball.repository.player import PlayerData
        player = PlayerData()
        player.name = self.name
        player.school = self.school
        player.grade = self.grade
        player.contact = self.batter.contact
        player.power = self.batter.power
        player.run = self.batter.run
        player.defence = self.batter.defence
        player.throw = self.batter.throw
        player.batter_box_count = self.batter.batter_stats.batter_box_count
        player.single_count = self.batter.batter_stats.single_count
        player.double_count = self.batter.batter_stats.double_count
        player.triple_count = self.batter.batter_stats.triple_count
        player.homerun_count = self.batter.batter_stats.homerun_count
        player.batter_fourball_count = self.batter.batter_stats.fourball_count
        player.batter_strikeout_count = self.batter.batter_stats.strikeout_count
        player.batter_runs = self.batter.batter_stats.runs
        player.speed = self.pitcher.speed
        player.stamina = self.pitcher.stamina
        player.control = self.pitcher.control
        player.henka = self.pitcher.henka
        player.out_count = self.pitcher.pitcher_stats.out_count
        player.pitcher_runs = self.pitcher.pitcher_stats.runs
        player.pitcher_strikeout_count = self.pitcher.pitcher_stats.strikeout_count
        player.pitcher_fourball_count = self.pitcher.pitcher_stats.fourball_count
        return player


class Grade(IntEnum):
    first = 1
    second = 2
    third = 3
    preattend = auto()
    graduated = auto()
    none = auto()
