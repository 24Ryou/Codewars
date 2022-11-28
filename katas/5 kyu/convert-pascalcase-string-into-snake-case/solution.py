# convert-pascalcase-string-into-snake-case
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def to_underscore(string):
  res = ""
  if type(string) != str : return str(string)
  for x in string:
    if x.isalpha() and x == x.upper():
      res += "_" + x.lower()
    else : 
      res += x
  return res[1:]
# ------------------------------ CLEVER SOLUTION ----------------------------- #
import re

def to_underscore(string):
  return re.sub(r'(.)([A-Z])', r'\1_\2', str(string)).lower()   
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(to_underscore("TestController"), "test_controller")
test.assert_equals(to_underscore("MoviesAndBooks"), "movies_and_books")
test.assert_equals(to_underscore("App7Test"), "app7_test")
test.assert_equals(to_underscore(1), "1")