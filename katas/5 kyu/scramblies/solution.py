# scramblies
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def scramble(s1 : str, s2 : str):
  for c in set(s2):
    if s1.count(c) < s2.count(c):
      return False
  return True
# ------------------------------ CLEVER SOLUTION ----------------------------- #
from collections import Counter
def scramble(s1,s2):
  # Counter basically creates a dictionary of counts and letters
  # Using set subtraction, we know that if anything is left over,
  # something exists in s2 that doesn't exist in s1
  return len(Counter(s2)- Counter(s1)) == 0
# ----------------------------------- TEST ----------------------------------- #
def dotest(s1, s2, expected):
    actual = scramble(s1, s2)
    test.assert_equals(actual, expected, f"With\ns1 = \"{s1}\"\ns2 = \"{s2}\"")


@test.describe("Tests")
def test_group():
    @test.it("Sample tests")
    def test_case():
        for s1, s2, expected in [
            ('rkqodlw', 'world', True),
            ('cedewaraaossoqqyt', 'codewars', True),
            ('katas', 'steak', False),
            ('scriptjava', 'javascript', True),
            ('scriptingjava', 'javascript', True)
        ]:
            dotest(s1, s2, expected)
            