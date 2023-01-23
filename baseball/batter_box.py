from baseball.runner import update
from baseball.enums.batter_result import BatterResult
import random
from enum import Enum, auto


class BatterBox:
    def __init__(self, batter, pitcher, defence_player_list, runner, out_count):
        self.batter = batter
        self.pitcher = pitcher
        self.defence_player_list = defence_player_list
        self.out_count = out_count
        self.runner = runner

    '''
    打席結果の判定ロジックを書いていく
    
    打席結果判定で使用するデータは以下である
    1. 打者の能力（ミート、パワー、走力）
    2. 投手の能力（球速、コントロール、変化球）
    3. 守備側の選手能力（内野守備、外野守備）
    
    処理順と使用するデータは以下のようにする
    1. 四死球判定（コントロール）
    2. 三振判定（ミート、球速、コントロール、変化球）
    3. 当たり（ゴロ、フライ、クリーン）判定（ミート、パワー、球速、コントロール、変化球）
    4. 内野外野判定（パワー、球速）
    3,4の結果でそれぞれ移行
    5-1. 内野ゴロヒット判定（ゴロは内野判定）（走力、内野守備）
      5-1-1. シングルヒット確定
    5-2. 内野フライ　エラー以外はアウト確定
    5-3. 外野フライヒット判定（外野守備）
      5-3-1. ヒット種類（走力）
    5-4. 内野クリーン　シングルヒット確定
    5-5. 外野クリーン　ヒット確定
      5-5-1. ホームラン判定（パワー、球速）
      5-5-2. ヒット種類（走力、外野守備）
    '''
    def judge_result(self):
        # 使用するデータを準備する
        contact = self.batter.contact
        power = self.batter.power
        run = self.batter.run
        speed = self.pitcher.speed
        control = self.pitcher.control
        henka = self.pitcher.henka
        infield_defence = 0
        outfield_defence = 0
        for player in self.defence_player_list[2:6]:
            infield_defence += player.defence
        infield_defence = infield_defence//4
        for player in self.defence_player_list[6:]:
            outfield_defence += player.defence
        outfield_defence = outfield_defence//3

        # 上から順に処理を書いていく
        # 1. 四死球判定（コントロール）
        if self.judge_fourball(control):
            return BatterResult.fourball
        # 2. 三振判定（ミート、球速、コントロール、変化球）
        if self.judge_strikeout(contact, speed, control, henka):
            return BatterResult.out
        # 3. 当たり（ゴロ、フライ、クリーン）判定（ミート、パワー、球速、コントロール、変化球）
        batted_ball = self.judge_batted_ball(contact, power, speed, control, henka)
        # 4. 内野外野判定（パワー、球速）
        field = self.judge_field(power, speed)
        # 5-1. 内野ゴロヒット判定（ゴロは内野判定）（走力、内野守備）
        if batted_ball == BattedBall.goro:
            #  5-1-1. シングルヒット確定
            if self.judge_infield_goro(run, infield_defence):
                return BatterResult.single
            else:
                return BatterResult.out
        # 5-2. 内野フライ　エラー以外はアウト確定
        if batted_ball == BattedBall.fly and field == Field.infield:
            return BatterResult.out
        # 5-3. 外野フライヒット判定（外野守備）
        if batted_ball == BattedBall.fly and field == Field.outfield:
            if self.judge_outfield_fly(outfield_defence):
                return BatterResult.out
            # 5-3-1. ヒット種類（走力）
            else:
                if self.judge_outfield_fly_hit(run):
                    return BatterResult.double
                else:
                    return BatterResult.single
        # 5-4. 内野クリーン　シングルヒット確定
        if batted_ball == BattedBall.clean and field == Field.infield:
            return BatterResult.single
        # 5-5. 外野クリーン　ヒット確定
        if batted_ball == BattedBall.clean and field == Field.outfield:
            # 5-5-1. ホームラン判定（パワー、球速）
            if self.judge_homerun(power, speed):
                return BatterResult.homerun
            # 5-5-2. ヒット種類（走力、外野守備）
            if self.judge_outfield_clean_hit(run, outfield_defence):
                return BatterResult.triple
            else:
                return BatterResult.double

        print(contact, power, run, speed, control, henka, infield_defence, outfield_defence)

        # どれにも引っかからないときはアウト
        return BatterResult.out

    # 打席結果判定用のメソッド群
    def judge_fourball(self, control):
        rand = random.random()
        # 係数
        s = 0.01
        return rand < (1 - (control * s))

    def judge_strikeout(self, contact, speed, control, henka):
        rand = random.random()
        # 係数
        s1 = 0.01
        s2 = 0.01
        s3 = 0.01
        s4 = 0.01
        return rand > (contact * s1) - (speed * s2) - (control * s3) - (henka * s4)

    def judge_batted_ball(self, contact, power, speed, control, henka):
        rand = random.random()
        # 係数
        s1 = 0.01
        s2 = 0.01
        s3 = 0.01
        s4 = 0.01
        s5 = 0.01
        if rand < (contact * s1) + (power * s2) - (speed * s3) - (control * s4) - (henka * s5):
            return BattedBall.clean
        else:
            if random.random() > 0.5:
                return BattedBall.goro
            else:
                return BattedBall.fly

    def judge_field(self, power, speed):
        rand = random.random()
        # 係数
        s1 = 0.01
        s2 = 0.01
        if rand < (power * s1) - (speed * s2):
            return Field.outfield
        else:
            return Field.infield

    def judge_infield_goro(self, run, infield_defence):
        rand = random.random()
        # 係数
        s1 = 0.01
        s2 = 0.01
        return rand < (run * s1) - (infield_defence * s2)

    def judge_outfield_fly(self, outfield_defence):
        rand = random.random()
        # 係数
        s = 0.01
        return rand < (outfield_defence * s)

    def judge_outfield_fly_hit(self, run):
        rand = random.random()
        # 係数
        s = 0.01
        return rand < (run * s)

    def judge_homerun(self, power, speed):
        rand = random.random()
        # 係数
        s1 = 0.01
        s2 = 0.01
        return rand < (power * s1) - (speed * s2)

    def judge_outfield_clean_hit(self, run, outfield_defence):
        rand = random.random()
        # 係数
        s1 = 0.01
        s2 = 0.01
        return rand < (run * s1) - (outfield_defence * s2)

    # 結果を取得する
    def get_result(self):
        action = self.judge_result()
        print(action)
        out, runner, score = update(self.out_count, self.runner, action)
        return out, runner, score


class BattedBall(Enum):
    goro = auto()
    fly = auto()
    clean = auto()


class Field(Enum):
    infield = auto()
    outfield = auto()
