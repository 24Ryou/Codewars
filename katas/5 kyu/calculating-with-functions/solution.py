from ast import operator
from tkinter.tix import INTEGER
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def zero(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1]
    match operator:
      case '*':
        return int(0*number)
      case '+':
        return int(0+number)
      case '-':
        return int(0-number)
      case '/':
        return int(0/number)
  return 0
def one(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1] 
    match operator:
      case '*':
        return int(1*number)
      case '+':
        return int(1+number)
      case '-':
        return int(1-number)
      case '/':
        return int(1/number)
  return 1
def two(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1] 
    match operator:
      case '*':
        return int(2*number)
      case '+':
        return int(2+number)
      case '-':
        return int(2-number)
      case '/':
        return int(2/number)
  return 2
def three(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1]
    match operator:
      case '*':
        return int(3*number)
      case '+':
        return int(3+number)
      case '-':
        return int(3-number)
      case '/':
        return int(3/number) 
  return 3
def four(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1]
    match operator:
      case '*':
        return int(4*number)
      case '+':
        return int(4+number)
      case '-':
        return int(4-number)
      case '/':
        return int(4/number) 
  return 4
def five(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1] 
    match operator:
      case '*':
        return int(5*number)
      case '+':
        return int(5+number)
      case '-':
        return int(5-number)
      case '/':
        return int(5/number)
  return 5
def six(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1] 
    match operator:
      case '*':
        return int(6*number)
      case '+':
        return int(6+number)
      case '-':
        return int(6-number)
      case '/':
        return int(6/number)
  return 6
def seven(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1]
    match operator:
      case '*':
        return int(7*number)
      case '+':
        return int(7+number)
      case '-':
        return int(7-number)
      case '/':
        return int(7/number)
  return 7
def eight(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1] 
    match operator:
      case '*':
        return int(8*number)
      case '+':
        return int(8+number)
      case '-':
        return int(8-number)
      case '/':
        return int(8/number)
  return 8
def nine(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1]
    match operator:
      case '*':
        return int(9*number)
      case '+':
        return int(9+number)
      case '-':
        return int(9-number)
      case '/':
        return int(9/number) 
  return 9

def plus(number : int): 
  return str(number)+'+'
def minus(number : int): 
  return str(number)+'-'
def times(number : int): 
  return str(number)+'*'
def divided_by(number : int): 
  return str(number)+'/'
# ------------------------------ CLEVER SOLUTION ----------------------------- #
id_ = lambda x: x
number = lambda x: lambda f=id_: f(x)
zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))
plus = lambda x: lambda y: y + x
minus = lambda x: lambda y: y - x
times = lambda x: lambda y: y * x
divided_by = lambda x: lambda y: y / x
# ----------------------------------- TEST ----------------------------------- #
test.describe('Basic Tests')
test.assert_equals(seven(times(five())), 35)
test.assert_equals(four(plus(nine())), 13)
test.assert_equals(eight(minus(three())), 5)
test.assert_equals(six(divided_by(two())), 3)