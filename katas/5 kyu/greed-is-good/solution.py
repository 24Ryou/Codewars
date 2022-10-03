# greed-is-good
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def score(dice):
  dice = "".join(list(map(str ,sorted(dice))))
  rules = { '111': 1000 , '666': 600 , '555': 500 , '444': 400 , '333': 300 , '222': 200 }
  rules2 = {'1': 100 , '5': 50}
  arr = []
  for k,v in rules.items():
    if k in dice:
      arr.append(v)
      dice = dice.replace(k , "")
  arr2 = [v*dice.count(k) for k,v in rules2.items()]
  return sum(arr + arr2)
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def score(dice):
  return dice.count(1)//3 * 1000 + dice.count(1)%3 * 100 \
    + dice.count(2)//3 * 200 \
    + dice.count(3)//3 * 300 \
    + dice.count(4)//3 * 400 \
    + dice.count(5)//3 * 500 + dice.count(5)%3 * 50 \
    + dice.count(6)//3 * 600 \
# ----------------------------------- TEST ----------------------------------- #
test.describe("Example Tests")
test.it("Example Case")
test.assert_equals( score( [2, 3, 4, 6, 2] ), 0)
test.assert_equals( score(  [4, 4, 4, 3, 3] ), 400)
test.assert_equals( score(  [2, 4, 4, 5, 4] ), 450)
test.assert_equals( score(  [1, 5, 1, 3, 4] ), 250)
test.assert_equals( score(  [2, 5, 5, 2, 1] ), 200)
test.assert_equals( score(  [1, 1, 1, 1, 3] ), 1100)