import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def reverse_seq(n):
    return sorted(list(range(1 , n+1)),reverse=True)
# ------------------------------ clever solution ----------------------------- #
def reverseseq(n):
    return list(range(n, 0, -1))
# ----------------------------------- test ----------------------------------- #
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(reverse_seq(5),[5,4,3,2,1])