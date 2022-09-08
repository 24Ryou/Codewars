# directions-reduction
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def dirReduc(arr):
  d = {'WEST':'EAST' , 'EAST':'WEST' , 'NORTH':'SOUTH' , 'SOUTH':'NORTH'}
  r = []
  for i in arr:
    if r and d[i] == r[-1]:
      r.pop()
    else:
      r.append(i)
  return r
# ------------------------------ CLEVER SOLUTION ----------------------------- #
def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3
# ----------------------------------- TEST ----------------------------------- #
a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
test.assert_equals(dirReduc(a), ['WEST'])
u=["NORTH", "WEST", "SOUTH", "EAST"]
test.assert_equals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])