import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def nb_year(p0, percent, aug, p):
  years = 0
  while p0 <= p :
    years += 1
    p0 += int(p0 * percent/100) + aug
  return years
# ------------------------------ clever solution ----------------------------- #
def nb_year(p0, percent, aug, p, years = 0):
    if p0 < p:
        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years
# ----------------------------------- test ----------------------------------- #
@test.describe("nb_year")
def tests():
    @test.it("basic tests")
    def basics():
        test.assert_equals(nb_year(1500, 5, 100, 5000), 15)
        test.assert_equals(nb_year(1500000, 2.5, 10000, 2000000), 10)
        test.assert_equals(nb_year(1500000, 0.25, 1000, 2000000), 94)