import codewars_test as test
import re
# -------------------------------- MY SOLUTION ------------------------------- #
def alphanumeric(password):
    regex = '^(?=[^\s_])[a-zA-Z0-9]+$'
    pattern = re.compile(regex)
    return bool(pattern.match(password))
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def alphanumeric(string):
    return string.isalnum()
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Sample Tests")
def sample_tests():
    tests = [
        ("hello world_", False),
        ("PassW0rd", True),
        ("     ", False)
    ]
    for s, b in tests:
        @test.it('alphanumeric("' + s + '")')
        def sample_test():
            test.assert_equals(alphanumeric(s), b)