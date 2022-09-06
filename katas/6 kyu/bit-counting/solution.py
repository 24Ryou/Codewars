# bit-counting
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def count_bits(n):
  return sum(1 for x in list(bin(n)[2:]) if x == '1')
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def countBits(n):
  return bin(n).count("1")
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(count_bits(0), 0)
test.assert_equals(count_bits(4), 1)
test.assert_equals(count_bits(7), 3)
test.assert_equals(count_bits(9), 2)
test.assert_equals(count_bits(10), 2)