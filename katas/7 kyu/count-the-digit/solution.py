import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def nb_dig(n, d):
  return ("".join(str(x**2) for x in range(0,n+1))).count(str(d))
# ------------------------------ clever solution ----------------------------- #
def nb_dig(n, d):
    return sum(str(i*i).count(str(d)) for i in range(n+1))
# ----------------------------------- test ----------------------------------- #
test.describe("nb_dig")
test.it("Basic tests") 	
test.assert_equals(nb_dig(5750, 0), 4700)
test.assert_equals(nb_dig(11011, 2), 9481)
test.assert_equals(nb_dig(12224, 8), 7733)
test.assert_equals(nb_dig(11549, 1), 11905)