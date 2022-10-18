# matrix-determinant
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
import numpy as np
def determinant(matrix):
  import numpy as np
  m = np.mat(matrix)
  c = np.linalg.det(m)
  c = int(round(c))
  return c
# ------------------------------ CLEVER SOLUTION ----------------------------- #
import numpy as np

def determinant(a):
  return round(np.linalg.det(np.matrix(a)))
# ----------------------------------- TEST ----------------------------------- #
m1 = [[4, 6], [3,8]]
m5 = [[2,4,2],[3,1,1],[1,2,0]]

test.assert_equals(determinant([[5]]), 5, "Determinant of a 1 x 1 matrix yields the value of the one element")
test.assert_equals(determinant(m1), 14, "Should return 4*8 - 3*6, i.e. 14")
test.assert_equals(determinant(m5), 10, "Should return the determinant of [[2,4,2],[3,1,1],[1,2,0]], i.e. 10")