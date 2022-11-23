# find-the-middle-element
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def gimme(input_array):
  for i,x in enumerate(input_array): 
    if x != max(input_array) and x != min(input_array): return i
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(gimme([2, 3, 1]), 0, 'Finds the index of middle element')
test.assert_equals(gimme([5, 10, 14]), 1, 'Finds the index of middle element')