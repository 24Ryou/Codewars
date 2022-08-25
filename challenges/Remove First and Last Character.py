import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def remove_char(s):
  return s[1:-1]
# ------------------------------ clever solution ----------------------------- #
# ----------------------------------- test ----------------------------------- #
@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(remove_char('eloquent'), 'loquen')
        test.assert_equals(remove_char('country'), 'ountr')
        test.assert_equals(remove_char('person'), 'erso')
        test.assert_equals(remove_char('place'), 'lac')
        test.assert_equals(remove_char('ok'), '')
        test.assert_equals(remove_char('ooopsss'), 'oopss')