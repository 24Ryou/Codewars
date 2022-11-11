# give-me-a-diamond
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def diamond(n):
  if n > 0 and n % 2 == 1:
    diamond = ""
    for i in range(n):
      diamond += " " * abs(int(n/2) - i)
      diamond += "*" * (n - abs((n-1) - 2 * i))
      diamond += "\n"
    return diamond
  else:
    return None
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #

expected =  " *\n"
expected += "***\n"
expected += " *\n"
test.assert_equals(diamond(1), "*\n")
test.assert_equals(diamond(2), None)
test.assert_equals(diamond(3), expected)
test.assert_equals(diamond(5), "  *\n ***\n*****\n ***\n  *\n")
test.assert_equals(diamond(0), None)
test.assert_equals(diamond(-3), None)