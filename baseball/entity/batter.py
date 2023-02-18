from baseball.entity.batter_stats import BatterStats
from baseball.entity.player import Player


# builder patternで実装してみる
class Batter(Player):

    def __init__(self, builder):
        # メソッドチェインの最後のbuild()をうけて、オブジェクトに値をセットする
        super().__init__()
        self.name = builder.builder_name
        self.contact = builder.builder_contact
        self.power = builder.builder_power
        self.run = builder.builder_run
        self.defence = builder.builder_defence
        self.throw = builder.builder_throw
        self.batter_stats = BatterStats()

    def __str__(self):
        info = (f'名前: {self.name}',
                f'ミート: {self.contact} '
                f'パワー: {self.power} '
                f'走力: {self.run} '
                f'守備: {self.defence} '
                f'送球: {self.throw}')
        return '\n'.join(info)

    # オブジェクト内にBuilderを持たせる
    class ButterBuilder:
        def __init__(self):
            self.builder_name = "no name"
            self.builder_contact = 1
            self.builder_power = 1
            self.builder_run = 1
            self.builder_defence = 1
            self.builder_throw = 1

        def name(self, name: str):
            self.builder_name = name
            return self

        def contact(self, contact: int):
            if contact < 1 or contact > 100:
                raise ValueError("invalid contact value")
            self.builder_contact = contact
            return self

        def power(self, power: int):
            if power < 1 or power > 100:
                raise ValueError("invalid power value")
            self.builder_power = power
            return self

        def run(self, run: int):
            if run < 1 or run > 100:
                raise ValueError("invalid run value")
            self.builder_run = run
            return self

        def defence(self, defence: int):
            if defence < 1 or defence > 100:
                raise ValueError("invalid defence value")
            self.builder_defence = defence
            return self

        def throw(self, throw: int):
            if throw < 1 or throw > 100:
                raise ValueError("invalid throw value")
            self.builder_throw = throw
            return self

        # メソッドチェインの最後にbuild()をコールさせて生成したComputerオブジェクトを返す
        def build(self):
            return Batter(self)
