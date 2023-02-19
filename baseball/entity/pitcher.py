from baseball.entity.pitcher_stats import PitcherStats
from baseball.entity.player import Player


# builder patternで実装してみる
class Pitcher(Player):

    def __init__(self, builder):
        # メソッドチェインの最後のbuild()をうけて、オブジェクトに値をセットする
        super().__init__()
        self.name = builder.builder_name
        self.speed = builder.builder_speed
        self.stamina = builder.builder_stamina
        self.control = builder.builder_control
        self.henka = builder.builder_henka
        self.pitcher_stats = PitcherStats()

    def __str__(self):
        info = (f'名前: {self.name}',
                f'球速: {self.speed} '
                f'スタミナ: {self.stamina} '
                f'コントロール: {self.control} '
                f'変化球: {self.henka} ')
        return '\n'.join(info)

    # オブジェクト内にBuilderを持たせる
    class PitcherBuilder:
        def __init__(self):
            self.builder_name = "no name"
            self.builder_speed = 1
            self.builder_stamina = 1
            self.builder_control = 1
            self.builder_henka = 1

        def name(self, name: str):
            self.builder_name = name
            return self

        def speed(self, speed: int):
            if speed < 1 or speed > 100:
                raise ValueError("invalid speed value")
            self.builder_speed = speed
            return self

        def stamina(self, stamina: int):
            if stamina < 1 or stamina > 100:
                raise ValueError("invalid stamina value")
            self.builder_stamina = stamina
            return self

        def control(self, control: int):
            if control < 1 or control > 100:
                raise ValueError("invalid control value")
            self.builder_control = control
            return self

        def henka(self, henka: int):
            if henka < 1 or henka > 100:
                raise ValueError("invalid henka value")
            self.builder_henka = henka
            return self

        # メソッドチェインの最後にbuild()をコールさせて生成したComputerオブジェクトを返す
        def build(self):
            return Pitcher(self)
