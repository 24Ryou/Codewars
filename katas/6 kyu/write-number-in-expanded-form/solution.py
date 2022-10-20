# write-number-in-expanded-form
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def expanded_form(num):
  result = []

  for index, digit in enumerate(str(num)[::-1]):
    if int(digit) != 0:
      result.append(digit + ('0' * index))

  return ' + '.join(result[::-1])
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def expanded_form(num):
  num = list(str(num))
  return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(expanded_form(12), '10 + 2');
test.assert_equals(expanded_form(42), '40 + 2');
test.assert_equals(expanded_form(70304), '70000 + 300 + 4');