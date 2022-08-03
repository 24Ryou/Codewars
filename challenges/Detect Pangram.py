import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def is_pangram(s):
  letters = list('abcdefghijklmnopqrstuvwxyz')
  for x in s:
    if x.lower() in letters:
      letters.remove(x.lower())
  return True if len(letters) == 0 else False
# ------------------------------ clever solution ----------------------------- #
def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True
# ----------------------------------- test ----------------------------------- #
@test.describe("sample tests")
def sample_tests():
    
    @test.it("Should return true for a pangram")
    def test_pangram():        
        test.assert_equals(is_pangram("The quick, brown fox jumps over the lazy dog!"), True)

    @test.it("Should return false for not a pangram")
    def test_not_pangram():        
        test.assert_equals(is_pangram("1bcdefghijklmnopqrstuvwxyz"), False)