# next-bigger-number-with-the-same-digits
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def next_bigger(n):
  string = list(str(n))
  for i in range(len(string) - 1, -1, -1):
    if int(string[i - 1]) > int(string[i]): continue
    else:
      string[i:] = sorted(string[i:])
      for j in range(i,len(string),1):
        if int(string[i-1]) >= int(string[j]): continue
        else: 
          string.insert(i-1,string[j])
          del string[j + 1]
          string[i:] = sorted(string[i:])
          return int("".join(string))
  return -1
# ------------------------------ CLEVER SOLUTION ----------------------------- #
import itertools
def next_bigger(n):
  s = list(str(n))
  for i in range(len(s)-2,-1,-1):
    if s[i] < s[i+1]:
      t = s[i:]
      m = min(filter(lambda x: x>t[0], t))
      t.remove(m)
      t.sort()
      s[i:] = [m] + t
      return int("".join(s))
  return -1

def next_bigger(n):
  i, ss = n, sorted(str(n))

  if str(n) == ''.join(sorted(str(n))[::-1]):
    return -1;

  while True:
    i += 1;
    if sorted(str(i)) == ss and i != n:
      return i
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(next_bigger(  12),   21)
test.assert_equals(next_bigger(  21),   -1)
test.assert_equals(next_bigger( 513),  531)
test.assert_equals(next_bigger(2017), 2071)
test.assert_equals(next_bigger( 414),  441)
test.assert_equals(next_bigger( 144),  414)