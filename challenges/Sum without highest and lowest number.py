import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def sum_array(arr):
  if arr != None and len(arr) > 2:
    return sum(arr) - (max(arr) + min(arr))
  else: return 0
# ------------------------------ clever solution ----------------------------- #
def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0
# ----------------------------------- test ----------------------------------- #
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('None or Empty')
    def basic_test_cases():
        test.assert_equals(sum_array(None), 0)
        test.assert_equals(sum_array([]), 0)

    @test.it("Only one Element")
    def one_test_cases():
        test.assert_equals(sum_array([3]), 0)
        test.assert_equals(sum_array([-3]), 0)
        
    @test.it("Only two Element")
    def two_test_cases():
        test.assert_equals(sum_array([ 3, 5]), 0)
        test.assert_equals(sum_array([-3, -5]), 0)

    @test.it("Real Tests")
    def real_test_cases():
        test.assert_equals(sum_array([6, 2, 1, 8, 10]), 16)
        test.assert_equals(sum_array([6, 0, 1, 10, 10]), 17)
        test.assert_equals(sum_array([-6, -20, -1, -10, -12]), -28)
        test.assert_equals(sum_array([-6, 20, -1, 10, -12]), 3)