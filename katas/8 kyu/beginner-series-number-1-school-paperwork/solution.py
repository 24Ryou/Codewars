import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def paperwork(n, m):
  return n*m if n>= 0 and m >= 0 else 0
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def paperwork(n, m):
    return max(n, 0)*max(m, 0)
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(paperwork(5,5), 25, "Failed at Paperwork(5,5)")
        test.assert_equals(paperwork(-5,5), 0, "Failed at Paperwork(-5,5)")
        test.assert_equals(paperwork(5,-5), 0, "Failed at Paperwork(5,-5)")
        test.assert_equals(paperwork(-5,-5), 0, "Failed at Paperwork(-5,-5)")
        test.assert_equals(paperwork(5,0), 0, "Failed at Paperwork(5,0)")

print(-5 * 2)