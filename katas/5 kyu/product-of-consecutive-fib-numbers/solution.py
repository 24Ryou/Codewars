from cgitb import text
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def productFib(prod):
  i = 0
  test = lambda i : fib(i)*fib(i+1)
  while(test(i) < prod):
    i += 1
  return [fib(i) , fib(i+1) , True] if test(i) == prod else [fib(i) , fib(i+1) , False]

def fib(n):
  if n == 0 or n == 1: return n
  x, y = 0, 1
  for i in range(n-1):
    x, y = y, x + y
  return y
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def productFib(prod):
  a, b = 0, 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(productFib(4895), [55, 89, True])
test.assert_equals(productFib(5895), [89, 144, False])