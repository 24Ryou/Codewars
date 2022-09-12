# find-the-parity-outlier
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def find_outlier(integers):
  a = [x for x in integers if x % 2 == 0]
  return [x for x in integers if x % 2 != 0 ][0] if len(a) > 1 else a[0]
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)