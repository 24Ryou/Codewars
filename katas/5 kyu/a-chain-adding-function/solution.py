# a-chain-adding-function
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
class add(int):
  def __call__(self , n):
    return add(self + n)
# ----------------------------------- TEST ----------------------------------- #
@test.it("Basic tests")
def _():
    test.assert_equals(add(1), 1)
    test.assert_equals(add(1)(2), 3)
    test.assert_equals(add(1)(2)(3), 6)