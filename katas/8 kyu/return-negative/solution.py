import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def make_negative( number ):
    return number * -1 if number > 0 else number
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def make_negative( number ):
    return -abs(number)
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        for n, expected in ((42,-42), (-9,-9), (0,0)):
            actual = make_negative(n)
            message = f"For n = {n}, expected {expected} but got {actual}"
            test.assert_equals(actual, expected, message)