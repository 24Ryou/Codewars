# pete-the-baker
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def cakes(recipe, available):
  amount = []
  for key , item in recipe.items():
    if key in available:
      amount.append(int(available[key]/item))
    else: return 0
  return min(amount)
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def cakes(recipe, available):
  return int(min(available.get(k, 0)/recipe[k] for k in recipe))
# ----------------------------------- TEST ----------------------------------- #
@test.it('Testing Pete, the Baker')
def _():
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    test.assert_equals(cakes(recipe, available), 2, 'example #1')

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    test.assert_equals(cakes(recipe, available), 0, 'example #2')