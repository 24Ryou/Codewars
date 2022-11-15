# data-reverse
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def data_reverse(data):
  bytes = [data[x:x+8] for x in range(len(data)) if x%8 == 0][::-1]
  return [i for x in bytes for i in x]
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def data_reverse(data):
  res = []
  
  for i in range(len(data)-8, -1, -8):
    res.extend(data[i:i+8])
  
  return res
# ----------------------------------- TEST ----------------------------------- #
data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
data2 = [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
test.assert_equals(data_reverse(data1),data2)

data3 = [0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1]
data4 = [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]
test.assert_equals(data_reverse(data3),data4)