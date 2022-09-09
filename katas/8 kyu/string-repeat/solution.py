# string-repeat
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
repeat_str = lambda a,b : a*b
# ----------------------------------- TEST ----------------------------------- #
@test.describe('Fixed tests')
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(repeat_str(4, 'a'), 'aaaa')
        test.assert_equals(repeat_str(3, 'hello '), 'hello hello hello ')
        test.assert_equals(repeat_str(2, 'abc'), 'abcabc')