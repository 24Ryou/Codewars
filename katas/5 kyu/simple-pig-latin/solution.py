# simple-pig-latin
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def pig_it(text):
  return " ".join(x[1:]+x[0]+'ay' if x not in ['!' , '?'] else x for x in text.split())
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def pig_it(text):
  lst = text.split()
  return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')