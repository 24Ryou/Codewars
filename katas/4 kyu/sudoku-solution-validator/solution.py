# sudoku-solution-validator
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def valid_solution(board):

  for i in range(len(board)):
    hadd = 0
    vadd = 0
    for j in range(len(board)):
      #vertical check
      vadd += board[j][i]
      #horizontal check
      hadd += board[i][j]
      #numbers check
      if board[i][j] < 1 or board[i][j] > 9:
        print(1)
        return False
    if vadd != 45 or hadd != 45:
      print (2)
      print (vadd)
      print (hadd)
      return False
  for i in range(3):
    for j in range(3):
      gadd = 0
      for k in range(3):
        for l in range(3):
          gadd += board[i*3+k][j*3+l]
          if board[i][j] < 1 or board[i][j] > 9:
            print (3)
            return False
      if gadd != 45:
        return False
  return True 
# ------------------------------ CLEVER SOLUTION ----------------------------- #
correct = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def valid_solution(board):
  # check rows
  for row in board:
    if sorted(row) != correct:
      return False
  
  # check columns
  for column in zip(*board):
    if sorted(column) != correct:
      return False
  
  # check regions
  for i in range(3):
    for j in range(3):
      region = []
      for line in board[i*3:(i+1)*3]:
        region += line[j*3:(j+1)*3]
      
      if sorted(region) != correct:
        return False
  
  # if everything correct
  return True
# ----------------------------------- TEST ----------------------------------- #
@test.describe('Testing...')
def _():
    @test.it('Sample tests')
    def _():

        test.assert_equals(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                                 [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                 [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                 [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                 [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                 [3, 4, 5, 2, 8, 6, 1, 7, 9]]), True);

        test.assert_equals(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                                 [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                 [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                 [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                 [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                 [3, 0, 0, 4, 8, 1, 1, 7, 9]]), False);

        test.assert_equals(valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                                ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]), True);

        test.assert_equals(valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                                ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]), False);

        test.assert_equals(valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                                ,[4, 9, 8, 2, 6, 0, 3, 7, 5]
                                ,[7, 0, 6, 3, 8, 0, 2, 1, 9]
                                ,[6, 4, 3, 1, 5, 0, 7, 9, 2]
                                ,[5, 2, 1, 7, 9, 0, 8, 4, 6]
                                ,[9, 8, 0, 4, 2, 6, 5, 3, 1]
                                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                                ,[3, 6, 0, 8, 1, 7, 9, 2, 4]
                                ,[8, 7, 0, 6, 4, 2, 1, 3, 5]]), False); 

        test.assert_equals(valid_solution([[1, 2, 3, 4, 5, 6, 7, 8, 9]
                                 ,[2, 3, 4, 5, 6, 7, 8, 9, 1]
                                 ,[3, 4, 5, 6, 7, 8, 9, 1, 2]
                                 ,[4, 5, 6, 7, 8, 9, 1, 2, 3]
                                 ,[5, 6, 7, 8, 9, 1, 2, 3, 4]
                                 ,[6, 7, 8, 9, 1, 2, 3, 4, 5]
                                 ,[7, 8, 9, 1, 2, 3, 4, 5, 6]
                                 ,[8, 9, 1, 2, 3, 4, 5, 6, 7]
                                 ,[9, 1, 2, 3, 4, 5, 6, 7, 8]]), False);