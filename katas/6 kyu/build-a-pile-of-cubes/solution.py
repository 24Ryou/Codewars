# build-a-pile-of-cubes
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def find_nb(m):
  total = 0
  n = 0
  
  while (total < m):
    n = n + 1
    total = total + n ** 3
      
  return n if total == m else -1
# ------------------------------ CLEVER SOLUTION ----------------------------- #
from math import floor, sqrt

def find_nb(m):
  # Used the formula for the sum of cubes: m = (n(n+1)/2)^2
  # Rearranged to find n^2 + n = n(n+1) ~= n^2 ~= 2sqrt(m),
  # so take square root and round down the result.
  n_canidate = int(floor(sqrt(2 * sqrt(m))))
  if (n_canidate * (n_canidate + 1) / 2 )**2 == m:
      return n_canidate
  else:
      return -1
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(find_nb(4183059834009), 2022)
test.assert_equals(find_nb(24723578342962), -1)
test.assert_equals(find_nb(135440716410000), 4824)
test.assert_equals(find_nb(40539911473216), 3568)
test.assert_equals(find_nb(26825883955641), 3218)
