import codewars_test as test
import re
# -------------------------------- my solution ------------------------------- #
disemvowel = lambda x :  re.sub("[aeiouAEIOU]","",x)
# ------------------------------ clever solution ----------------------------- #
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")
# ----------------------------------- test ----------------------------------- #
@test.describe("Fixed Tests")
def basic_tests():
    @test.it("First fixed test")
    def fixed_test_1():
        test.assert_equals(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")