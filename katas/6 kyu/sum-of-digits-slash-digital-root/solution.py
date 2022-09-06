# sum-of-digits-slash-digital-root
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def digital_root(n):
  n = list(str(n))
  if len(n) == 1:
    return int(n[0])
  return digital_root(sum(int(i) for i in n))
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def digital_root(n):
  return n if n < 10 else digital_root(sum(map(int,str(n))))

def digital_root(n):
  return n%9 or n and 9 
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(digital_root(16), 7)
test.assert_equals(digital_root(942), 6)
test.assert_equals(digital_root(132189), 6)
test.assert_equals(digital_root(493193), 2)