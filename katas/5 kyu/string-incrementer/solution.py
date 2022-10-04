# string-incrementer
from ast import pattern
from string import digits
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
import re
def increment_string(strng):
  pattern = '\d+$'
  letters = re.sub(pattern,"", strng)
  digits = re.search(pattern , strng)
  if digits:
    digits = digits.group()
    return letters + str(int(digits) + 1).zfill(len(digits))
  else : return strng + '1'
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def increment_string(strng):
  head = strng.rstrip('0123456789')
  print(head)
  tail = strng[len(head):]
  print(tail)
  if tail == "": return strng+"1"
  return head + str(int(tail) + 1).zfill(len(tail))
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(increment_string("foo"), "foo1")
test.assert_equals(increment_string("foobar001"), "foobar002")
test.assert_equals(increment_string("foobar1"), "foobar2")
test.assert_equals(increment_string("foobar00"), "foobar01")
test.assert_equals(increment_string("foobar99"), "foobar100")
test.assert_equals(increment_string("foobar099"), "foobar100")
test.assert_equals(increment_string("fo99obar99"), "fo99obar100")
test.assert_equals(increment_string(""), "1")