from batter_box import BatterBox
from entity.team import Team


class Game:
    def __init__(self, first_team: Team, second_team: Team):
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
        self.first_team = first_team
        self.second_team = second_team
        self.first_team_number_order = 0
        self.second_team_number_order = 0

    # イニングの開始前に行う初期化処理
    def __init_inning(self):
        self.out_count = 0
        self.runner = 0b0000
        self.score = 0
        if not self.first_attack_flag:
            self.inning += 1
        self.first_attack_flag = not self.first_attack_flag

    # イニングの終了時に行う処理
    def __finish_inning(self):
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

    def __do_inning(self):
        attack_side_string = '表' if self.first_attack_flag else '裏'
        print("%d回%s 開始" % (self.inning, attack_side_string))
        # イニング中のプレー処理
        while True:
            # 打席の選手のセット
            if self.first_attack_flag:
                batter = self.first_team.player_list[self.first_team_number_order]
                pitcher = self.second_team.pitcher
                defence_player_list = self.second_team.player_list
                self.first_team_number_order += 1
                if self.first_team_number_order == 9:
                    self.first_team_number_order = 0
            else:
                batter = self.second_team.player_list[self.second_team_number_order]
                pitcher = self.first_team.pitcher
                defence_player_list = self.first_team.player_list
                self.second_team_number_order += 1
                if self.second_team_number_order == 9:
                    self.second_team_number_order = 0

            box = BatterBox(batter, pitcher, defence_player_list, self.runner, self.out_count)
            self.out_count, self.runner, score = box.get_result()
            self.score += score
            if self.out_count == 3:
                break
        print(self.score)

    def get_score(self):
        sum_first_score = sum(self.first_score_list)
        sum_second_score = sum(self.second_score_list)
        return sum_first_score, sum_second_score

    def start_game(self):
        print("start game")

        # イニング処理開始
        while self.continue_flag:
            # イニング中の処理
            self.__do_inning()
            # イニング終了の処理
            self.continue_flag = self.__finish_inning()
            # イニングの初期化処理
            self.__init_inning()

        print("finish game")
        print(self.first_score_list)
        print(self.second_score_list)
