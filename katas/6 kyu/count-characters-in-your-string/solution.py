# count-characters-in-your-string
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def count(string):
  r = {}
  for word in string:
    if word not in r: r[word] = 1
    else: r[word] += 1
  return r
# ------------------------------ CLEVER SOLUTION ----------------------------- #
from collections import Counter

def count(string):
  return Counter(string)
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(count('aba'), {'a': 2, 'b': 1})
test.assert_equals(count(''), {})