import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def tower_builder(n_floors, block_size):
  w, h = block_size
  result = []
  width = (w*2)*n_floors-w
  for x in range(1, 2 * n_floors, 2):
    for y in range(0 , h):
      stars = x * ('*'*w)
      line = stars.center(width)
      result.append(line)
  return result
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def tower_builder(n_floors, block_size):
  w , h = block_size
  return [str.center("*" * (i*2-1)*w, (n_floors*2-1)*w) for i in range(1, n_floors+1) for _ in range(h)]
# ----------------------------------- TEST ----------------------------------- #
test.describe("Tests")
test.it("Basic Tests")
test.assert_equals(tower_builder(1, (1, 1)), ['*', ])
test.assert_equals(tower_builder(3, (4, 2)), ['        ****        ', '        ****        ', '    ************    ', '    ************    ', '********************', '********************'])