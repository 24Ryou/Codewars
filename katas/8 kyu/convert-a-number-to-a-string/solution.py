import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
number_to_string = lambda x : str(x)
# ------------------------------ CLEVER SOLUTION ----------------------------- #
number_to_string = str
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(number_to_string(67), '67')
        test.assert_equals(number_to_string(79585), '79585')
        test.assert_equals(number_to_string(79585), "79585")
        test.assert_equals(number_to_string(1+2), '3')
        test.assert_equals(number_to_string(1-2), '-1')