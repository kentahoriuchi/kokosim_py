import json
from enum import IntEnum, auto
from baseball.domain.player.pitcher.pitcher import Pitcher
from baseball.domain.player.batter.batter import Batter


class Player:

    def __init__(self):
        self.name = "no name"
        self.grade = Grade.preattend
        self.batter = Batter()
        self.pitcher = Pitcher()
        self.school = "no data"
        self.batter_hand = Hand.right
        self.pitcher_hand = Hand.right

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
        player.batter_hand = self.batter_hand
        player.pitcher_hand = self.pitcher_hand
        player.contact = self.batter.contact
        player.power = self.batter.power
        player.run = self.batter.run
        player.defence = self.batter.defence
        player.throw = self.batter.throw
        player.batting_eye = self.batter.batting_eye
        player.c_lead = self.batter.c_lead
        player.batter_position = json.dumps(self.batter.batter_position.position_pro)
        player.batter_box_count = self.batter.batter_stats.batter_box_count
        player.single_count = self.batter.batter_stats.single_count
        player.double_count = self.batter.batter_stats.double_count
        player.triple_count = self.batter.batter_stats.triple_count
        player.homerun_count = self.batter.batter_stats.homerun_count
        player.batter_fourball_count = self.batter.batter_stats.fourball_count
        player.batter_strikeout_count = self.batter.batter_stats.strikeout_count
        player.batter_runs = self.batter.batter_stats.runs
        player.contact_ex = self.batter.batter_ex_point.contact
        player.power_ex = self.batter.batter_ex_point.power
        player.run_ex = self.batter.batter_ex_point.run
        player.defence_ex = self.batter.batter_ex_point.defence
        player.throw_ex = self.batter.batter_ex_point.throw
        player.batting_eye_ex = self.batter.batter_ex_point.batting_eye
        player.c_lead_ex = self.batter.batter_ex_point.c_lead
        player.speed = self.pitcher.speed
        player.max_stamina = self.pitcher.max_stamina
        player.now_stamina = self.pitcher.now_stamina
        player.control = self.pitcher.control
        player.henka = self.pitcher.henka
        player.pitch_types = json.dumps(self.pitcher.pitch_types)
        player.speed_ex = self.pitcher.pitcher_ex_point.speed
        player.max_stamina_ex = self.pitcher.pitcher_ex_point.max_stamina
        player.control_ex = self.pitcher.pitcher_ex_point.control
        player.henka_ex = self.pitcher.pitcher_ex_point.henka
        player.pitch_types_ex = json.dumps(self.pitcher.pitcher_ex_point.pitch_types)
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


class Hand(IntEnum):
    right = auto()
    left = auto()
    switch = auto()
