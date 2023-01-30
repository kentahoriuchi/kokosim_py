import pytest
from baseball.entity.batter import Batter
from baseball.entity.pitcher import Pitcher
from baseball.batter_box import BatterBox
from data_aggregate_helper import DataAggregateHelper

import pandas as pd


def read_csv():
    test_csv = pd.read_csv('resource/batterbox_test.csv', index_col=0)
    return test_csv


def create_batter():
    return Batter.ButterBuilder().name("テスト打者").contact(50).power(50).run(50).build()


def create_pitcher():
    return Pitcher.PitcherBuilder().name("テスト投手").speed(50).control(50).henka(50).build()


def create_defence():
    return Batter.ButterBuilder().name("テスト守備").defence(50).throw(50).build()

def test_read_csv():
    test_csv = read_csv()
    print(test_csv.iloc[0].power)


def test_batterbox():
    test_csv = read_csv()
    result_average = []
    result_fourball = []
    result_strikeout = []
    result_single = []
    result_double = []
    result_triple = []
    result_homerun = []
    for test_id in range(len(test_csv)):
        test_data = test_csv.iloc[test_id]
        batter = Batter.ButterBuilder().name("テスト打者").contact(test_data.contact)\
            .power(test_data.power).run(test_data.run).build()
        pitcher = Pitcher.PitcherBuilder().name("テスト投手").speed(test_data.speed)\
            .control(test_data.control).henka(test_data.henka).build()
        defence = Batter.ButterBuilder().name("テスト守備").defence(test_data.defence)\
            .throw(test_data.throw).build()
        box = BatterBox(batter, pitcher, [defence] * 9, 0b0000, 0)
        data_helper = DataAggregateHelper()
        for _ in range(1000):
            action = box.judge_result()
            data_helper.count(action)
        result_average.append(data_helper.average())
        result_fourball.append(data_helper.fourball_prob())
        result_strikeout.append(data_helper.strikeout_prob())
        result_single.append(data_helper.single_prob())
        result_double.append(data_helper.double_prob())
        result_triple.append(data_helper.triple_prob())
        result_homerun.append(data_helper.homerun_prob())

    test_csv["average"] = pd.Series(result_average)
    test_csv["fourball"] = pd.Series(result_fourball)
    test_csv["strikeout"] = pd.Series(result_strikeout)
    test_csv["single"] = pd.Series(result_single)
    test_csv["double"] = pd.Series(result_double)
    test_csv["triple"] = pd.Series(result_triple)
    test_csv["homerun"] = pd.Series(result_homerun)

    test_csv.to_csv('resource/results/batterbox_test_result.csv', index=False)



