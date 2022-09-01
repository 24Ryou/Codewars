import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
from collections import OrderedDict
def solution(n):
  conversions = OrderedDict([('M',1000), ('CM',900), ('D', 500), ('CD',400), ('C',100), ('XC',90), ('L',50), ('XL',40),('X',10), ('IX',9), ('V',5), ('IV',4), ('I',1)])
  out = ''
  for key, value in conversions.items():
    while n >= value:
      out += key
      n -= value
  return out
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(solution(1),'I', "solution(1),'I'")
test.assert_equals(solution(4),'IV', "solution(4),'IV'")
test.assert_equals(solution(6),'VI', "solution(6),'VI'")
test.assert_equals(solution(14),'XIV', "solution(14),'XIV")
test.assert_equals(solution(21),'XXI', "solution(21),'XXI'")
test.assert_equals(solution(89),'LXXXIX', "solution(89),'LXXXIX'")
test.assert_equals(solution(91),'XCI', "solution(91),'XCI'")
test.assert_equals(solution(984),'CMLXXXIV', "solution(984),'CMLXXXIV'")
test.assert_equals(solution(1000), 'M', 'solution(1000), M')
test.assert_equals(solution(1889),'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
test.assert_equals(solution(1989),'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")