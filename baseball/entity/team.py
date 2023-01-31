from baseball.entity.pitcher import Pitcher


class Team:

    def __init__(self):
        self.name = "デフォルトチーム"
        self.player_list = []
        self.pitcher = Pitcher
        self.games = []

    def set_name(self, name):
        self.name = name

    def set_players(self, player_list):
        self.player_list = player_list
        if len(player_list) > 9:
            raise ValueError("player list length must be less than 9")

    def add_player(self, player):
        if len(self.player_list) == 9:
            raise ValueError("cannot add player for player list over 9")
        self.player_list.add(player)

    def set_pitcher(self, pitcher):
        self.pitcher = pitcher

    def add_game(self, game):
        self.games.append(game)
