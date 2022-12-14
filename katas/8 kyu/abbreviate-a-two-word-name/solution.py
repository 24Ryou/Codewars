# abbreviate-a-two-word-name
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
abbrev_name = lambda x: ".".join([x[0] , x.split(" ")[1][0]]).upper()
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(abbrev_name("Sam Harris"), "S.H")
        test.assert_equals(abbrev_name("patrick feenan"), "P.F")
        test.assert_equals(abbrev_name("Evan C"), "E.C")
        test.assert_equals(abbrev_name("P Favuzzi"), "P.F")
        test.assert_equals(abbrev_name("David Mendieta"), "D.M")