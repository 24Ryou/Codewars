# maximum-subarray-sum
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def max_sequence(arr):
  best_sum = 0
  current_sum = 0
  for x in arr:
      current_sum = max(0, current_sum + x)
      best_sum = max(best_sum, current_sum)
  return best_sum
# ----------------------------------- TEST ----------------------------------- #
test.describe("Tests")
test.it('should work on an empty array')   
test.assert_equals(max_sequence([]), 0)
test.it('should work on the example')
test.assert_equals(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)