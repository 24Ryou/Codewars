# count-the-smiley-faces
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
import itertools
def count_smileys(arr):
  c = 0
  eye = [':' , ';']
  nose = ['' , '-' , '~']
  mouth = [')' , 'D']
  allowlist = ["".join(x) for x in itertools.product(eye,nose,mouth)]
  for x in arr:
    if x in allowlist:
      c += 1
  return c
# ------------------------------ CLEVER SOLUTION ----------------------------- #
from re import findall
def count_smileys(arr):
  return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))
# ----------------------------------- TEST ----------------------------------- #
test.describe("Basic tests")
test.assert_equals(count_smileys([]), 0)
test.assert_equals(count_smileys([':D',':~)',';~D',':)']), 4)
test.assert_equals(count_smileys([':)',':(',':D',':O',':;']), 2)
test.assert_equals(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)