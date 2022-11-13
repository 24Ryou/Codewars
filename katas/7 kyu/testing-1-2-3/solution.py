# testing-1-2-3
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def number(lines):
  return [f"{i+1}: {x}" for i , x in enumerate(lines)]
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(number([]), [])
test.assert_equals(number(["a", "b", "c"]), ["1: a", "2: b", "3: c"])