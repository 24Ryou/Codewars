# basic-mathematical-operations
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def basic_op (operator, value1, value2):
  match operator:
    case '+':
      return value1 + value2
    case '-':
      return value1 - value2
    case '*':
      return value1 * value2
    case '/':
      return value1/value2
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(basic_op('+', 4, 7), 11)
        test.assert_equals(basic_op('-', 15, 18), -3)
        test.assert_equals(basic_op('*', 5, 5), 25)
        test.assert_equals(basic_op('/', 49, 7), 7)