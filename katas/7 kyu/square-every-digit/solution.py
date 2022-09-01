import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def square_digits(num) : return int(''.join(str(int(i)**2) for i in str(num)))
# ------------------------------ clever solution ----------------------------- #
square_digits = lambda num: int(''.join(str(int(d)**2) for d in str(num)))
# ----------------------------------- test ----------------------------------- #
@test.describe("Premade tests: ")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
      test.assert_equals(square_digits(9119), 811181)
      test.assert_equals(square_digits(0), 0)