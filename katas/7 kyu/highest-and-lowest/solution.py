import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def high_and_low(numbers):
  num = [int(x) for x in numbers.split()]
  return f'{max(num)} {min(num)}'
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def high_and_low(numbers):
  return " ".join(x(numbers.split(), key=int) for x in (max, min))
# ----------------------------------- TEST ----------------------------------- #

test.assert_equals(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"), "42 -9");
test.assert_equals(high_and_low("1 2 3"), "3 1");