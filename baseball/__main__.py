from game import Game
from team_generator import ramdom_team_generate
from baseball.scripts.write_csv import write_csv_team


def main():
    # mainの処理
    first_team, second_team = ramdom_team_generate()
    for i in range(100):
        play_ground = Game(first_team, second_team)
        play_ground.start_game()
        first_score, second_score = play_ground.get_score()
        print("%d vs %d" %(first_score, second_score))
    write_csv_team(first_team)
    write_csv_team(second_team)


if __name__ == '__main__':
    main()

