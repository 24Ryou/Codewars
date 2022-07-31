import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def even_or_odd(number): return 'Even' if number%2 == 0 else 'Odd'
# ------------------------------ clever solution ----------------------------- #
def even_or_odd(number):
  return ["Even", "Odd"][number % 2]

even_or_odd=lambda n:'EOvdedn'[n%2::2]
# ----------------------------------- test ----------------------------------- #
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(even_or_odd(2), "Even")
        test.assert_equals(even_or_odd(1), "Odd")
        test.assert_equals(even_or_odd(0), "Even")
        test.assert_equals(even_or_odd(1545452), "Even")
        test.assert_equals(even_or_odd(7), "Odd")
        test.assert_equals(even_or_odd(78), "Even")
        test.assert_equals(even_or_odd(17), "Odd")
        test.assert_equals(even_or_odd(74156741), "Odd")
        test.assert_equals(even_or_odd(100000), "Even")
        test.assert_equals(even_or_odd(-123), "Odd")
        test.assert_equals(even_or_odd(-456), "Even")