# the-observed-pin
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
import itertools as iter
def get_pins(observed):
  couldbe = {
    "0": ["8" , "0"] , 
    "1": ["2" , "4" , "1"] , 
    "2": ["1" , "3" , "5" , "2"] , 
    "3": ["2" , "6" , "3"] , 
    "4": ["1" , "5" , "7" , "4"] , 
    "5": ["8" , "4" , "6" , "2" , "5"] , 
    "6": ["9" , "5" , "3" , "6"] , 
    "7": ["8" , "4" , "7"] , 
    "8": ["7" , "5" , "9" , "0" , "8"] , 
    "9": ["8" , "6" , "9"] , 
  }
  out = []
  for x in observed:
    if x in couldbe:
      out.append(couldbe[x])
  out = list(iter.product(*out))
  return ["".join(x) for x in out]
# ------------------------------ CLEVER SOLUTION ----------------------------- #
from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
  return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]
# ----------------------------------- TEST ----------------------------------- #
test.describe('example tests')
expectations = [('8', ['5','7','8','9','0']),
                ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
                ('369', ["339","366","399","658","636","258","268","669","668","266","369","398","256","296","259","368","638","396","238","356","659","639","666","359","336","299","338","696","269","358","656","698","699","298","236","239"])]

for tup in expectations:
  test.assert_equals(sorted(get_pins(tup[0])), sorted(tup[1]), 'PIN: ' + tup[0])