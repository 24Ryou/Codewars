import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def reverse_words(text):
  list = text.split(" ")
  _list = []
  for x in list:
    if len(x) > 1: 
      _list.append(x[::-1])
    else:
      _list.append(x)
  return " ".join(_list)
# ------------------------------ clever solution ----------------------------- #
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))
# ----------------------------------- test ----------------------------------- #
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god')
        test.assert_equals(reverse_words('apple'), 'elppa')
        test.assert_equals(reverse_words('a b c d'), 'a b c d')
        test.assert_equals(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')