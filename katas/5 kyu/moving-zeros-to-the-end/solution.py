# moving-zeros-to-the-end
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def move_zeros(lst : list):
  n = len(lst)
  for x in lst:
    if x == 0:
      lst.remove(x)
      lst.insert(n , x)
  return lst
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def move_zeros(arr):
  l = [i for i in arr if isinstance(i, bool) or i!=0]
  return l+[0]*(len(arr)-len(l))

def move_zeros(array):
  return sorted(array, key=lambda x: x==0)
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(move_zeros(
    [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
    [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
test.assert_equals(move_zeros(
    [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
    [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
test.assert_equals(move_zeros([0, 0]), [0, 0])
test.assert_equals(move_zeros([0]), [0])
test.assert_equals(move_zeros([]), [])