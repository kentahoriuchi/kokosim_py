# builder patternで実装してみる
class Pitcher:

    def __init__(self, builder):
        # メソッドチェインの最後のbuild()をうけて、オブジェクトに値をセットする
        self.name = builder.builder_name
        self.speed = builder.builder_speed
        self.stamina = builder.builder_stamina
        self.control = builder.builder_control
        self.henka = builder.builder_henka

    def __str__(self):
        info = (f'名前: {self.name}',
                f'球速: {self.speed} '
                f'スタミナ: {self.stamina} '
                f'コントロール: {self.control} '
                f'変化球: {self.henka} ')
        return '\n'.join(info)

    # オブジェクト内にBuilderを持たせる
    class ButterBuilder:
        def __init__(self):
            self.builder_name = "no name"
            self.builder_speed = 0
            self.builder_stamina = 0
            self.builder_control = 0
            self.builder_henka = 0

        def name(self, name):
            self.builder_name = name
            return self

        def speed(self, speed):
            self.builder_speed = speed
            return self

        def stamina(self, stamina):
            self.builder_stamina = stamina
            return self

        def control(self, control):
            self.builder_control = control
            return self

        def henka(self, henka):
            self.builder_henka = henka
            return self

        # メソッドチェインの最後にbuild()をコールさせて生成したComputerオブジェクトを返す
        def build(self):
            return Pitcher(self)
