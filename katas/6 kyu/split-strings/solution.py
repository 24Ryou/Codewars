# split-strings
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def solution(s):
  return [s[i:i+2].ljust(2, "_") for i in range(0, len(s), 2)]
# ------------------------------ CLEVER SOLUTION ----------------------------- #
import re

def solution(s):
    return re.findall(".{2}", s + "_")
# ----------------------------------- TEST ----------------------------------- #
test.describe("Example Tests")

tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

for inp, exp in tests:
    test.assert_equals(solution(inp), exp)