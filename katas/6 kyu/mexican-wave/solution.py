# mexican-wave
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def wave(people):
  new=[]
  for i, val in enumerate(people[:]):
    if val.isalpha():
      up=people[i].upper()
      c=people[:i] + up + people[i+1:]
      new.append(c)
  return new
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def wave(str):
  return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]
# ----------------------------------- TEST ----------------------------------- #
result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
test.assert_equals(wave("hello"), result)

result = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
test.assert_equals(wave("codewars"), result)

result = []
test.assert_equals(wave(""), result)

result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
test.assert_equals(wave("two words"),result)

result = [" Gap ", " gAp ", " gaP "]
test.assert_equals(wave(" gap "), result)

result = ["A       b    ", "a       B    "]
test.assert_equals(wave("a       b    "), result)

result = ["This is a few words", "tHis is a few words", "thIs is a few words", "thiS is a few words", "this Is a few words", "this iS a few words", "this is A few words", "this is a Few words", "this is a fEw words", "this is a feW words", "this is a few Words", "this is a few wOrds", "this is a few woRds", "this is a few worDs", "this is a few wordS"]
test.assert_equals(wave("this is a few words"), result)