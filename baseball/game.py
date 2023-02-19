from baseball.batter_box import BatterBox
from baseball.entity.batter import Batter
from baseball.entity.pitcher import Pitcher
from baseball.entity.team import Team


class Game:
    def __init__(self, first_team: Team, second_team: Team, is_official_game=True):
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
        self.is_official_game = is_official_game

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
        # 得点の記録
        if self.first_attack_flag:
            self.first_score += self.score
            self.first_score_list.append(self.score)
        else:
            self.second_score += self.score
            self.second_score_list.append(self.score)
        # ゲームを続けるかの判定(延長戦の判定)
        if self.inning >= 9 \
                and ((not self.first_attack_flag and self.first_score != self.second_score)
                     or (self.first_attack_flag and self.first_score < self.second_score)):
            return False
        else:
            return True

    def __do_inning(self):
        attack_side_string = '表' if self.first_attack_flag else '裏'
        # print("%d回%s 開始" % (self.inning, attack_side_string))
        # イニング中のプレー処理
        while True:
            # 打席の選手のセット
            if self.first_attack_flag:
                batter: Batter = self.first_team.player_list[self.first_team_number_order]
                pitcher: Pitcher = self.second_team.pitcher
                defence_player_list = self.second_team.player_list
                self.first_team_number_order += 1
                if self.first_team_number_order == 9:
                    self.first_team_number_order = 0
            else:
                batter: Batter = self.second_team.player_list[self.second_team_number_order]
                pitcher: Pitcher = self.first_team.pitcher
                defence_player_list = self.first_team.player_list
                self.second_team_number_order += 1
                if self.second_team_number_order == 9:
                    self.second_team_number_order = 0
            # 打席結果処理
            box = BatterBox(batter, pitcher, defence_player_list, self.runner, self.out_count)
            self.out_count, self.runner, score, action = box.get_result()
            # 公式戦なら結果を記録
            if self.is_official_game:
                batter.batter_stats.count(action, score)
                pitcher.pitcher_stats.count(action, score)
            self.score += score
            if self.out_count == 3:
                break

    def get_win_team(self):
        if self.first_score >= self.second_score:
            return self.first_team
        else:
            return self.second_team

    def get_lose_team(self):
        if self.first_score >= self.second_score:
            return self.second_team
        else:
            return self.first_team

    def start_game(self):
        # イニング処理開始
        while self.continue_flag:
            # イニング中の処理
            self.__do_inning()
            # イニング終了の処理
            self.continue_flag = self.__finish_inning()
            # イニングの初期化処理
            self.__init_inning()
