import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def lovefunc( flower1, flower2 ):
    return True if flower1%2==0 and flower2%2 != 0 or flower2%2 == 0 and flower1%2 != 0 else False
# ------------------------------ clever solution ----------------------------- #
def lovefunc( flower1, flower2 ):
  return (flower1+flower2)%2

def lovefunc(flower1, flower2):
    return flower1 % 2 != flower2 % 2
# ----------------------------------- test ----------------------------------- #
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(lovefunc(1,4), True)
        test.assert_equals(lovefunc(2,2), False)
        test.assert_equals(lovefunc(0,1), True)
        test.assert_equals(lovefunc(0,0), False)