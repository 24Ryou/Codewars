from itertools import count
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
count_sheeps = lambda x : x.count(True)
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)
# ----------------------------------- TEST ----------------------------------- #
array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ];
              
test.assert_equals(result := count_sheeps(array1), 17, "There are 17 sheeps in total, not %s" % result)