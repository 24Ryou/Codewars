# bouncing-balls
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def bouncing_ball(h, bounce, window):
  if h > 0 and 0 < bounce < 1 and window < h: 
    count = 1
    current = h*bounce
    while current > window:
      current *= bounce
      count += 2
    return count 
  else : return -1
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def bouncingBall(h, bounce, window):
  seen = -1
  if 0 < bounce < 1:
    while h > window > 0:
      seen += 2
      h *= bounce
  return seen

def bouncingBall(h, bounce, window):
  if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
    return -1
  return 2 + bouncingBall(h * bounce, bounce, window)
# ----------------------------------- TEST ----------------------------------- #
@test.describe('Tests')
def fixed_tests():
    def testing(h, bounce, window, exp):
        actual = bouncing_ball(h, bounce, window)
        test.assert_equals(actual, exp)
        
    @test.it('Fixed Tests')
    def tests():
        testing(2, 0.5, 1, 1)
        testing(3, 0.66, 1.5, 3)
        testing(30, 0.66, 1.5, 15)
        testing(30, 0.75, 1.5, 21)