import pytest
from src.bowling_python import BowlingGameV1


@pytest.fixture
def bowling():
    return BowlingGameV1()


def test_single_roll(bowling):
    bowling.roll(5)
    assert 5 == bowling.score()


# func (suite *BowlingTestSuite) Test_TwoRolls() {
# 	bowling.Roll(5)
# 	bowling.Roll(5)
# 	assert.Equal(suite.T(), 10, bowling.Score())
# }

# func (suite *BowlingTestSuite) Test_WithStrikeAndFollowUpRolls() {
# 	bowling.Roll(10)
# 	bowling.Roll(4)
# 	bowling.Roll(3)
# 	assert.Equal(suite.T(), 24, bowling.Score())
# }

# func (suite *BowlingTestSuite) Test_WithStrikeAndWithSingleFollowUpRoll() {
# 	bowling.Roll(10)
# 	bowling.Roll(4)
# 	assert.Equal(suite.T(), 18, bowling.Score())
# }

# func (suite *BowlingTestSuite) Test_WithStrikeAndWithNoFollowUpRoll() {
# 	bowling.Roll(10)
# 	assert.Equal(suite.T(), 10, bowling.Score())
# }

# func (suite *BowlingTestSuite) Test_WithSpareAndFollowUpRoll() {
# 	bowling.Roll(4)
# 	bowling.Roll(6)
# 	bowling.Roll(3)
# 	assert.Equal(suite.T(), 16, bowling.Score())
# }

# func (suite *BowlingTestSuite) Test_WithSpareNoFollowUpRoll() {
# 	bowling.Roll(4)
# 	bowling.Roll(6)
# 	assert.Equal(suite.T(), 10, bowling.Score())
# }

# func (suite *BowlingTestSuite) Test_WithFullGame() {
# 	bowling.Roll(10)
# 	bowling.Roll(4)
# 	bowling.Roll(3)
# 	bowling.Roll(8)
# 	bowling.Roll(2)
# 	bowling.Roll(10)
# 	bowling.Roll(8)
# 	bowling.Roll(1)
# 	bowling.Roll(3)
# 	bowling.Roll(3)
# 	bowling.Roll(10)
# 	bowling.Roll(10)
# 	bowling.Roll(10)
# 	bowling.Roll(6)
# 	bowling.Roll(3)
# 	assert.Equal(suite.T(), 162, bowling.Score())
# }

# func (suite *BowlingTestSuite) Test_WithAllStrikes() {
# 	for i := 0; i < 12; i++ {
# 		bowling.Roll(10)
# 	}

# 	assert.Equal(suite.T(), 300, bowling.Score())
# }

# func (suite *BowlingTestSuite) Test_StrikeOnFinalFrame() {
# 	for i := 0; i < 18; i++ {
# 		bowling.Roll(1)
# 	}
# 	bowling.Roll(10)
# 	bowling.Roll(10)
# 	bowling.Roll(10)

# 	assert.Equal(suite.T(), 48, bowling.Score())
# }

# func (suite *BowlingTestSuite) Test_SpareOnFinalFrame() {
# 	for i := 0; i < 18; i++ {
# 		bowling.Roll(1)
# 	}
# 	bowling.Roll(6)
# 	bowling.Roll(4)
# 	bowling.Roll(3)

# 	assert.Equal(suite.T(), 31, bowling.Score())
# }

# func BenchmarkFullGame(b *testing.B) {
# 	for i := 0; i < b.N; i++ {
# 		bowling.StartNewGame()
# 		for b := 0; b < 21; b++ {
# 			bowling.Roll(i % 5)
# 		}
# 		bowling.Score()
# 	}
# }
