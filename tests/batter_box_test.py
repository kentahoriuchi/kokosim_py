import pytest
from baseball.entity.batter import Butter
from baseball.entity.pitcher import Pitcher
from baseball.batter_box import BatterBox
from baseball.enums.batter_result import BatterResult
from data_aggregate_helper import DataAggregateHelper


@pytest.fixture
def create_normal_batter():
    return Butter.ButterBuilder().name("テスト打者").contact(50).power(50).run(50).build()


@pytest.fixture
def create_normal_pitcher():
    return Pitcher.PitcherBuilder().name("テスト投手").speed(50).control(100).henka(50).build()


@pytest.fixture
def create_normal_defence():
    return Butter.ButterBuilder().name("テスト守備").defence(50).throw(50).build()


def test_平均的な打者vs平均的な投手(create_normal_batter, create_normal_pitcher, create_normal_defence):
    box = BatterBox(create_normal_batter, create_normal_pitcher, [create_normal_defence] * 9, 0b0000, 0)
    data_helper = DataAggregateHelper()
    for _ in range(1000):
        action = box.judge_result()
        data_helper.count(action)

    print(data_helper.average(), data_helper.homerun())
    assert 0.3 < data_helper.average() < 0.5
    assert 100 < data_helper.homerun() < 200
