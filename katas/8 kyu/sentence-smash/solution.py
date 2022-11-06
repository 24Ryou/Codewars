# sentence-smash
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def smash(words):
  return " ".join(words)
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(smash([]), "")
test.assert_equals(smash(["hello"]), "hello")
test.assert_equals(smash(["hello", "world"]), "hello world")
test.assert_equals(smash(["hello", "amazing", "world"]), "hello amazing world")
test.assert_equals(smash(["this", "is", "a", "really", "long", "sentence"]), "this is a really long sentence")