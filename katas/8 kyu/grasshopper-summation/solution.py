import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def summation(num):
  return sum(range(1 , num+1))
# ------------------------------ clever solution ----------------------------- #
def summation(num):
  return (1+num) * num / 2
# ----------------------------------- test ----------------------------------- #
@test.describe('Fixed tests')
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(summation(1), 1)
        test.assert_equals(summation(8), 36)
        test.assert_equals(summation(22), 253)
        test.assert_equals(summation(100), 5050)
        test.assert_equals(summation(213), 22791)