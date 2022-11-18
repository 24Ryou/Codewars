# exclusive-or-xor-logical-operator
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def xor(a,b):
  return a != b
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(xor(False, False), False, "False xor False == False")
test.assert_equals(xor(True, False), True, "True xor False == True")
test.assert_equals(xor(False, True), True, "False xor True == True")
test.assert_equals(xor(True, True), False, "True xor True == False")
