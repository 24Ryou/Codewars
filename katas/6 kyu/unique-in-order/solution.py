import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def unique_in_order(iterable):
  x = []
  if len(iterable) > 0:
    x.append(iterable[0])
    for i in range(len(iterable)-1):
      if iterable[i] != iterable[i+1]:
        x.append(iterable[i+1])
  return x
# ------------------------------ CLEVER SOLUTION ----------------------------- #
unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])