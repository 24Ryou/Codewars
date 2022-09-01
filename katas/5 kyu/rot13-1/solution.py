import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def rot13(message):
  rot = ""
  for c in message:
    rot += rot_char(c)
  return rot

def rot_char(c):
  if c == "a": return "n"
  if c == "b": return "o"
  if c == "c": return "p"
  if c == "d": return "q"
  if c == "e": return "r"
  if c == "f": return "s"
  if c == "g": return "t"
  if c == "h": return "u"
  if c == "i": return "v"
  if c == "j": return "w"
  if c == "k": return "x"
  if c == "l": return "y"
  if c == "m": return "z"
  if c == "n": return "a"
  if c == "o": return "b"
  if c == "p": return "c"
  if c == "q": return "d"
  if c == "r": return "e"
  if c == "s": return "f"
  if c == "t": return "g"
  if c == "u": return "h"
  if c == "v": return "i"
  if c == "w": return "j"
  if c == "x": return "k"
  if c == "y": return "l"
  if c == "z": return "m"
  if c == "A": return "N"
  if c == "B": return "O"
  if c == "C": return "P"
  if c == "D": return "Q"
  if c == "E": return "R"
  if c == "F": return "S"
  if c == "G": return "T"
  if c == "H": return "U"
  if c == "I": return "V"
  if c == "J": return "W"
  if c == "K": return "X"
  if c == "L": return "Y"
  if c == "M": return "Z"
  if c == "N": return "A"
  if c == "O": return "B"
  if c == "P": return "C"
  if c == "Q": return "D"
  if c == "R": return "E"
  if c == "S": return "F"
  if c == "T": return "G"
  if c == "U": return "H"
  if c == "V": return "I"
  if c == "W": return "J"
  if c == "X": return "K"
  if c == "Y": return "L"
  if c == "Z": return "M"
  return c
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def rot13(message):
    rot13 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
    return message.translate(rot13)
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(rot13("test"),"grfg")
test.assert_equals(rot13("Test"),"Grfg")
