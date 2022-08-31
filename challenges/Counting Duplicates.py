import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def duplicate_count(text):
  chars = set(text.lower())
  times = [text.lower().count(char) for char in chars]
  return sum(1 for v in times if v > 1)
# ------------------------------ clever solution ----------------------------- #
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
# ----------------------------------- test ----------------------------------- #
test.assert_equals(duplicate_count(""), 0)
test.assert_equals(duplicate_count("abcde"), 0)
test.assert_equals(duplicate_count("abcdeaa"), 1)
test.assert_equals(duplicate_count("abcdeaB"), 2)
test.assert_equals(duplicate_count("Indivisibilities"), 2)