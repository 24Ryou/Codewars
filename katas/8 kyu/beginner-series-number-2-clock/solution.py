# beginner-series-number-2-clock
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def past(h, m, s):
  # s -> * 1000
  # m -> s * 60
  # h -> s * 3600
  return sum([s*1000 , m*1000*60 , h*1000*3600])
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def past(h, m, s):
  return (3600*h + 60*m + s) * 1000
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(past(0,1,1),61000)
test.assert_equals(past(1,1,1),3661000)
test.assert_equals(past(0,0,0),0)
test.assert_equals(past(1,0,1),3601000)
test.assert_equals(past(1,0,0),3600000)