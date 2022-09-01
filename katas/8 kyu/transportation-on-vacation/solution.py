import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def rental_car_cost(d):
    return d*40 if d < 3 else d*40-20 if d < 7 else d*40-50
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def rental_car_cost(d):
  return d * 40 - (d > 2) * 20 - (d > 6) * 30
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(rental_car_cost(1),40)
        test.assert_equals(rental_car_cost(4),140)
        test.assert_equals(rental_car_cost(7),230)
        test.assert_equals(rental_car_cost(8),270)

# every day cost 40$
# days more than 6 cost 50$ off total
# days more than 2 cost 20$ off total