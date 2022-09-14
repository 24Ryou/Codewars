# does-my-number-look-big-in-this
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def narcissistic( value ):
  sum = 0
  pow = len(str(value))
  for digit in str(value):
    sum += int(digit) ** pow
  return True if sum == value else False
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def narcissistic(value):
  return value == sum(int(x) ** len(str(value)) for x in str(value))
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(narcissistic(7), True, '7 is narcissistic');
test.assert_equals(narcissistic(371), True, '371 is narcissistic');
test.assert_equals(narcissistic(122), False, '122 is not narcissistic')
test.assert_equals(narcissistic(4887), False, '4887 is not narcissistic')