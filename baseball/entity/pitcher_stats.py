from baseball.enums.batter_result import BatterResult


class PitcherStats:

    def __init__(self):
        self.out_count = 0
        self.runs = 0
        self.strikeout_count = 0
        self.fourball_count = 0

    def count(self, action, score):
        if action == BatterResult.out:
            self.out_count += 1
        elif action == BatterResult.strikeout:
            self.out_count += 1
            self.strikeout_count += 1
        elif action == BatterResult.fourball:
            self.fourball_count += 1
        self.runs += score

    def era(self):
        return round(self.runs * 9 / (self.out_count / 3), 3)

    def inning(self):
        return round(self.out_count / 3, 1)
