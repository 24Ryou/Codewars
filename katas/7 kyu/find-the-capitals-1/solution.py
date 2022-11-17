# find-the-capitals-1
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def capitals(word : str):
  return [i for i,x in enumerate(word) if x.isupper()]
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals( capitals('CodEWaRs'), [0,3,4,6] )