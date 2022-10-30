# best-travel
from tkinter.messagebox import NO
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
from itertools import combinations
def choose_best_sum(t, k, ls):
  arr = combinations(ls , k)
  arr_sum = [sum(x) for x in arr if sum(x) <= t]
  return max(arr_sum) if arr_sum != [] else None
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #

test.it("Bigger numbers")
xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
test.assert_equals(choose_best_sum(230, 4, xs), 230)
test.assert_equals(choose_best_sum(430, 5, xs), 430)
test.assert_equals(choose_best_sum(430, 8, xs), None)
