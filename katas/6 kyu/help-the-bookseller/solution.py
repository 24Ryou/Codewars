# help-the-bookseller
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def stock_list(list_of_art, list_of_cat):
  res = []
  for c in list_of_cat:
    q = [int(x.split(" ")[-1]) for x in list_of_art if x[0] == c]
    res.append(f'({c} : {sum(q)})')
  return " - ".join(res) if list_of_art and list_of_cat else ""
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #
b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B", "C", "D"]
test.assert_equals(stock_list(b, c), "(A : 0) - (B : 1290) - (C : 515) - (D : 600)")

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
test.assert_equals(stock_list(b, c), "(A : 200) - (B : 1140)")