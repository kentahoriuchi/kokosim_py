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


class Grade(IntEnum):
    first = 1
    second = 2
    third = 3
    preattend = auto()
    graduated = auto()
    none = auto()
