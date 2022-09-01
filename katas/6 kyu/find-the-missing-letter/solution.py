import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def find_missing_letter(chars):
  for i in range(1,len(chars)):
    if ord(chars[i]) > ord(chars[i-1])+1:
      return chr(ord(chars[i])-1)

def find_missing_letter(chars):
  return [chr(ord(chars[i])-1) for i in range(1,len(chars)) if ord(chars[i])-1 != ord(chars[i-1])][0]
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def find_missing_letter(chars):
  n = 0
  while ord(chars[n]) == ord(chars[n+1]) - 1:
      n += 1
  return chr(1+ord(chars[n]))

def find_missing_letter(c):
  return next(chr(ord(c[i])+1) for i in range(len(c)-1) if ord(c[i])+1 != ord(c[i+1]))
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(find_missing_letter(['a','b','c','d','f']), 'e')
test.assert_equals(find_missing_letter(['O','Q','R','S']), 'P')