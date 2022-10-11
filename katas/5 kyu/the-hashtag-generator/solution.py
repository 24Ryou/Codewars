# the-hashtag-generator
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def generate_hashtag(s):
  s = '#'+s.title()
  s = ''.join(s.split())
  if len(s) in range(2,140):
    return s
  else:    
    return False
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def generate_hashtag(s):
  output = "#"
  
  for word in s.split():
      output += word.capitalize()
  
  return False if (len(s) == 0 or len(output) > 140) else output

def generate_hashtag(s):
  ans = '#'+ str(s.title().replace(' ',''))
  return s and not len(ans)>140 and ans or False
# ----------------------------------- TEST ----------------------------------- #
test.describe("Basic tests")
test.assert_equals(generate_hashtag(''), False, 'Expected an empty string to return False')
test.assert_equals(generate_hashtag('Do We have A Hashtag')[0], '#', 'Expeted a Hashtag (#) at the beginning.')
test.assert_equals(generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')
test.assert_equals(generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')
test.assert_equals(generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')
test.assert_equals(generate_hashtag('codewars is nice'), '#CodewarsIsNice', 'Should capitalize first letters of words.')
test.assert_equals(generate_hashtag('CodeWars is nice'), '#CodewarsIsNice', 'Should capitalize all letters of words - all lower case but the first.')
test.assert_equals(generate_hashtag('c i n'), '#CIN', 'Should capitalize first letters of words even when single letters.')
test.assert_equals(generate_hashtag('codewars  is  nice'), '#CodewarsIsNice', 'Should deal with unnecessary middle spaces.')
test.assert_equals(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'), False, 'Should return False if the final word is longer than 140 chars.')