# weird-string-case
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def to_weird_case(words):
  return " ".join(["".join([x.upper() if i % 2 == 0 else x.lower() for (i , x) in enumerate(word)]) for word in words.split(" ")])
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(to_weird_case('This'), 'ThIs')
test.assert_equals(to_weird_case('is'), 'Is')
test.assert_equals(to_weird_case('THIs iS a TEST'), 'ThIs Is A TeSt')