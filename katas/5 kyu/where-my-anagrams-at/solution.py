import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def anagrams(word, words):
    list = []
    for x in words:
        if sorted(x) == sorted(word):
            list.append(x)
    return list
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
test.assert_equals(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])