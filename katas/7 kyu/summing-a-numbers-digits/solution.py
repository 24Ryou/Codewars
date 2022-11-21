# summing-a-numbers-digits
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def sum_digits(number):
  return sum([int(d) for d in str(number) if d.isnumeric()])
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(sum_digits(10), 1)
test.assert_equals(sum_digits(99), 18)
test.assert_equals(sum_digits(-32), 5)