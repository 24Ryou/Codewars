import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def greet(name, owner):
  return 'Hello boss' if name == owner else 'Hello guest'
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(greet('Daniel', 'Daniel'), 'Hello boss')
test.assert_equals(greet('Greg', 'Daniel'), 'Hello guest')