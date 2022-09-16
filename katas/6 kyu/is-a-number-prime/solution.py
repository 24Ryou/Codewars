# is-a-number-prime
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def is_prime(num):
  if (num <= 1):
    return False
  for i in range(2, int(num**(0.5))+1):
    if (num % i == 0):
      return False
  return True
# ------------------------------ CLEVER SOLUTION ----------------------------- #
import random

def even_odd(n):
    s, d = 0, n
    while d % 2 == 0:
          s += 1
          d >>= 1
    return s, d

def Miller_Rabin(a, p):
    s, d = even_odd(p-1)
    a = pow(a, d, p)
    if a == 1: return True
    for i in range(s):
        if a == p-1: return True
        a = pow(a, 2, p)
    return False

def is_prime(p):
    if p == 2: return True
    if p <= 1 or p % 2 == 0: return False
    return all(Miller_Rabin(random.randint(2,p-1),p) for _ in range(40))
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Basic")
def basic():
    
    @test.it("Basic tests")
    def basic_tests():
        test.assert_equals(is_prime(0),  False, "0  is not prime")
        test.assert_equals(is_prime(1),  False, "1  is not prime")
        test.assert_equals(is_prime(2),  True, "2  is prime")
        test.assert_equals(is_prime(73), True, "73 is prime")
        test.assert_equals(is_prime(75), False, "75 is not prime")
        test.assert_equals(is_prime(-1), False, "-1 is not prime")

    
    @test.it("Test prime")
    def test_prime():
        test.assert_equals(is_prime(3),  True, "3  is prime");
        test.assert_equals(is_prime(5),  True, "5  is prime");
        test.assert_equals(is_prime(7),  True, "7  is prime");
        test.assert_equals(is_prime(41), True, "41 is prime");
        test.assert_equals(is_prime(5099), True, "5099 is prime");
        
    @test.it("Test not prime")
    def test_not_prime():
        test.assert_equals(is_prime(4),  False, "4  is not prime");
        test.assert_equals(is_prime(6),  False, "6  is not prime");
        test.assert_equals(is_prime(8),  False, "8  is not prime");
        test.assert_equals(is_prime(9), False, "9 is not prime");
        test.assert_equals(is_prime(45), False, "45 is not prime");
        test.assert_equals(is_prime(-5), False, "-5 is not prime");
        test.assert_equals(is_prime(-8), False, "-8 is not prime");
        test.assert_equals(is_prime(-41), False, "-41 is not prime");