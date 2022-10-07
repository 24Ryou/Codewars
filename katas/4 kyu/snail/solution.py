# snail
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def snail(array):
  results = []
  while len(array) > 0:
    # go right
    results += array[0]
    del array[0]

    if len(array) > 0:
      # go down
      for i in array:
        results += [i[-1]]
        del i[-1]

      # go left
      if array[-1]:
        results += array[-1][::-1]
        del array[-1]

      # go top
      for i in reversed(array):
        results += [i[0]]
        del i[0]

  return results
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def snail(array):
  out = []
  while len(array):
    out += array.pop(0)
    array = list(zip(*array))[::-1] # Rotate
  return out

import numpy as np

def snail(array):
  m = []
  array = np.array(array)
  while len(array) > 0:
      m += array[0].tolist()
      array = np.rot90(array[1:])
  return m
# ----------------------------------- TEST ----------------------------------- #
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
test.assert_equals(snail(array), expected)


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
test.assert_equals(snail(array), expected)
