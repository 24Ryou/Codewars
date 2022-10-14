# strings-mix
from ast import pattern
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def mix(s1, s2):
  s = []
  lett = "abcdefghijklmnopqrstuvwxyz"
  
  for ch in lett:
    val1, val2 = s1.count(ch), s2.count(ch)
    if max(val1, val2) >= 2:
      if val1 > val2: s.append("1:"+val1*ch)
      elif val1 < val2: s.append("2:"+val2*ch)
      else: s.append("=:"+val1*ch)

  s.sort()
  s.sort(key=len, reverse=True)
  return "/".join(s)
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def mix(s1, s2):
  hist = {}
  for ch in "abcdefghijklmnopqrstuvwxyz":
    val1, val2 = s1.count(ch), s2.count(ch)
    if max(val1, val2) > 1:
      which = "1" if val1 > val2 else "2" if val2 > val1 else "="
      hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
  return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
test.assert_equals(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp"), '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
test.assert_equals(mix("looping is fun but dangerous", "less dangerous than coding"), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
test.assert_equals(mix(" In many languages", " there's a pair of functions"), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
test.assert_equals(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
test.assert_equals(mix("codewars", "codewars"), "")
test.assert_equals(mix("A generation must confront the looming ", "codewarrs"), "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")