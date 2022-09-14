# last-digit-of-a-huge-number
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
# watch https://www.youtube.com/watch?v=k7rm55Sw-SE
# read https://www.geeksforgeeks.org/find-last-digit-of-ab-for-large-numbers/
def last_digit(lst):
  if lst == []:
    return 1
  r = 1
  for num in lst[::-1]:
    r = num ** (r if r < 4 else r % 4 + 4)
  return r % 10
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def last_digit(lst):
    n = 1
    for x in reversed(lst):
        n = x ** (n if n < 4 else n % 4 + 4)
    return n % 10
# ----------------------------------- TEST ----------------------------------- #
test.it('Basic tests')
test_data = [
    ([], 1),
    ([0, 0], 1),
    ([0, 0, 0], 0),
    ([1, 2], 1),
    ([3, 4, 5], 1),
    ([4, 3, 6], 4),
    ([7, 6, 21], 1),
    ([12, 30, 21], 6),
    ([2, 2, 2, 0], 4),
    ([937640, 767456, 981242], 0),
    ([123232, 694022, 140249], 6),
    ([499942, 898102, 846073], 6)
]
for test_input, test_output in test_data:
    test.assert_equals(last_digit(test_input), test_output)