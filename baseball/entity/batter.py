# builder patternで実装してみる
class Butter:

    def __init__(self, builder):
        # メソッドチェインの最後のbuild()をうけて、オブジェクトに値をセットする
        self.name = builder.builder_name
        self.contact = builder.builder_contact
        self.power = builder.builder_power
        self.run = builder.builder_run
        self.defence = builder.builder_defence
        self.throw = builder.builder_throw

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
            self.builder_contact = 0
            self.builder_power = 0
            self.builder_run = 0
            self.builder_defence = 0
            self.builder_throw = 0

        def name(self, name):
            self.builder_name = name
            return self

        def contact(self, contact):
            self.builder_contact = contact
            return self

        def power(self, power):
            self.builder_power = power
            return self

        def run(self, run):
            self.builder_run = run
            return self

        def defence(self, defence):
            self.builder_defence = defence
            return self

        def throw(self, throw):
            self.builder_throw = throw
            return self

        # メソッドチェインの最後にbuild()をコールさせて生成したComputerオブジェクトを返す
        def build(self):
            return Butter(self)
