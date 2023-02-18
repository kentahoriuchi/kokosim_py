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
            return BatterResult.strikeout
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

        # どれにも引っかからないときはアウト
        return BatterResult.out

    # 打席結果判定用のメソッド群
    def judge_fourball(self, control):
        rand = random.random() * 100
        # 係数
        sd = 500
        max_lim = 50
        return rand < min((sd / control), max_lim)

    def judge_strikeout(self, contact, speed, control, henka):
        rand = random.random() * 100
        # 係数
        sp1 = 0.45
        sp2 = 0.2
        sp3 = 0.45
        sb = 0.9
        max_lim = 80
        return rand < min(((speed * sp1) + (control * sp2) + (henka * sp3)) - (contact * sb), max_lim)

    def judge_batted_ball(self, contact, power, speed, control, henka):
        rand = random.random() * 100
        # 係数
        sb1 = 0.5
        sb2 = 0.3
        sp1 = 0.2
        sp2 = 0.2
        sp3 = 0.2
        min_lim = 10
        max_lim = 90
        if rand < min(max(((contact * sb1) + (power * sb2)) - ((speed * sp1) + (control * sp2) + (henka * sp3)) + 25,
                          min_lim), max_lim):
            return BattedBall.clean
        else:
            if random.random() > 0.5:
                return BattedBall.goro
            else:
                return BattedBall.fly

    def judge_field(self, power, speed):
        rand = random.random() * 100
        # 係数
        sb = 0.7
        sp = 0.1
        if rand < (power * sb) - (speed * sp):
            return Field.outfield
        else:
            return Field.infield

    def judge_infield_goro(self, run, infield_defence):
        rand = random.random() * 100
        # 係数
        sb = 1
        sp = 1
        return rand < (run * sb) - (infield_defence * sp)

    def judge_outfield_fly(self, outfield_defence):
        rand = random.random() * 100
        # 係数
        s = 0.9
        return rand < (outfield_defence * s)

    def judge_outfield_fly_hit(self, run):
        rand = random.random() * 100
        # 係数
        s = 0.5
        return rand < (run * s)

    def judge_homerun(self, power, speed):
        rand = random.random() * 100
        # 係数
        sb = 0.7
        sp = 0.2
        return rand < (power * sb) - (speed * sp)

    def judge_outfield_clean_hit(self, run, outfield_defence):
        rand = random.random() * 100
        # 係数
        sb = 0.3
        sp = 0.1
        return rand < (run * sb) - (outfield_defence * sp)

    # 結果を取得する
    def get_result(self):
        action = self.judge_result()
        out, runner, score = update(self.out_count, self.runner, action)
        return out, runner, score, action


class BattedBall(Enum):
    goro = auto()
    fly = auto()
    clean = auto()


class Field(Enum):
    infield = auto()
    outfield = auto()
