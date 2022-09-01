import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def find_average(numbers):
    return sum(numbers)/len(numbers)
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_average([1, 2, 3]), 2)