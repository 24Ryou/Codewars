# persistent-bugger
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def persistence(n):
  r = 1
  c = 0
  t = 0
  while n > 9 :
    t = str(n)
    for i in range(len(t)) :
      r *= int(t[i])
    c += 1
    n = r
    r = 1
  return c
# ------------------------------ CLEVER SOLUTION ----------------------------- #
from functools import reduce
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Persistent Bugger.")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(persistence(39), 3)
        test.assert_equals(persistence(4), 0)
        test.assert_equals(persistence(25), 2)
        test.assert_equals(persistence(999), 4)
