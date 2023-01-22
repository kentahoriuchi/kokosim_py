import random
import enums.batter_result


def get_score(runner):
    run = bin(runner & 0b1111000).count('1')  # 第3ビット以上で1がたっているビット数が得点
    runner = runner & 0b111  # 第0−2ビットに残っているのがランナー

    return run, runner


def update(out, runner, action):
    batter_result_enum = enums.batter_result.BatterResult
    if action == batter_result_enum.out:  # アウト
        out += 1
    elif action == batter_result_enum.fourball:  # 四死球：ランナーを1つ進塁して1塁走者をおく
        runner = runner << 1
        runner = runner | 0b0001
    elif action == batter_result_enum.sacrifice:  # 犠打：ランナーを1つ進塁(左シフト)してアウトカウントを1つ増やす
        runner = runner << 1
        out += 1
    elif action == batter_result_enum.single:  # ヒット：ランナーを1つあるいは2つ進塁して1塁走者をおく(第0ビットをたてる)
        if random.random() > 0.5:
            runner = runner << 1
        else:
            runner = runner << 2
        runner = runner | 0b0001
    elif action == batter_result_enum.double:  # 2塁打: ランナーを2つあるいは3つ進塁して2塁走者をおく
        if random.random() > 0.5:
            runner = runner << 2
        else:
            runner = runner << 3
        runner = runner | 0b0010
    elif action == batter_result_enum.triple:  # 3塁打: ランナーを3つ進塁して3塁走者をおく
        runner = runner << 3
        runner = runner | 0b0100
    elif action == batter_result_enum.homerun:  # ホームラン： ランナーを4つ進塁し第3ビットをたてる
        runner = runner << 4
        runner = runner | 0b1000

    run, runner = get_score(runner)  # アクションの結果入った得点を計算

    return out, runner, run
