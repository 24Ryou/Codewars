import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def comp(a1, a2):
    return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)
# ------------------------------ clever solution ----------------------------- #
def comp(array1 , array2):   
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False
# ------------------------------------ test ----------------------------------- #
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
test.assert_equals(comp(a1, a2), True)
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
test.assert_equals(comp(a1, a2), False)
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
test.assert_equals(comp(a1, a2), False)