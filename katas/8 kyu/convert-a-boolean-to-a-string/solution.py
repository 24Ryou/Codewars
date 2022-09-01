import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
boolean_to_string = str
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def boolean_to_string(b):
    return str(b)
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(boolean_to_string(True), "True")
        test.assert_equals(boolean_to_string(False), "False")