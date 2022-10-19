# recover-a-secret-string-from-random-triplets
from unittest import result
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def recoverSecret(triplets):
  letters = list(set([l for t in triplets for l in t]))        

  for t in triplets * len(letters):
    for i in range(len(t)-1):
      a, b = letters.index(t[i]), letters.index(t[i+1])
      if( a > b ): letters[b], letters[a] = letters[a], letters[b]

  return ''.join(letters)
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def recoverSecret(triplets):
  r = list(set([i for l in triplets for i in l]))
  for l in triplets:
    fix(r, l[1], l[2])
    fix(r, l[0], l[1])
  return ''.join(r)
  
def fix(l, a, b):
  """l.index(a) < l.index(b)"""
  if l.index(a) > l.index(b):
    l.remove(a)
    l.insert(l.index(b), a)
# ----------------------------------- TEST ----------------------------------- #
secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

test.assert_equals(recoverSecret(triplets), secret)