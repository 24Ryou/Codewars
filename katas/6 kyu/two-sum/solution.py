# two-sum
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def two_sum(numbers, target):
  for i in range(0 , len(numbers)-1):
    for j in range(i+1, len(numbers)):
      if numbers[i] + numbers[j] == target: return [i , j]
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def two_sum(nums, t):
  for i, x in enumerate(nums):
    for j, y in enumerate(nums):
      if i != j and x + y == t:
        return [i, j]
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(sorted(two_sum([1,2,3], 4)), [0,2])
test.assert_equals(sorted(two_sum([1234,5678,9012], 14690)), [1,2])
test.assert_equals(sorted(two_sum([2,2,3], 4)), [0,1])