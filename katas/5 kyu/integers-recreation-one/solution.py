# integers-recreation-one
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def list_squared(m, n):
  return [[x,int(is_sqr(x))] for x in range(m,n+1) if is_sqr(x) != None]

def divisors(n):
  result = set()
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      result.add(i)
      result.add(n//i)
  return list(result)

def is_sqr(num):
  n = sum(x**2 for x in divisors(num))
  sqr = int(n**0.5)
  return n if sqr**2 == n else None
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #
@test.describe('Tests...')
def _():
  @test.it('Fixed Tests')
  def _():
    test.assert_equals(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
    test.assert_equals(list_squared(42, 250), [[42, 2500], [246, 84100]])
    test.assert_equals(list_squared(250, 500), [[287, 84100]])