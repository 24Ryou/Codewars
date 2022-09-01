import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def find_uniq(arr):
  for x in range(0,len(arr)):
    c = set(sorted(arr[x-1].lower()))
    a = set(sorted(arr[x].lower()))
    b = set(sorted(arr[x+1].lower()))
    if a != b:
      if a!=c:
        return arr[x]
      else:
        return arr[x+1]
# ------------------------------ clever solution ----------------------------- #
def find_uniq(arr):
    if set(arr[0].lower()) == set(arr[1].lower()):
        majority_set = set(arr[0].lower())
    elif set(arr[0].lower()) == set(arr[2].lower()):
        majority_set = set(arr[0].lower())
    else:
        majority_set = set(arr[1].lower())
    
    for string in arr:
        if set(string.lower()) != majority_set:
            return string
# ----------------------------------- test ----------------------------------- #
test.describe('should handle sample cases')
test.assert_equals(find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]), 'BbBb')
test.assert_equals(find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]), 'foo')
test.assert_equals(find_uniq([ '    ', 'a', '  ' ]), 'a')
