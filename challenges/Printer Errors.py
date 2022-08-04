from turtle import width
import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def printer_error(s):
  count = 0
  for x in s.upper():
    if ord(x) not in range(65,78):
      count += 1 
  return f'{count}/{len(s)}'
# ------------------------------ clever solution ----------------------------- #
from re import sub
def printer_error(s):
  return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

def printer_error(s):
  return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))
# ----------------------------------- test ----------------------------------- #
s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
test.assert_equals(printer_error(s), "3/56")
s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
test.assert_equals(printer_error(s), "6/60")
s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
test.assert_equals(printer_error(s) , "11/65")