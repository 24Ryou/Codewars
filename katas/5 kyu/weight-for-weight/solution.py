# weight-for-weight
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def order_weight(strng):
  arr = strng.split()
  fn_sum = lambda x : sum(int(i) for i in x)
  arr = sorted(sorted(arr), key=fn_sum)
  return " ".join(arr)
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def order_weight(_str : str):
  return " ".join(sorted(sorted(_str.split()), key=lambda x : sum(int(i) for i in x)))
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Weight for weight")
def tests():
    @test.it("basic tests")
    def basics1():
        test.assert_equals(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
        test.assert_equals(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")
        test.assert_equals(order_weight(""), "")
        
