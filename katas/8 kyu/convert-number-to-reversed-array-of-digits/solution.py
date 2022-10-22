# convert-number-to-reversed-array-of-digits
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def digitize(n):
  return list(map(lambda x : int(x) , list(str(n))))[::-1]
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def digitize(n):
  return list(map(int, str(n)[::-1]))
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(digitize(35231),[1,3,2,5,3])
test.assert_equals(digitize(0),[0])
test.assert_equals(digitize(23582357),[7,5,3,2,8,5,3,2])
test.assert_equals(digitize(984764738),[8,3,7,4,6,7,4,8,9])
test.assert_equals(digitize(45762893920),[0,2,9,3,9,8,2,6,7,5,4])
test.assert_equals(digitize(548702838394),[4,9,3,8,3,8,2,0,7,8,4,5])