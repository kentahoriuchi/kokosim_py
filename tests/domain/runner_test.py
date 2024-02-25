import pytest
from baseball.domain.runner import update
from baseball.enums.batter_result import BatterResult

# out, runner, action, expect_out, expect_runner, expect_run
no_runner_param = {
    "out": (0, 0b0000, BatterResult.out, 1, 0b0000, 0),
    "strikeout": (0, 0b0000, BatterResult.strikeout, 1, 0b0000, 0),
    "fourball": (0, 0b0000, BatterResult.fourball, 0, 0b0001, 0),
    "single": (0, 0b0000, BatterResult.single, 0, 0b0001, 0),
    "double": (0, 0b0000, BatterResult.double, 0, 0b0010, 0),
    "triple": (0, 0b0000, BatterResult.triple, 0, 0b0100, 0),
    "homurun": (0, 0b0000, BatterResult.homerun, 0, 0b0000, 1)
}


@pytest.mark.parametrize("out, runner, action, expect_out, expect_runner, expect_run", list(no_runner_param.values()),
                         ids=list(no_runner_param.keys()))
def test_no_runner(out, runner, action, expect_out, expect_runner, expect_run):
    actual_out, actual_runner, actual_run = update(out, runner, action)
    assert actual_out == expect_out
    assert actual_runner == expect_runner
    assert actual_run == expect_run


# ランナーの残り方が1種類のもの
# out, runner, action, expect_out, expect_runner, expect_run
runner_param = {
    "1_fourball": (0, 0b0001, BatterResult.fourball, 0, 0b0011, 0),
    "1_2_fourball": (0, 0b0011, BatterResult.fourball, 0, 0b0111, 0),
    "2_fourball": (0, 0b0010, BatterResult.fourball, 0, 0b0011, 0),
    "3_single": (0, 0b0100, BatterResult.single, 0, 0b0001, 1),
    "2_3_double": (0, 0b0110, BatterResult.double, 0, 0b0010, 2),
    "1_triple": (0, 0b0001, BatterResult.triple, 0, 0b0100, 1),
    "1_2_3_homurun": (0, 0b0111, BatterResult.homerun, 0, 0b0000, 4)
}


@pytest.mark.parametrize("out, runner, action, expect_out, expect_runner, expect_run", list(runner_param.values()),
                         ids=list(runner_param.keys()))
def test_runner(out, runner, action, expect_out, expect_runner, expect_run):
    actual_out, actual_runner, actual_run = update(out, runner, action)
    assert actual_out == expect_out
    assert actual_runner == expect_runner
    assert actual_run == expect_run
