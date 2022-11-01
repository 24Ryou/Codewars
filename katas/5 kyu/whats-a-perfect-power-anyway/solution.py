# whats-a-perfect-power-anyway
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def isPP(n):
  for i in range(2, int(n**.5) + 1):
    number = n
    times = 0
    while number % i == 0:
      number /= i
      times += 1
      if number == 1:
        return [i, times]
  return None
# ------------------------------ CLEVER SOLUTION ----------------------------- #
from math import ceil, log, sqrt

def isPP(n):
  for b in range(2, int(sqrt(n)) + 1):
    e = int(round(log(n, b)))
    if b ** e == n:
      return [b, e]
  return None
# ----------------------------------- TEST ----------------------------------- #
from random import random, randrange
from math import log, floor

test.describe("perfect powers")
test.it("should work for some examples")
test.assert_equals(isPP(4), [2,2], "4 = 2^2")
test.assert_equals(isPP(9), [3,2], "9 = 3^2")
test.assert_equals(isPP(5), None, "5 isn't a perfect power")

test.it("should work for the first perfect powers")
pp = [4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, 216, 225, 243, 256, 289, 324, 343, 361, 400, 441, 484]
for item in pp:
    test.expect(isPP(item) != None, "the perfect power "+str(item)+" wasn't recognized as one")

test.it("should work for random perfect powers")
for i in range(100):
    m = 2 + floor(random() * 255)
    k = 2 + floor(random() * log(268435455) / log(m))
    l = m**k
    r = isPP(l)
    if r==None:
        test.expect(r != None, str(l) + " is a perfect power")
        break
    elif r[0]**r[1] != l:
        test.assert_equals(r[0]**r[1], l, "your pair (" + str(r[0]) + ", "+ str(r[1])+ ") doesn't work for "+ str(l))
        break
      
        
test.it("should return valid pairs for random inputs")
for i in range(100):
    l = randrange(65535);
    r = isPP(l);
    if r != None and r[0]**r[1] != l:
        test.assert_equals(r[0]**r[1], l, "your pair ("+str(r[0])+", "+str(r[1])+") doesn't work for "+str(l))
        break