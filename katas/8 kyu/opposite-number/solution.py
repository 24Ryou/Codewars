# opposite-number
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def opposite(number):
  return -number
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(opposite(1),-1)
test.assert_equals(opposite(25.6), -25.6)
test.assert_equals(opposite(0), 0)
test.assert_equals(opposite(1425.2222), -1425.2222)
test.assert_equals(opposite(-3.1458), 3.1458)
test.assert_equals(opposite(-95858588225),95858588225)