import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def find_uniq(arr):
  arr = sorted(arr)
  for x in range(0 , len(arr)):
    if arr[x] != arr[x+1]:
      if arr[x] != arr[x-1]:
        return arr[x]
      else: return arr[x+1]
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def find_uniq(arr):
  a, b = set(arr)
  return a if arr.count(a) == 1 else b
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Basic Tests")
def f():
    @test.it("Simple tests")
    def _():
        test.assert_equals(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
        test.assert_equals(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
        test.assert_equals(find_uniq([ 3, 10, 3, 3, 3 ]), 10)