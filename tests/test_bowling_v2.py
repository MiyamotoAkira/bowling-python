import pytest
from src.bowling_python import BowlingGameV2


@pytest.fixture
def bowling():
    return BowlingGameV2()


def test_single_roll(bowling):
    bowling.roll(5)
    assert 5 == bowling.score()


def test_two_rolls(bowling):
    bowling.roll(5)
    bowling.roll(3)
    assert 8 == bowling.score()


def test_with_strike_and_follow_up_rolls(bowling):
    bowling.roll(10)
    bowling.roll(4)
    bowling.roll(3)
    assert 24 == bowling.score()


def test_with_strike_and_with_single_follow_up_roll(bowling):
    bowling.roll(10)
    bowling.roll(4)
    assert 18 == bowling.score()


def test_with_strike_and_with_no_follow_up_roll(bowling):
    bowling.roll(10)
    assert 10 == bowling.score()


def test_with_spare_and_follow_up_roll(bowling):
    bowling.roll(4)
    bowling.roll(6)
    bowling.roll(3)
    assert 16 == bowling.score()


def test_with_spare_no_follow_up_roll(bowling):
    bowling.roll(4)
    bowling.roll(6)
    assert 10 == bowling.score()


# func (suite *BowlingTestSuite) Test_WithFullGame() {
def test_with_full_game(bowling):
    # First frame
    bowling.roll(10)
    # second frame
    bowling.roll(4)
    bowling.roll(3)
    # third frame
    bowling.roll(8)
    bowling.roll(2)
    # fourth frame
    bowling.roll(10)
    # fifth frame
    bowling.roll(8)
    bowling.roll(1)
    # sixth frame
    bowling.roll(3)
    bowling.roll(3)
    # seventh frame
    bowling.roll(10)
    # eighth frame
    bowling.roll(10)
    # ninth frame
    bowling.roll(10)
    # tenth frame
    bowling.roll(6)
    bowling.roll(3)
    assert 162 == bowling.score()


def test_with_all_strikes(bowling):
    for i in range(12):
        bowling.roll(10)

    assert 300 == bowling.score()


def test_strike_on_final_frame(bowling):
    for i in range(18):
        bowling.roll(1)

    bowling.roll(10)
    bowling.roll(10)
    bowling.roll(10)

    assert 48 == bowling.score()


def test_spare_on_final_frame(bowling):
    for i in range(18):
        bowling.roll(1)

    bowling.roll(6)
    bowling.roll(4)
    bowling.roll(3)

    assert 31 == bowling.score()
