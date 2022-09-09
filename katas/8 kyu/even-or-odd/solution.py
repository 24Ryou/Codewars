# even-or-odd
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def even_or_odd(number): return 'Even' if number%2 == 0 else 'Odd'
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def even_or_odd(number):
    return 'Odd' if number % 2 else 'Even'
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(even_or_odd(2), "Even")
test.assert_equals(even_or_odd(1), "Odd")
test.assert_equals(even_or_odd(0), "Even")
test.assert_equals(even_or_odd(1545452), "Even")
test.assert_equals(even_or_odd(7), "Odd")
test.assert_equals(even_or_odd(78), "Even")
test.assert_equals(even_or_odd(17), "Odd")
test.assert_equals(even_or_odd(74156741), "Odd")
test.assert_equals(even_or_odd(100000), "Even")
test.assert_equals(even_or_odd(-123), "Odd")
test.assert_equals(even_or_odd(-456), "Even")