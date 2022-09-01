import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def order(sentence):
  sentence = sentence.split()
  order = [int(y) for x in sentence for y in x if y.isdigit()]
  dic = dict(zip(order , sentence))
  return " ".join(dict(sorted(dic.items())).values())
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
# ----------------------------------- TEST ----------------------------------- #
@test.describe('Your order, please')
def desc1():
    @test.it('Sample tests')
    def it1():
        test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
        test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
        test.assert_equals(order(""), "")