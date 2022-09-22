# break-camelcase
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def solution(s):
  letters = 'abcdefghijklmnopqrstuvwxyz'.upper()
  _str = ''
  for x in s:
    if x in letters:
      _str += " "
    _str += x
  return _str
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def solution(s):
  return ''.join(' ' + c if c.isupper() else c for c in s)

import re
def solution(s):
  return re.sub('([A-Z])', r' \1', s)
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(solution("helloWorld"), "hello World")
test.assert_equals(solution("camelCase"), "camel Case")
test.assert_equals(solution("breakCamelCase"), "break Camel Case")
