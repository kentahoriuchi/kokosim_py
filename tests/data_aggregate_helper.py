from baseball.enums.batter_result import BatterResult


# テスト用のヘルパークラス
class DataAggregateHelper:
    def __init__(self):
        self.batter_box_count = 0
        self.single_count = 0
        self.double_count = 0
        self.triple_count = 0
        self.homerun_count = 0
        self.fourball_count = 0
        self.strikeout_count = 0

    def count(self, action):
        self.batter_box_count += 1
        if action == BatterResult.single:
            self.single_count += 1
        elif action == BatterResult.double:
            self.double_count += 1
        elif action == BatterResult.triple:
            self.triple_count += 1
        elif action == BatterResult.homerun:
            self.homerun_count += 1
        elif action == BatterResult.fourball:
            self.fourball_count += 1
        elif action == BatterResult.strikeout:
            self.strikeout_count += 1
        elif action == BatterResult.out:
            pass
        else:
            raise ValueError("Input action Type not match")

    def fourball_prob(self):
        return round(self.fourball_count / self.batter_box_count, 3)

    def strikeout_prob(self):
        return round(self.strikeout_count / (self.batter_box_count - self.fourball_count), 3)

    def single_prob(self):
        return round(self.single_count / (self.batter_box_count - self.fourball_count), 3)

    def double_prob(self):
        return round(self.double_count / (self.batter_box_count - self.fourball_count),3)

    def triple_prob(self):
        return round(self.triple_count / (self.batter_box_count - self.fourball_count), 3)

    def homerun_prob(self):
        return round(self.homerun_count / (self.batter_box_count - self.fourball_count), 3)

    def average(self):
        return round((self.single_count + self.double_count + self.triple_count + self.homerun_count) \
            / (self.batter_box_count - self.fourball_count), 3)
