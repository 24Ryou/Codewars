import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def fake_bin(x):
  return ''.join(['1' if int(i) >= 5 else '0' for i in x])
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def fake_bin(s):
  return s.translate(s.maketrans('0123456789', '0000011111'))
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        tests = [
            # [expected, input]
            ["01011110001100111", "45385593107843568"],
            ["101000111101101", "509321967506747"],
            ["011011110000101010000011011", "366058562030849490134388085"],
            ["01111100", "15889923"],
            ["100111001111", "800857237867"],
        ]
        
        for exp, inp in tests:
            test.assert_equals(fake_bin(inp), exp)