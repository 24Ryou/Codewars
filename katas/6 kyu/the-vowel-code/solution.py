# the-vowel-code
import code
from multiprocessing.sharedctypes import Value
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
codes = {'a' : "1" ,'e' : "2" ,'i' : "3" ,'o' : "4" ,'u' : "5" }

def encode(st):
  return "".join([l if l not in codes else codes[l] for l in st]) 

def decode(st):
  new_dic = {value:key for (key , value) in codes.items()}
  return "".join([l if l not in new_dic else new_dic[l] for l in st])
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def encode(s, t=str.maketrans("aeiou", "12345")):
  return s.translate(t)
  
def decode(s, t=str.maketrans("12345", "aeiou")):
  return s.translate(t)
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(encode('hello'), 'h2ll4')
test.assert_equals(encode('How are you today?'), 'H4w 1r2 y45 t4d1y?')
test.assert_equals(encode('This is an encoding test.'), 'Th3s 3s 1n 2nc4d3ng t2st.')
test.assert_equals(decode('h2ll4'), 'hello')