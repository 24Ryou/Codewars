# permutations
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
import itertools as iter
def permutations(s):
  return list(set(["".join(x) for x in iter.permutations(s)]))
# ------------------------------ CLEVER SOLUTION ----------------------------- #
import itertools
def permutations(string):
  return list("".join(p) for p in set(itertools.permutations(string)))
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Basic Tests")
def basic_tests():
    
  @test.it("Basic Tests")
  def basic_tests():
    test.assert_equals(sorted(permutations('a')), ['a']);
    test.assert_equals(sorted(permutations('ab')), ['ab', 'ba'])
    test.assert_equals(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])