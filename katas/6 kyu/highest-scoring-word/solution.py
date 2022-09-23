# highest-scoring-word
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def high(x):
  max = ''
  cal = 0
  nums = range(1,27)
  letters = 'abcdefghijklmnopqrstuvwxyz'
  table = dict(zip(letters , nums))
  for word in x.split(" "):
    count = sum(list(map(lambda x:table[x] , word)))
    if count > cal:
      cal = count
      max = word
  return max
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def high(x):
  return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
        test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
        test.assert_equals(high('take me to semynak'), 'semynak')
        test.assert_equals(high('aa b'), 'aa')
        test.assert_equals(high('b aa'), 'b')
        test.assert_equals(high('bb d'), 'bb')
        test.assert_equals(high('d bb'), 'd')
        test.assert_equals(high("aaa b"), "aaa")