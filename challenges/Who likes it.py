import codewars_test as test
# -------------------------------- my solution ------------------------------- #
def likes(names):
    i = len(names)
    s = ''
    if i > 0 :
        if i > 2:
            x = i - 2
            s = names[0] + ', ' + names[1] + ' and ' + str(x) + ' others like this'
        elif i > 1:
            s = names[0] + ' and ' + names[1] + ' like this'
        else:
            s = names[0] + ' likes this'
    else:
        s = 'no one likes this'
        
    return s
# ----------------------------- clever solution ----------------------------- #
def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)
# ----------------------------------- test ----------------------------------- #
@test.it('Basic tests')
def _():
    test.assert_equals(likes([]), 'no one likes this')
    test.assert_equals(likes(['Peter']), 'Peter likes this')
    test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
    test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
    test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')