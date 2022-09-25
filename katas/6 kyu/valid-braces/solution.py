# valid-braces
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def valid_braces(string):
  brackets = ['()', '{}', '[]']
  while any(x in string for x in brackets):
    for br in brackets:
      string = string.replace(br, '')
  return not string
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
    s=s.replace('{}','')
    s=s.replace('[]','')
    s=s.replace('()','')
  return s==''
# ----------------------------------- TEST ----------------------------------- #
def assert_valid(string):
    test.assert_equals(valid_braces(string), True, 'Expected "{0}" to be valid'.format(string))

def assert_invalid(string):
    test.assert_equals(valid_braces(string), False, 'Expected "{0}" to be invalid'.format(string))


@test.describe("Valid Braces")
def tests():
	@test.it("sample Tests")
	def sample_tests():
		assert_valid( "()" )
		assert_invalid( "(}" )
		assert_valid( "[]" )
		assert_invalid("[(])")
		assert_valid( "{}" )
		assert_valid( "{}()[]" )
		assert_valid( "([{}])" )
		assert_invalid( "([}{])" )
		assert_valid( "{}({})[]" )
		assert_valid( "(({{[[]]}}))" )
		assert_invalid( "(((({{" )
		assert_invalid( ")(}{][" )
		assert_invalid( "())({}}{()][][" )