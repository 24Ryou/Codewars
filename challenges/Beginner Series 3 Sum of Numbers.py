import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def get_sum(a,b):
  return sum(range(min(a,b),max(a,b)+1))
# ------------------------------ clever solution ----------------------------- #
def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2
# ----------------------------------- test ----------------------------------- #
@test.describe('Sum of numbers')
def desc1():
    @test.it('Sample tests')
    def it1():
        test.assert_equals(get_sum(0,1),1)
        test.assert_equals(get_sum(0,-1),-1)