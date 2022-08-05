import codewars_test as test
import re
# -------------------------------- my solution ------------------------------- #
def is_isogram(string):
  _str = 'abcdefghijklmnopqrstuvwxyz'
  if string == "":
    return True
  for x in string.lower() :
    if string.lower().count(x.lower()) > 1 or x.isdigit():
      return False
  return True
# ------------------------------ clever solution ----------------------------- #
def is_isogram(string):
    return len(string) == len(set(string.lower()))
# ----------------------------------- test ----------------------------------- #

test.assert_equals(is_isogram("Dermatoglyphics"), True )
test.assert_equals(is_isogram("isogram"), True )
test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent" )
test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case" )
test.assert_equals(is_isogram("isIsogram"), False )
test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram" )