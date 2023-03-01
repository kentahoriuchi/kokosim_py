import pytest
from baseball.repository.player import PlayerData


def test_テーブルが作製できる():
    player = PlayerData()
    player.create_table()
