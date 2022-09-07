# human-readable-time
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def make_readable(seconds):
  h = seconds/3600
  m = (h - int(h)) * 60
  s = (m - int(m)) * 60
  return "{}:{}:{}".format(str(int(h)).zfill(2),str(int(m)).zfill(2),str(round(s)).zfill(2))
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def make_readable(s):
  return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(make_readable(0), "00:00:00")
test.assert_equals(make_readable(5), "00:00:05")
test.assert_equals(make_readable(60), "00:01:00")
test.assert_equals(make_readable(86399), "23:59:59")
test.assert_equals(make_readable(359999), "99:59:59")