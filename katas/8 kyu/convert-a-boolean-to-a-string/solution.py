import codewars_test as test
# -------------------------------- my solution ------------------------------- #
boolean_to_string = str
# ------------------------------ clever solution ----------------------------- #
def boolean_to_string(b):
    return str(b)
# ----------------------------------- test ----------------------------------- #
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(boolean_to_string(True), "True")
        test.assert_equals(boolean_to_string(False), "False")