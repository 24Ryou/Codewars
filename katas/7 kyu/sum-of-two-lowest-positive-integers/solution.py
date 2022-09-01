import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[0:2])
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
        test.assert_equals(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
        test.assert_equals(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)