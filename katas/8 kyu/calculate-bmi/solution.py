import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def bmi(weight, height):
    if weight/height**2 <= 18.5:
      return 'Underweight'
    if weight/height**2 <= 25.0:
      return 'Normal'
    if weight/height**2 <= 30.0:
      return 'Overweight'
    if weight/height**2 > 30:
      return 'Obese'
# ------------------------------ clever solution ----------------------------- #
def bmi(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]
# ----------------------------------- test ----------------------------------- #
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(bmi(50, 1.80), "Underweight")
        test.assert_equals(bmi(80, 1.80), "Normal")
        test.assert_equals(bmi(90, 1.80), "Overweight")
        test.assert_equals(bmi(110, 1.80), "Obese")
        test.assert_equals(bmi(50, 1.50), "Normal")