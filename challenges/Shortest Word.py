import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def find_short(s):
  mini = 100
  for x in s.split():
    if len(x) < mini:
      mini = len(x)
  return mini 
# ------------------------------ clever solution ----------------------------- #
def find_short(s):
    return min(len(x) for x in s.split())
# ----------------------------------- test ----------------------------------- #
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
        test.assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
        test.assert_equals(find_short("lets talk about javascript the best language"), 3)
        test.assert_equals(find_short("i want to travel the world writing code one day"), 1)
        test.assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)   
        test.assert_equals(find_short("Let's travel abroad shall we"), 2)