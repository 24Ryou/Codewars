import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def find_average(numbers):
    return sum(numbers)/len(numbers)
# ----------------------------------- test ----------------------------------- #
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_average([1, 2, 3]), 2)