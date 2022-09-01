import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def descending_order(num) :
  return int(''.join(sorted(list(str(num)) , reverse=True)))
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(descending_order(0), 0)
        test.assert_equals(descending_order(15), 51)
        test.assert_equals(descending_order(123456789), 987654321)