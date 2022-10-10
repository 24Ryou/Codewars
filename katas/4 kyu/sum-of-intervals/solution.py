# sum-of-intervals
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def sum_of_intervals(intervals):
  intervals = [[x,y] for x,y in intervals]
  return sum(y-x for x,y in merge(intervals))

def merge(intervals):

  intervals.sort(key=lambda x: x[0])

  merged = []
  for interval in intervals:
    if not merged or merged[-1][1] < interval[0]:
      merged.append(interval)
    else:
      merged[-1][1] = max(merged[-1][1], interval[1])

  return merged
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #
@test.describe("Fixed tests")
def fixed_tests():
  @test.it("Tests")
  def it_1():
    test.assert_equals(sum_of_intervals([(1, 5)]), 4)
    test.assert_equals(sum_of_intervals([(1, 5), (6, 10)]), 8)
    test.assert_equals(sum_of_intervals([(1, 5), (1, 5)]), 4)
    test.assert_equals(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
      
  @test.it("Large numbers")
  def it_2():
    test.assert_equals(sum_of_intervals([(-1_000_000_000, 1_000_000_000)]), 2_000_000_000)
    test.assert_equals(sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]), 100_000_030)