from game import Game
from team_generator import normal_team_generate


def main():
    # mainの処理
    first_team, second_team = normal_team_generate()
    play_ground = Game(first_team, second_team)
    play_ground.start_game()
    first_score, second_score = play_ground.get_score()
    print("%d vs %d" %(first_score, second_score))


if __name__ == '__main__':
    main()

