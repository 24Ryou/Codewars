# buying-a-car
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def nbMonths(oldCarPrice, newCarPrice, savingMonth, percentLoss):

  saving = 0
  month = 0

  while (saving + oldCarPrice) < newCarPrice:
    month += 1
    saving += savingMonth

    if month % 2 == 0:
      percentLoss += 0.5
    
    oldCarPrice *= ((100 - percentLoss) / 100)
    newCarPrice *= ((100 - percentLoss) / 100)
  
  return [month , round(saving + oldCarPrice - newCarPrice)]
# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #
test.assert_equals(nbMonths(2000, 8000, 1000, 1.5), [6, 766])
test.assert_equals(nbMonths(12000, 8000, 1000, 1.5) ,[0, 4000])