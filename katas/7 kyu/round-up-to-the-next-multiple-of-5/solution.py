# round-up-to-the-next-multiple-of-5
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def round_to_next5(n):
  return n + (5 - n) % 5
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #
inp = 0
out = round_to_next5(inp)
test.assert_equals(out, 0, "Input: {}".format(inp))

inp = 1
out = round_to_next5(inp)
test.assert_equals(out, 5, "Input: {}".format(inp))

inp = -1
out = round_to_next5(inp)
test.assert_equals(out, 0, "Input: {}".format(inp))

inp = 5
out = round_to_next5(inp)
test.assert_equals(out, 5, "Input: {}".format(inp))

inp = 7
out = round_to_next5(inp)
test.assert_equals(out, 10, "Input: {}".format(inp))

inp = 20
out = round_to_next5(inp)
test.assert_equals(out, 20, "Input: {}".format(inp))

inp = 39
out = round_to_next5(inp)
test.assert_equals(out, 40, "Input: {}".format(inp))