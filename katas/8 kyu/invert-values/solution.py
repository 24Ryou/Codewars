import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def invert(lst):
  _list = []
  for x in lst :
    if x > 0:
      _list.append(-x)
    else:
      _list.append(abs(x))
  return _list
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def invert(lst):
    return [-x for x in lst]
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Invert values")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(invert([1,2,3,4,5]),[-1,-2,-3,-4,-5])
        test.assert_equals(invert([1,-2,3,-4,5]), [-1,2,-3,4,-5])
        test.assert_equals(invert([]), [])