from itertools import count
from wsgiref.util import request_uri
import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def valid_parentheses(string):
  count = 0
  for x in string:
    if x == '(' :
      count += 1
    elif x == ')':
      count -= 1
    
    if count < 0 :
      return False
  if count != 0 :
    return False
  return True
# ------------------------------ clever solution ----------------------------- #
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False
# ----------------------------------- test ----------------------------------- #
@test.describe("Sample Tests")
def tests():
    @test.it("Sample tests")
    def sample_tests():
        test.assert_equals(valid_parentheses("  ("),False, "should work for '  ('")
        test.assert_equals(valid_parentheses(")test"),False, "should work for ')test'")
        test.assert_equals(valid_parentheses(""),True, "should work for ''")
        test.assert_equals(valid_parentheses("hi())("),False, "should work for 'hi())('")
        test.assert_equals(valid_parentheses("hi(hi)()"),True, "should work for 'hi(hi)()'")