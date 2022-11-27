# youre-a-square
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def is_square(n):    
  return True if (n**0.5)**2 == n else False
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
test.assert_equals(is_square( 0), True, "0 is a square number (0 * 0)")
test.assert_equals(is_square( 3), False, "3 is not a square number")
test.assert_equals(is_square( 4), True, "4 is a square number (2 * 2)")
test.assert_equals(is_square(25), True, "25 is a square number (5 * 5)")
test.assert_equals(is_square(26), False, "26 is not a square number")
