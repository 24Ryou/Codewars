# number-of-trailing-zeros-of-n
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def zeros(n):
  if(n < 0):
    return -1

  count = 0

  while(n >= 5):
    n //= 5
    count += n

  return count
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def zeros(n):
  return n/5 + zeros(n/5) if n >= 5 else 0
# ----------------------------------- TEST ----------------------------------- #
test.describe("Sample Tests")
test.it("Should pass sample tests")
test.assert_equals(zeros(0), 0, "Testing with n = 0")
test.assert_equals(zeros(6), 1, "Testing with n = 6")
test.assert_equals(zeros(30), 7, "Testing with n = 30")