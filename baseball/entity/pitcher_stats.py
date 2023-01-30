from baseball.enums.batter_result import BatterResult


class PitcherStats:

    def __init__(self):
        self.out = 0
        self.runs = 0
        self.strikeout = 0
        self.fourball = 0

    def count(self, action, score):
        if action == BatterResult.out:
            self.out += 1
        elif action == BatterResult.strikeout:
            self.out += 1
            self.strikeout += 1
        elif action == BatterResult.fourball:
            self.fourball += 1
        self.runs += score

    def era(self):
        return round(self.runs * 9 / (self.out / 3), 3)

    def inning(self):
        return round(self.out / 3, 1)
