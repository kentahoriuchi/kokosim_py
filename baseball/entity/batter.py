from baseball.entity.batter_stats import BatterStats


class Batter:

    def __init__(self):
        super().__init__()
        self.contact = 1
        self.power = 1
        self.run = 1
        self.defence = 1
        self.throw = 1
        self.batter_stats = BatterStats()

    def __str__(self):
        info = ( f'ミート: {self.contact} '
                f'パワー: {self.power} '
                f'走力: {self.run} '
                f'守備: {self.defence} '
                f'送球: {self.throw}')
        return '\n'.join(info)

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
