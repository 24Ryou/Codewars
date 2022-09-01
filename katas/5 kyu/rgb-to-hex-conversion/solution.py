import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def rgb(r, g, b):
  r = check(r)
  b = check(b)
  g = check(g)
  return ('%02X%02X%02X' % (r, g, b))

def check(int):
  if int >= 255:
    return 255
  if int <= 0:
    return 0
  else :
    return int
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(rgb(0,0,0),"000000", "testing zero values")
test.assert_equals(rgb(1,2,3),"010203", "testing near zero values")
test.assert_equals(rgb(255,255,255), "FFFFFF", "testing max values")
test.assert_equals(rgb(254,253,252), "FEFDFC", "testing near max values")
test.assert_equals(rgb(-20,275,125), "00FF7D", "testing out of range values")