from game import Game


def main():
    game = Game()
    # ゲームの起動時処理
    game.start()
    # ゲーム中処理
    game.do()
    # ゲーム終了時処理
    game.finish()


if __name__ == '__main__':
    main()
