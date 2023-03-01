from baseball.baseball_game import BaseballGame
from baseball.scripts.team_generator import gauss_random_team_generate
from random import shuffle


class Tournament:

    def __init__(self, team_num):
        self.team_num = team_num
        self.teams = []

    def random_team_generator(self):
        for _ in range(self.team_num):
            team = gauss_random_team_generate()
            self.teams.append(team)

    def pick_two_teams(self, teams):
        two_teams = teams[:2]
        other = teams[2:]
        return two_teams, other

    def tournament(self):
        # 初期化処理
        teams_list = self.teams
        next_team = teams_list
        while True:
            if len(next_team) == 1:
                champion = next_team[0]
                break
            elif len(next_team) == 4:
                best4 = next_team
            shuffle(next_team)
            teams_list = next_team
            next_team = []
            while True:
                if len(teams_list) < 2:
                    if len(teams_list) == 1:
                        next_team.append(teams_list[0])
                    break
                two_teams, teams_list = self.pick_two_teams(teams_list)
                # if len(teams_list) >= 64:
                #     game = BaseballGame(two_teams[0], two_teams[1], is_official_game=False)
                # else:
                game = BaseballGame(two_teams[0], two_teams[1])
                game.start_game()
                win_team = game.get_win_team()
                win_team.add_game(game)
                next_team.append(win_team)

        print(champion.name)
        return champion, best4


