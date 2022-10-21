# reversed-strings
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def solution(string):
  return string[::-1]
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(solution('world'), 'dlrow')
test.assert_equals(solution('hello'), 'olleh')
test.assert_equals(solution(''), '')
test.assert_equals(solution('h'), 'h')