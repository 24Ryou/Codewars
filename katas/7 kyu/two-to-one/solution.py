import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def longest(s1, s2):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = s1 + s2
    y = ""
    for x in alphabet:
      if x not in s:
        continue
      if x in s:
        y = y + x
    return y
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))
# ----------------------------------- TEST ----------------------------------- #
@test.describe("longest")
def tests():
    @test.it("basic tests")
    def basics():
        test.assert_equals(longest("aretheyhere", "yestheyarehere"), "aehrsty")
        test.assert_equals(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
        test.assert_equals(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")
