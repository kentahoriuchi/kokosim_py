from runner import update
import entity.batter
import enums.batter_result
import random


class Game:
    def __init__(self):
        self.inning = 1
        self.score = 0
        self.first_score = 0
        self.second_score = 0
        self.first_score_list = []
        self.second_score_list = []
        self.out_count = 0
        self.runner = 0b0000
        self.first_attack_flag = True
        self.continue_flag = True

    # イニングの開始前に行う初期化処理
    def init_inning(self):
        self.out_count = 0
        self.runner = 0b0000
        self.score = 0
        if not self.first_attack_flag:
            self.inning += 1
        self.first_attack_flag = not self.first_attack_flag

    # イニングの終了時に行う処理
    def finish_inning(self):
        # 得点板に得点記録
        if self.first_attack_flag:
            self.first_score_list.append(self.score)
        else:
            self.second_score_list.append(self.score)
        # ゲームを続けるかの判定
        if self.inning == 9 and not self.first_attack_flag:
            return False
        else:
            return True

    def do_inning(self):
        attack_side_string = '表' if self.first_attack_flag else '裏'
        print("%d回%s 開始" % (self.inning, attack_side_string))
        # イニング中のプレー処理
        while self.out_count != 3:
            self.batter_box_result()
        print(self.score)


    # 打席結果の処理
    def batter_box_result(self):
        batter_result_enum = enums.batter_result.BatterResult
        if random.random() > 0.95:
            action = batter_result_enum.homerun
        elif random.random() > 0.7:
            action = batter_result_enum.single
        else:
            action = batter_result_enum.out
        print(action)
        out, runner, score = update(self.out_count, self.runner, action)
        self.out_count = out
        self.runner = runner
        self.score += score

    def start_game(self):
        print("start game")

        # イニング処理開始
        while self.continue_flag:
            # イニング中の処理
            self.do_inning()
            # イニング終了の処理
            self.continue_flag = self.finish_inning()
            # イニングの初期化処理
            self.init_inning()

        print("finish game")
        print(self.first_score_list)
        print(self.second_score_list)
