from inspect import stack
import codewars_test as test
from collections import deque
# -------------------------------- my solution ------------------------------- #
def tower_builder(n_floor):
  result = []
  width = (n_floor * 2) - 1
  for x in range(1, 2 * n_floor, 2):
      stars = x * '*'
      line = stars.center(width)
      result.append(line)
  return result
# ------------------------------ clever solution ----------------------------- #
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
# ----------------------------------- test ----------------------------------- #
@test.describe("Build Tower")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(tower_builder(1), ['*', ])
        test.assert_equals(tower_builder(2), [' * ', '***'])
        test.assert_equals(tower_builder(3), ['  *  ', ' *** ', '*****'])