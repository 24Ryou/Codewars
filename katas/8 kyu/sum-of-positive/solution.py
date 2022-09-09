# sum-of-positive
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
# ----------------------------------- TEST ----------------------------------- #
@test.describe("positive_sum")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(positive_sum([1,2,3,4,5]),15)
        test.assert_equals(positive_sum([1,-2,3,4,5]),13)
        test.assert_equals(positive_sum([-1,2,3,4,-5]),9)
        
    @test.it("returns 0 when array is empty")
    def empty_case():
        test.assert_equals(positive_sum([]),0)      
        
    @test.it("returns 0 when all elements are negative")
    def negative_case():
        test.assert_equals(positive_sum([-1,-2,-3,-4,-5]),0)