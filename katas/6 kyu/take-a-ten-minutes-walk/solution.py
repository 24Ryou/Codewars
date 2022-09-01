from pickle import TRUE
from typing_extensions import clear_overloads
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def is_valid_walk(walk):
  if len(walk) != 10 :
    return False;
  if walk.count('w') != walk.count('e'):
    return False;
  if walk.count('s') != walk.count('n'):
    return False
  return True
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
# ----------------------------------- TEST ----------------------------------- #
test.expect(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), 'should return True');
test.expect(not is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), 'should return False');
test.expect(not is_valid_walk(['w']), 'should return False');
test.expect(not is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), 'should return False');
test.expect(is_valid_walk(['s','e','w','n','n','e','e','w','w','s']), 'should return True');