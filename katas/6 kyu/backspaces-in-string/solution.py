# backspaces-in-string
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def clean_string(s):
  output = ''
  for letter in s:
    if letter == '#':
      output = output[:-1]
    else:
      output += letter
  return output
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(clean_string('abc#d##c'), "ac")
test.assert_equals(clean_string('abc####d##c#'), "" )
test.assert_equals(clean_string("#######"), "" )
test.assert_equals(clean_string(""), "" )