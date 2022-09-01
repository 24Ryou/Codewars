import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
    s += pow(int(c),p+i)
  return s/n if s%n==0 else -1
# ------------------------------ clever solution ----------------------------- #
dig_pow = lambda n,p : -1 if int(sum([int(x)**(p+i) for i , x in enumerate(str(n))])%n) != 0 else sum([int(x)**(p+i) for i , x in enumerate(str(n))])/n
# ----------------------------------- test ----------------------------------- #
test.assert_equals(dig_pow(89, 1), 1)
test.assert_equals(dig_pow(92, 1), -1)
test.assert_equals(dig_pow(46288, 3), 51)