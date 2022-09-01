import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def to_camel_case(text):
    output = ''.join(x for x in text.title() if x not in "_-")
    return text[0] + output[1:] if text else ''
# ----------------------------------- TEST ----------------------------------- #
test.describe("Testing function to_camel_case")
test.it("Basic tests")
test.assert_equals(to_camel_case(''), '', "An empty string was provided but not returned")
test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior","to_camel_case('the_stealth_warrior') did not return correct value")
test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior","to_camel_case('The-Stealth-Warrior') did not return correct value")
test.assert_equals(to_camel_case("A-B-C"), "ABC","to_camel_case('A-B-C') did not return correct value")
