# sum-by-factors
import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
def sum_for_list(lst):
    PrimeLst = []
    FinalList = []
    for n in lst:
        PrimeLst = list(set(PrimeLst).union(set(prime_factors(n))))
    PrimeLst.sort()
    for n in PrimeLst:
        sum = 0
        listN = [n]
        for m in lst:
            if m%n ==0:
                sum = sum+m
        listN.append(sum)
        FinalList.append(listN)
    return FinalList

def prime_factors(n):
    i = 2
    n = abs(n)
    factors = []
    while i * i <= n:         
        if n % i:             
            i += 1        
        else:             
            n //= i             
            factors.append(i)     
    if n > 1:
        factors.append(n)
    return factors

# ------------------------------ CLEVER SOLUTION ----------------------------- #
# ----------------------------------- TEST ----------------------------------- #
a = [12, 15]
test.assert_equals(sum_for_list(a), [[2, 12], [3, 27], [5, 15]])
a = [15, 21, 24, 30, 45]
test.assert_equals(sum_for_list(a), [[2, 54], [3, 135], [5, 90], [7, 21]])