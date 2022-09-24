# which-are-in
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def in_array(array1, array2):
  r = []
  for x in array2:
    for y in array1:
      if y in x:
        r.append(y)
  return sorted(list(set(r)))
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def in_array(a1, a2):
  return sorted({sub for sub in a1 if any(sub in s for s in a2)})
# ----------------------------------- TEST ----------------------------------- #
@test.describe("in_array")
def tests():
    def testing(array1, array2, expect):
        actual = in_array(array1, array2)
        test.assert_equals(actual, expect)
    @test.it("Basic tests")
    def basics():
        a1 = ["live", "arp", "strong"] 
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ['arp', 'live', 'strong']
        testing(a1, a2, r)          
        a1 = ["arp", "mice", "bull"] 
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ['arp']
        testing(a1, a2, r)    