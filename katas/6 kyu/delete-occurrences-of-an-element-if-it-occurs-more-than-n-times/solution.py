# delete-occurrences-of-an-element-if-it-occurs-more-than-n-times
from itertools import count
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def delete_nth(order,max_e):
  r = []
  o = {}
  for x in order :
    count = o.setdefault(x , 0)
    if count >= max_e:
      continue
    r.append(x)
    o[x] += 1
  return r
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(delete_nth([20,37,20,21], 1), [20,37,21])
test.assert_equals(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])