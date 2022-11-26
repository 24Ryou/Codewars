# grasshopper-terminal-game-combat-function-1
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def combat(health, damage):
  return 0 if health < damage else health - damage
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(combat(100, 5), 95)
test.assert_equals(combat(83, 16), 67)
test.assert_equals(combat(20, 30), 0)