# most-frequently-used-words-in-a-text
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
from collections import Counter
import re

def top_3_words(text):
  letters = "abcdefghijklmnopqrstuvwxyz"
  text = re.sub('[^\'a-z\s]'," " ,text.lower()).strip()
  arr = Counter(text.split())
  arr = {k:v for k,v in sorted(arr.items() , key=lambda x: x[1] , reverse=True)}
  result = []
  j = 0
  for k , v in arr.items():
    if any(i in letters for i in k):
      result.append(k)
      j += 1
    if j == 3:
      break
  return result
# ------------------------------ CLEVER SOLUTION ----------------------------- #
from collections import Counter
import re

def top_3_words(text):
  c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
  return [w for w,_ in c.most_common(3)]
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
test.assert_equals(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
test.assert_equals(top_3_words("  //wont won't won't "), ["won't", "wont"])
test.assert_equals(top_3_words("  , e   .. "), ["e"])
test.assert_equals(top_3_words("  ...  "), [])
test.assert_equals(top_3_words("  '  "), [])
test.assert_equals(top_3_words("  '''  "), [])
test.assert_equals(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])