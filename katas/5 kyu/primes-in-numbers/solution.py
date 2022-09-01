import time
import codewars_test as test
start_time = time.time()
# -------------------------------- my solution ------------------------------- #
def prime_factors(n):
  i = 2
  res = {}
  while n/i != 1:
    if n%i == 0:
      if i in res:
        res[i] = res[i]+1
      else:
        res[i] = 1
      n = n/i
    else:
      i+=1
  if i in res:
    res[i] = res[i]+1
  else:
    res[i] = 1
  t = ''
  res = sorted(res.items(),key = lambda a:a[0])
  for key in res:
    if key[1] == 1:
      t = t + '('+str(key[0]) +')'
    else:
      t = t + '(' +str(key[0]) + '**' + str(key[1]) + ')'
  return t
# ------------------------------ clever solution ----------------------------- #
def prime_factors(n):
  i, j, p = 2, 0, []
  while n > 1:
    while n % i == 0: n, j = n / i, j + 1
    if j > 0: p.append([i,j])
    i, j = i + 1, 0
  return ''.join('(%d' %q[0] + ('**%d' %q[1]) * (q[1] > 1) + ')' for q in p)
# ----------------------------------- test ----------------------------------- #
@test.describe('Testing...')
def _():
    @test.it('Fixed tests')
    def _():
        test.assert_equals(prime_factors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")
        test.assert_equals(prime_factors(7919), "(7919)")

print("--- %s seconds ---" % (time.time() - start_time))