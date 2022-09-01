import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def rps(p1, p2):
    rule = {'rock' : 'paper' , 'paper' : 'scissors' , 'scissors' : 'rock'}
    if p1 == p2 :
      return 'Draw!'
    return 'Player 2 won!' if p2 == rule[p1] else 'Player 1 won!'
# ------------------------------ clever solution ----------------------------- #
def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]
# ----------------------------------- test ----------------------------------- #
@test.describe("rock paper scissors")
def basic_tests():
    @test.it("Player 1 wins")
    def player_1():
        test.assert_equals(rps('rock', 'scissors'), "Player 1 won!")
    @test.it("Player 1 wins")
    def player_1():
        test.assert_equals(rps('scissors', 'rock'), "Player 2 won!")
    @test.it("Draw")
    def draw():
        test.assert_equals(rps('rock', 'rock'), 'Draw!')