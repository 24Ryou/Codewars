# convert-a-number-to-a-string
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
number_to_string = lambda x : str(x)
# ------------------------------ CLEVER SOLUTION ----------------------------- #
number_to_string = str
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(number_to_string(67), '67')
test.assert_equals(number_to_string(79585), '79585')
test.assert_equals(number_to_string(79585), "79585")
test.assert_equals(number_to_string(1+2), '3')
test.assert_equals(number_to_string(1-2), '-1')