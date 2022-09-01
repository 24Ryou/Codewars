import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def sort_array(source_array):
    odds = []
    answer = []
    for i in source_array:
        if i % 2 > 0:
            odds.append(i)
            answer.append("X")
        else:
            answer.append(i)
    odds.sort()
    for i in odds:
        x = answer.index("X")
        answer[x] = i
    return answer
# ------------------------------ clever solution ----------------------------- #
def sort_array(source_array):
    odd = sorted((x for x in source_array if x%2!=0), reverse=True)
    return [x if x%2 == 0 else odd.pop() for x in source_array]
# ----------------------------------- test ----------------------------------- #
test.assert_equals(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
test.assert_equals(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
test.assert_equals(sort_array([]),[])