# title-case
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def title_case(title, minor_words=''):
  title = title.capitalize().split()
  minor_words = minor_words.lower().split()
  return ' '.join([word if word in minor_words else word.capitalize() for word in title])
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(title_case(''), '')
test.assert_equals(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
test.assert_equals(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
test.assert_equals(title_case('the quick brown fox'), 'The Quick Brown Fox')