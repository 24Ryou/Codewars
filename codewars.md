__Lists of challenges__
- [Abbreviate a Two Word Name](#abbreviate-a-two-word-name)
- [Are they the same](#are-they-the-same)
- [Basic Mathematical Operations](#basic-mathematical-operations)
- [Calculating with Functions](#calculating-with-functions)
- [Convert a Number to a String](#convert-a-number-to-a-string)
- [Convert a String to a Number](#convert-a-string-to-a-number)
- [Convert string to camel case](#convert-string-to-camel-case)
- [Counting sheep](#counting-sheep)
- [Disemvowel Trolls](#disemvowel-trolls)
- [Even or Odd](#even-or-odd)
- [Find the odd int](#find-the-odd-int)
- [Growth of a Population](#growth-of-a-population)
- [Highest and Lowest](#highest-and-lowest)
- [Not very secure](#not-very-secure)
- [Remove String Spaces](#remove-string-spaces)
- [PaginationHelper](#paginationhelper)
- [Playing with digits](#playing-with-digits)
- [Primes in numbers](#primes-in-numbers)
- [Regex Password Validation](#regex-password-validation)
- [RGB To Hex Conversion](#rgb-to-hex-conversion)
- [Rot13](#rot13)
- [Sort the odd](#sort-the-odd)
- [Square Every Digit](#square-every-digit)
- [String repeat](#string-repeat)
- [Sum of odd numbers](#sum-of-odd-numbers)
- [Take a Ten Minutes Walk](#take-a-ten-minutes-walk)
- [Tribonacci Sequence](#tribonacci-sequence)
- [Two to One](#two-to-one)
- [Unique In Order](#unique-in-order)
- [Valid Parentheses](#valid-parentheses)
- [Vowel Count](#vowel-count)
- [Where my anagrams at](#where-my-anagrams-at)
- [Who likes it](#who-likes-it)
- [Beginner Series 3 Sum of Numbers](#beginner-series-3-sum-of-numbers)
- [Build Tower](#build-tower)
- [Build Tower Advanced](#build-tower-advanced)
- [Convert a Boolean to a String](#convert-a-boolean-to-a-string)
- [Function 1 hello world](#function-1-hello-world)
- [Invert values](#invert-values)
- [Reverse words](#reverse-words)
- [Detect Pangram](#detect-pangram)
- [Opposites Attract](#opposites-attract)
- [Printer Errors](#printer-errors)
- [Find the unique number](#find-the-unique-number)
- [Find the unique string](#find-the-unique-string)
- [Isograms](#isograms)

# Abbreviate a Two Word Name
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

`Sam Harris` => `S.H`

`patrick feeney` => `P.F`

Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

`Sam Harris` => `S.H`

`patrick feeney` => `P.F`


```py
def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()

# Clever Solution
abbrev_name = lambda x: ".".join([x[0] , x.split(" ")[1][0]]).upper()
```
# Are they the same
Given two arrays `a` and `b` write a function `comp(a, b)` (or`compSame(a, b)`) that checks whether the two arrays have the "same" elements, with the same *multiplicities* (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in `b` are the elements in `a` squared, regardless of the order.

#### Examples
##### Valid arrays
Given two arrays `a` and `b` write a function `comp(a, b)` (or`compSame(a, b)`) that checks whether the two arrays have the "same" elements, with the same *multiplicities* (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in `b` are the elements in `a` squared, regardless of the order.

#### Examples
##### Valid arrays
```
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
```
`comp(a, b)` returns true because in `b` 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write `b`'s elements in terms of squares:
```
a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
```
##### Invalid arrays
If, for example, we change the first number to something else, `comp` is not returning true anymore:
```
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
```
`comp(a,b)` returns false because in `b` 132 is not the square of any number of `a`.
```
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
```
`comp(a,b)` returns false because in `b` 36100 is not the square of any number of `a`.

#### Remarks
- `a` or `b` might be `[] or {}` (all languages except R, Shell).
- `a` or `b` might be `nil` or `null` or `None` or `nothing` (except in C++, COBOL, Crystal, D, Dart, Elixir, Fortran, F#, Haskell, Nim, OCaml, Pascal, Perl, PowerShell, Prolog, PureScript, R, Racket, Rust, Shell, Swift). 

If `a` or `b` are `nil` (or `null` or `None`, depending on the language), the problem doesn't make sense so return false.

#### Note for C
The two arrays have the same size `(> 0)` given as parameter in function `comp`.

```py
def comp(a1, a2):
    return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)

# Clever Solution
def comp(array1 , array2):   
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False
```
# Basic Mathematical Operations
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).  
The function should return result of numbers after applying the chosen operation.

### Examples(Operator, value1, value2) --> output

~~~if-not:nasm
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).  
The function should return result of numbers after applying the chosen operation.

### Examples(Operator, value1, value2) --> output

~~~if-not:nasm
```
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7
```
~~~

~~~if:nasm
```nasm
mov dil, '+'
mov rax, __float64__(4.0)
mov rdx, __float64__(7.0)
movq xmm0, rax
movq xmm1, rdx
call basic_op        ; XMM0 <- 11.0

mov dil, '-'
mov rax, __float64__(15.0)
mov rdx, __float64__(18.0)
movq xmm0, rax
movq xmm1, rdx
call basic_op        ; XMM0 <- -3.0

mov dil, '*'
mov rax, __float64__(5.0)
movq xmm0, rax
movq xmm1, rax
call basic_op        ; XMM0 <- 25.0

mov dil, '/'
mov rax, __float64__(49.0)
mov rdx, __float64__(7.0)
movq xmm0, rax
movq xmm1, rdx
call basic_op        ; XMM0 <- 7.0
```
~~~
```py
def basic_op (operator, value1, value2):
  match operator:
    case '+':
      return value1 + value2
    case '-':
      return value1 - value2
    case '*':
      return value1 * value2
    case '/':
      return value1/value2

# Clever Solution
def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))

def basic_op(o, a, b):
    return {'+':a+b,'-':a-b,'*':a*b,'/':a/b}.get(o)
```
# Calculating with Functions
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

```py
def zero(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1]
    match operator:
      case '*':
        return int(0*number)
      case '+':
        return int(0+number)
      case '-':
        return int(0-number)
      case '/':
        return int(0/number)
  return 0
def one(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1] 
    match operator:
      case '*':
        return int(1*number)
      case '+':
        return int(1+number)
      case '-':
        return int(1-number)
      case '/':
        return int(1/number)
  return 1
def two(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1] 
    match operator:
      case '*':
        return int(2*number)
      case '+':
        return int(2+number)
      case '-':
        return int(2-number)
      case '/':
        return int(2/number)
  return 2
def three(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1]
    match operator:
      case '*':
        return int(3*number)
      case '+':
        return int(3+number)
      case '-':
        return int(3-number)
      case '/':
        return int(3/number) 
  return 3
def four(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1]
    match operator:
      case '*':
        return int(4*number)
      case '+':
        return int(4+number)
      case '-':
        return int(4-number)
      case '/':
        return int(4/number) 
  return 4
def five(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1] 
    match operator:
      case '*':
        return int(5*number)
      case '+':
        return int(5+number)
      case '-':
        return int(5-number)
      case '/':
        return int(5/number)
  return 5
def six(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1] 
    match operator:
      case '*':
        return int(6*number)
      case '+':
        return int(6+number)
      case '-':
        return int(6-number)
      case '/':
        return int(6/number)
  return 6
def seven(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1]
    match operator:
      case '*':
        return int(7*number)
      case '+':
        return int(7+number)
      case '-':
        return int(7-number)
      case '/':
        return int(7/number)
  return 7
def eight(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1] 
    match operator:
      case '*':
        return int(8*number)
      case '+':
        return int(8+number)
      case '-':
        return int(8-number)
      case '/':
        return int(8/number)
  return 8
def nine(r = ''):
  if r != '':
    number = int(r[0])
    operator = r[1]
    match operator:
      case '*':
        return int(9*number)
      case '+':
        return int(9+number)
      case '-':
        return int(9-number)
      case '/':
        return int(9/number) 
  return 9

def plus(number : int): 
  return str(number)+'+'
def minus(number : int): 
  return str(number)+'-'
def times(number : int): 
  return str(number)+'*'
def divided_by(number : int): 
  return str(number)+'/'

# Clever Solution
id_ = lambda x: x
number = lambda x: lambda f=id_: f(x)
zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))
plus = lambda x: lambda y: y + x
minus = lambda x: lambda y: y - x
times = lambda x: lambda y: y * x
divided_by = lambda x: lambda y: y / x
```
# Convert a Number to a String
We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?

We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?

```if:c
In C, return a dynamically allocated string that will be freed by the test suite.
```

#### Examples (input --> output):

```
123  --> "123"
999  --> "999"
-100 --> "-100"
```

```py
number_to_string = lambda x : str(x)

# Clever Solution
number_to_string = str
```
# Convert a String to a Number
Note: This kata is inspired by [Convert a Number to a String!](http://www.codewars.com/kata/convert-a-number-to-a-string/). Try that one too.

## Description

We need a function that can transform a string into a number. What ways of achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

## Examples
Note: This kata is inspired by [Convert a Number to a String!](http://www.codewars.com/kata/convert-a-number-to-a-string/). Try that one too.

## Description

We need a function that can transform a string into a number. What ways of achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

## Examples
```
"1234" --> 1234
"605"  --> 605
"1405" --> 1405
"-7" --> -7
```


```py
string_to_number = lambda n: int(n)

# Clever Solution
string_to_number = int
```
# Convert string to camel case
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized **only** if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). 

### Examples

`"the-stealth-warrior"` gets converted to `"theStealthWarrior"`  
`"The_Stealth_Warrior"` gets converted to `"TheStealthWarrior"`
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized **only** if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). 

### Examples

`"the-stealth-warrior"` gets converted to `"theStealthWarrior"`  
`"The_Stealth_Warrior"` gets converted to `"TheStealthWarrior"`

```py
def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

# Clever Solution
def to_camel_case(text):
    output = ''.join(x for x in text.title() if x not in "_-")
    return text[0] + output[1:] if text else ''
```
# Counting sheep
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

```py
def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)

# Clever Solution
count_sheeps = lambda x : x.count(True)
```
# Disemvowel Trolls
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata `y` isn't considered a vowel.
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata `y` isn't considered a vowel.

```py
disemvowel = lambda x :  re.sub("[aeiouAEIOU]","",x)

# Clever Solution
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")
```
# Even or Odd
```if-not:sql,shell
Create a function that takes an integer as an argument and returns `"Even"` for even numbers or `"Odd"` for odd numbers.
```
```if:sql
## SQL Notes:
You will be given a table, `numbers`, with one column `number`.</br>

Return a table with a column `is_even` containing `"Even"` or `"Odd"` depending on `number` column values.

### numbers table schema
* number INT

### output table schema
* is_even STRING
```
```if:shell
Write a script that takes an integer as an argument and returns `"Even"` for even numbers or `"Odd"` for odd numbers.
```
```py
def even_or_odd(number): return 'Even' if number%2 == 0 else 'Odd'

# Clever Solution
def even_or_odd(number):
  return ["Even", "Odd"][number % 2]

even_or_odd=lambda n:'EOvdedn'[n%2::2]
```
# Find the odd int
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.


### Examples

`[7]` should return `7`, because it occurs 1 time (which is odd).  
`[0]` should return `0`, because it occurs 1 time (which is odd).  
`[1,1,2]` should return `2`, because it occurs 1 time (which is odd).  
`[0,1,0,1,0]` should return `0`, because it occurs 3 times (which is odd).  
`[1,2,2,3,3,3,4,3,3,3,2,2,1]` should return `4`, because it appears 1 time (which is odd).
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

### Examples

`[7]` should return `7`, because it occurs 1 time (which is odd).  
`[0]` should return `0`, because it occurs 1 time (which is odd).  
`[1,1,2]` should return `2`, because it occurs 1 time (which is odd).  
`[0,1,0,1,0]` should return `0`, because it occurs 3 times (which is odd).  
`[1,2,2,3,3,3,4,3,3,3,2,2,1]` should return `4`, because it appears 1 time (which is odd).

```py
def find_it(seq):
  array = seq
  for x in seq:
    count = 0
    for i in seq:
        if i == x :
          count += 1
    if count%2 != 0 :
      return x

# Clever Solution
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
```
# Growth of a Population
In a small town the population is `p0 = 1000` at the beginning of a year. The population
regularly increases by `2 percent` per year and moreover `50` new inhabitants per year come to live in the town. 
How many years does the town need to see its population
greater or equal to `p = 1200` inhabitants?

In a small town the population is `p0 = 1000` at the beginning of a year. The population
regularly increases by `2 percent` per year and moreover `50` new inhabitants per year come to live in the town. 
How many years does the town need to see its population
greater or equal to `p = 1200` inhabitants?

```
At the end of the first year there will be: 
1000 + 1000 * 0.02 + 50 => 1070 inhabitants

At the end of the 2nd year there will be: 
1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

At the end of the 3rd year there will be:
1141 + 1141 * 0.02 + 50 => 1213

It will need 3 entire years.
```
More generally given parameters:

`p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)`

the function `nb_year` should return `n` number of entire years needed to get a population greater or equal to `p`.

aug is an integer, percent a positive or null floating number, p0 and p are positive integers (> 0)

```
Examples:
nb_year(1500, 5, 100, 5000) -> 15
nb_year(1500000, 2.5, 10000, 2000000) -> 10
```

#### Note: 
Don't forget to convert the percent parameter as a percentage in the body of your function: if the parameter percent is 2 you have to convert it to 0.02.


```py
def nb_year(p0, percent, aug, p):
  years = 0
  while p0 <= p :
    years += 1
    p0 += int(p0 * percent/100) + aug
  return years

# Clever Solution
def nb_year(p0, percent, aug, p, years = 0):
    if p0 < p:
        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years
```
# Highest and Lowest
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

### Examples

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

```py
def high_and_low(numbers):
  num = [int(x) for x in numbers.split()]
  return f'{max(num)} {min(num)}'

# Clever Solution
def high_and_low(numbers):
  return " ".join(x(numbers.split(), key=int) for x in (max, min))
```
# Not very secure
In this example you have to validate if a user input string is alphanumeric. The given string is not `nil/null/NULL/None`, so you don't have to check that.

The string has the following conditions to be alphanumeric:

* At least one character (`""` is not valid)
* Allowed characters are uppercase / lowercase latin letters and digits from `0` to `9`
* No whitespaces / underscore
In this example you have to validate if a user input string is alphanumeric. The given string is not `nil/null/NULL/None`, so you don't have to check that.

The string has the following conditions to be alphanumeric:

* At least one character (`""` is not valid)
* Allowed characters are uppercase / lowercase latin letters and digits from `0` to `9`
* No whitespaces / underscore

```py
def alphanumeric(password):
    regex = '^(?=[^\s_])[a-zA-Z0-9]+$'
    pattern = re.compile(regex)
    return bool(pattern.match(password))

# Clever Solution
def alphanumeric(string):
    return string.isalnum()
```
# Remove String Spaces
Simple, remove the spaces from the string, then return the resultant string.

~~~if:bf
The input string will be terminated with a null character `\0`.
~~~
~~~if:c,nasm
For C and Nasm, you must return a new dynamically allocated string.
~~~
Simple, remove the spaces from the string, then return the resultant string.

~~~if:bf
The input string will be terminated with a null character `\0`.
~~~
~~~if:c,nasm
For C and Nasm, you must return a new dynamically allocated string.
~~~

```py
def no_space(x):
    return "".join(x.split())

# Clever Solution
no_space = lambda x : x.replace(' ', '')
```
# PaginationHelper
For this exercise you will be strengthening your page-fu mastery.  You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array. 

The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. The types of values contained within the collection/array are not relevant. 

The following are some examples of how this class is used:

helper = PaginationHelper(['a','b','c','d','e','f'], 4)
helper.page_count() # should == 2
helper.item_count() # should == 6
helper.page_item_count(0)  # should == 4
helper.page_item_count(1) # last page - should == 2
helper.page_item_count(2) # should == -1 since the page is invalid

## page_index takes an item index and returns the page that it belongs on
helper.page_index(5) # should == 1 (zero based index)
helper.page_index(2) # should == 0
helper.page_index(20) # should == -1
helper.page_index(-10) # should == -1 because negative indexes are invalid

```py
class PaginationHelper:

  def __init__(self, collection : list, items_per_page):
    self.collection = collection
    self.item_per_page = items_per_page

  def item_count(self):
    return len(self.collection)

  def page_count(self):
    return int(len(self.collection)/self.item_per_page)+1

  def page_item_count(self, page_index):
    pages = range(0,int(len(self.collection)/self.item_per_page)+1)
    if page_index in pages:
      data = []
      for i in range(0 , len(self.collection) , self.item_per_page) :
        data.append(self.collection[i : i+self.item_per_page])
      return len(data[page_index])
    else :
      return -1

  def page_index(self, item_index):
    if item_index >= len(self.collection) or item_index < 0 or len(self.collection) <1:
      return -1
    elif item_index == 0:
        return 0
    else:
      return int(self.collection.index(item_index)/self.item_per_page)

# Clever Solution
class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self._item_count = len(collection)
        self.items_per_page = items_per_page

    def item_count(self):
        return self._item_count

    def page_count(self):
        return -(self._item_count // -self.items_per_page)

    def page_item_count(self, page_index):
        return min(self.items_per_page, self._item_count - page_index * self.items_per_page) \
            if 0 <= page_index < self.page_count() else -1

    def page_index(self, item_index):
        return item_index // self.items_per_page \
            if 0 <= item_index < self._item_count else -1
```
# Playing with digits
Some numbers have funny properties. For example:

> 89 --> 8¹ + 9² = 89 * 1

> 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

> 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p 
- we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n. 

In other words:


> Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.

**Note**: n and p will always be given as strictly positive integers.

dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

```py
def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
    s += pow(int(c),p+i)
  return s/n if s%n==0 else -1

# Clever Solution
dig_pow = lambda n,p : -1 if int(sum([int(x)**(p+i) for i , x in enumerate(str(n))])%n) != 0 else sum([int(x)**(p+i) for i , x in enumerate(str(n))])/n
```
# Primes in numbers
Given a positive number n > 1 find the prime factor decomposition of n.
The result will be a string with the following form :
Given a positive number n > 1 find the prime factor decomposition of n.
The result will be a string with the following form :
```
 "(p1**n1)(p2**n2)...(pk**nk)"
```
with the p(i) in increasing order and n(i) empty if
n(i) is 1.
```
Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
```


```py
def prime_factors(n):
  i = 2
  res = {}
  while n/i != 1:
    if n%i == 0:
      if i in res:
        res[i] = res[i]+1
      else:
        res[i] = 1
      n = n/i
    else:
      i+=1
  if i in res:
    res[i] = res[i]+1
  else:
    res[i] = 1
  t = ''
  res = sorted(res.items(),key = lambda a:a[0])
  for key in res:
    if key[1] == 1:
      t = t + '('+str(key[0]) +')'
    else:
      t = t + '(' +str(key[0]) + '**' + str(key[1]) + ')'
  return t

# Clever Solution
def prime_factors(n):
  i, j, p = 2, 0, []
  while n > 1:
    while n % i == 0: n, j = n / i, j + 1
    if j > 0: p.append([i,j])
    i, j = i + 1, 0
  return ''.join('(%d' %q[0] + ('**%d' %q[1]) * (q[1] > 1) + ')' for q in p)
```
# Regex Password Validation
You need to write regex that will validate a password to make sure it meets the following criteria:

* At least six characters long
* contains a lowercase letter
* contains an uppercase letter
* contains a digit
* only contains alphanumeric characters (note that `'_'` is not alphanumeric)You need to write regex that will validate a password to make sure it meets the following criteria:

* At least six characters long
* contains a lowercase letter
* contains an uppercase letter
* contains a digit
* only contains alphanumeric characters (note that `'_'` is not alphanumeric)
```py
regex = compile("""^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])[A-Za-z\d]{6,}$""", VERBOSE)

# Clever Solution
regex = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])[A-Za-z0-9]{6,}$'
```
# RGB To Hex Conversion
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of  expected output values:
rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

```py
def rgb(r, g, b):
  r = check(r)
  b = check(b)
  g = check(g)
  return ('%02X%02X%02X' % (r, g, b))

def check(int):
  if int >= 255:
    return 255
  if int <= 0:
    return 0
  else :
    return int

# Clever Solution
def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
```
# Rot13
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

```if:python
Please note that using `encode` is considered cheating.
```

```if:r
**Note:** As R is a natively vectorized language, you should write `rot13()` such that the argument `x` may be a character vector of any length. The return value should always be a character vector of the same length as `x`.
```

```py
def rot13(message):
  rot = ""
  for c in message:
    rot += rot_char(c)
  return rot

def rot_char(c):
  if c == "a": return "n"
  if c == "b": return "o"
  if c == "c": return "p"
  if c == "d": return "q"
  if c == "e": return "r"
  if c == "f": return "s"
  if c == "g": return "t"
  if c == "h": return "u"
  if c == "i": return "v"
  if c == "j": return "w"
  if c == "k": return "x"
  if c == "l": return "y"
  if c == "m": return "z"
  if c == "n": return "a"
  if c == "o": return "b"
  if c == "p": return "c"
  if c == "q": return "d"
  if c == "r": return "e"
  if c == "s": return "f"
  if c == "t": return "g"
  if c == "u": return "h"
  if c == "v": return "i"
  if c == "w": return "j"
  if c == "x": return "k"
  if c == "y": return "l"
  if c == "z": return "m"
  if c == "A": return "N"
  if c == "B": return "O"
  if c == "C": return "P"
  if c == "D": return "Q"
  if c == "E": return "R"
  if c == "F": return "S"
  if c == "G": return "T"
  if c == "H": return "U"
  if c == "I": return "V"
  if c == "J": return "W"
  if c == "K": return "X"
  if c == "L": return "Y"
  if c == "M": return "Z"
  if c == "N": return "A"
  if c == "O": return "B"
  if c == "P": return "C"
  if c == "Q": return "D"
  if c == "R": return "E"
  if c == "S": return "F"
  if c == "T": return "G"
  if c == "U": return "H"
  if c == "V": return "I"
  if c == "W": return "J"
  if c == "X": return "K"
  if c == "Y": return "L"
  if c == "Z": return "M"
  return c

# Clever Solution
def rot13(message):
    rot13 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
    return message.translate(rot13)
```
# Sort the odd
## Task

You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

### Examples

## Task

You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

### Examples

```
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
```

~~~if:lambdacalc
### Encodings

purity: `LetRec`  
numEncoding: `BinaryScott`  
export constructors `nil, cons` and deconstructor `foldl` for your `List` encoding  
~~~
```py
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

# Clever Solution
def sort_array(source_array):
    odd = sorted((x for x in source_array if x%2!=0), reverse=True)
    return [x if x%2 == 0 else odd.pop() for x in source_array]
```
# Square Every Digit
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 9<sup>2</sup> is 81 and 1<sup>2</sup> is 1.

**Note:** The function accepts an integer and returns an integer
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 9<sup>2</sup> is 81 and 1<sup>2</sup> is 1.

**Note:** The function accepts an integer and returns an integer

```py
def square_digits(num) : return int(''.join(str(int(i)**2) for i in str(num)))

# Clever Solution
square_digits = lambda num: int(''.join(str(int(d)**2) for d in str(num)))
```
# String repeat
~~~if:bf
Write a program which accepts a single byte `n` and then a sequence of bytes `string` and outputs the `string` exactly `n` times.

The first input byte will be `n`. Following bytes will be characters of `string`. The end of the input `string` will be indicated with a null byte `\0`.

### Examples:

"\6I" -> "IIIIII"
"\5Hello" -> "HelloHelloHelloHelloHello"
~~~

Write a function that accepts an integer `n` and a string `s` as parameters, and returns a string of `s` repeated exactly `n` times.

### Examples (input -> output)

~~~if:bf
Write a program which accepts a single byte `n` and then a sequence of bytes `string` and outputs the `string` exactly `n` times.

The first input byte will be `n`. Following bytes will be characters of `string`. The end of the input `string` will be indicated with a null byte `\0`.

### Examples:

"\6I" -> "IIIIII"
"\5Hello" -> "HelloHelloHelloHelloHello"
~~~

Write a function that accepts an integer `n` and a string `s` as parameters, and returns a string of `s` repeated exactly `n` times.

### Examples (input -> output)

```
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
```

```py
def repeat_str(repeat, string):
    return repeat * string

# Clever Solution
repeat_str = lambda a,b : a*b

from operator import mul as repeat_str
```
# Sum of odd numbers
Given the triangle of consecutive odd numbers:

Given the triangle of consecutive odd numbers:

```
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
```

Calculate the sum of the numbers in the n<sup>th</sup> row of this triangle (starting at index 1) e.g.: (**Input --> Output**)

```
1 -->  1
2 --> 3 + 5 = 8
```


```py
def row_sum_odd_numbers(n):
    return n*n*n

# Clever Solution
def row_sum_odd_numbers(n):
    return n ** 3
```
# Take a Ten Minutes Walk
You live in the city of Cartesia where all roads are laid out in a perfect grid.  You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.  The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).  You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return **true** if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point.  Return **false** otherwise.

> **Note**: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only).  It will never give you an empty array (that's not a walk, that's standing still!).
You live in the city of Cartesia where all roads are laid out in a perfect grid.  You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk.  The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']).  You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return **true** if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point.  Return **false** otherwise.

> **Note**: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only).  It will never give you an empty array (that's not a walk, that's standing still!).

```py
def is_valid_walk(walk):
  if len(walk) != 10 :
    return False;
  if walk.count('w') != walk.count('e'):
    return False;
  if walk.count('s') != walk.count('n'):
    return False
  return True

# Clever Solution
def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
```
# Tribonacci Sequence
Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

So, if we are to start our Tribonacci sequence with `[1, 1, 1]` as a starting input (AKA *signature*), we have this sequence:

Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

So, if we are to start our Tribonacci sequence with `[1, 1, 1]` as a starting input (AKA *signature*), we have this sequence:

```
[1, 1 ,1, 3, 5, 9, 17, 31, ...]
```

But what if we started with `[0, 0, 1]` as a signature? As starting with `[0, 1]` instead of `[1, 1]` basically *shifts* the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

```
[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
```

Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a **signature** array/list, returns **the first n elements - signature included** of the so seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative number; if `n == 0`, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)

If you enjoyed this kata more advanced and generalized version of it can be found in the <a href="http://www.codewars.com/kata/fibonacci-tribonacci-and-friends"  target="_blank" title="Xbonacci sequence">Xbonacci kata</a>

*[Personal thanks to Professor <a href="https://www.coursera.org/instructor/jimfowler" target="_blank" title="Jim Fowler">Jim Fowler</a> on Coursera for his awesome classes that I really recommend to any math enthusiast and for showing me this mathematical curiosity too with his usual contagious passion :)]*
```py
def tribonacci(signature, n):
    if n < 3:
        return signature[:n]
    if n == 0:
        return []
    if n <= 3:
        return signature
    else:
        l = len(signature)
        signature.append(sum(signature[l-3:l]))
        return tribonacci(signature,n-1)

# Clever Solution
def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3): res.append(sum(res[-3:]))
    return res
```
# Two to One
Take 2 strings `s1` and `s2` including only letters from `a` to `z`.
Return a new **sorted** string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

#### Examples:
Take 2 strings `s1` and `s2` including only letters from `a` to `z`.
Return a new **sorted** string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

#### Examples:
```
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
```

```py
def longest(s1, s2):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  s = s1 + s2
  y = ""
  for x in alphabet:
    if x not in s:
      continue
    if x in s:
      y = y + x
  return y

# Clever Solution
def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))
```
# Unique In Order
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]

```py
def unique_in_order(iterable):
  x = []
  if len(iterable) > 0:
    x.append(iterable[0])
    for i in range(len(iterable)-1):
      if iterable[i] != iterable[i+1]:
        x.append(iterable[i+1])
  return x

# Clever Solution
unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]
```
# Valid Parentheses
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return `true` if the string is valid, and `false` if it's invalid.

## Examples

Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return `true` if the string is valid, and `false` if it's invalid.

## Examples

```
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
```

## Constraints

`0 <= input.length <= 100`

~~~if-not:javascript,go,cobol
Along with opening (`(`) and closing (`)`) parenthesis, input may contain any valid ASCII characters.  Furthermore, the input string may be empty and/or not contain any parentheses at all.  Do **not** treat other forms of brackets as parentheses (e.g. `[]`, `{}`, `<>`).
~~~

```py
def valid_parentheses(string):
  count = 0
  for x in string:
    if x == '(' :
      count += 1
    elif x == ')':
      count -= 1
    
    if count < 0 :
      return False
  if count != 0 :
    return False
  return True

# Clever Solution
def valid_parentheses(string):
  cnt = 0
  for char in string:
      if char == '(': cnt += 1
      if char == ')': cnt -= 1
      if cnt < 0: return False
  return True if cnt == 0 else False
```
# Vowel Count
Return the number (count) of vowels in the given string. 

We will consider `a`, `e`, `i`, `o`, `u` as vowels for this Kata (but not `y`).

The input string will only consist of lower case letters and/or spaces.
Return the number (count) of vowels in the given string. 

We will consider `a`, `e`, `i`, `o`, `u` as vowels for this Kata (but not `y`).

The input string will only consist of lower case letters and/or spaces.

```py
def get_count(sentence):
  return len([x for x in sentence if x.lower() in 'aeuio'])

# Clever Solution
def getCount(inputStr):
  return sum(1 for let in inputStr if let in "aeiouAEIOU")
```
# Where my anagrams at
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

```
'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
```

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

```javascript
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
```

**Note for Go**\
For Go: Empty string slice is expected when there are no anagrams found.


```py
def anagrams(word, words):
  list = []
  for x in words:
      if sorted(x) == sorted(word):
          list.append(x)
  return list

# Clever Solution
def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]
```
# Who likes it
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

```
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
```

```if:c
* return must be an allocated string
* do not mutate input
```

Note: For 4 or more names, the number in `"and 2 others"` simply increases.

```py
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

# Clever Solution
def likes(names):
  n = len(names)
  return {
      0: 'no one likes this',
      1: '{} likes this', 
      2: '{} and {} like this', 
      3: '{}, {} and {} like this', 
      4: '{}, {} and {others} others like this'
  }[min(4, n)].format(*names[:3], others=n-2)
```
# Beginner Series 3 Sum of Numbers
Given two integers `a` and `b`, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return `a` or `b`.

**Note:** `a` and `b` are not ordered!

## Examples (a, b) --> output (explanation)

Given two integers `a` and `b`, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return `a` or `b`.

**Note:** `a` and `b` are not ordered!

## Examples (a, b) --> output (explanation)

```
(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
```
```py
def get_sum(a,b):
  return sum(range(min(a,b),max(a,b)+1))

# Clever Solution
def get_sum(a, b):
  return (a + b) * (abs(a - b) + 1) // 2
```
# Build Tower
Build Tower
---

Build a pyramid-shaped tower given a positive integer `number of floors`. A tower block is represented with `"*"` character.

For example, a tower with `3` floors looks like this:

Build Tower
---

Build a pyramid-shaped tower given a positive integer `number of floors`. A tower block is represented with `"*"` character.

For example, a tower with `3` floors looks like this:

```
[
  "  *  ",
  " *** ", 
  "*****"
]
```

And a tower with `6` floors looks like this:

```
[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
```

___

Go challenge [Build Tower Advanced](https://www.codewars.com/kata/57675f3dedc6f728ee000256) once you have finished this :)

```py
def tower_builder(n_floor):
  result = []
  width = (n_floor * 2) - 1
  for x in range(1, 2 * n_floor, 2):
      stars = x * '*'
      line = stars.center(width)
      result.append(line)
  return result

# Clever Solution
def tower_builder(n):
  return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
```
# Build Tower Advanced
Build Tower Advanced
---

Build Tower by the following given arguments:<br>
__number of floors__ (integer and always greater than 0)<br>
__block size__ (width, height) (integer pair and always greater than (0, 0))

Tower block unit is represented as `*`

* Python: return a `list`;
* JavaScript: returns an `Array`;

Have fun!
***

for example, a tower of 3 floors with block size = (2, 3) looks like below
Build Tower Advanced
---

Build Tower by the following given arguments:<br>
__number of floors__ (integer and always greater than 0)<br>
__block size__ (width, height) (integer pair and always greater than (0, 0))

Tower block unit is represented as `*`

* Python: return a `list`;
* JavaScript: returns an `Array`;

Have fun!
***

for example, a tower of 3 floors with block size = (2, 3) looks like below
```
[
  '    **    ',
  '    **    ',
  '    **    ',
  '  ******  ',
  '  ******  ',
  '  ******  ',
  '**********',
  '**********',
  '**********'
]
```
and a tower of 6 floors with block size = (2, 1) looks like below
```
[
  '          **          ', 
  '        ******        ', 
  '      **********      ', 
  '    **************    ', 
  '  ******************  ', 
  '**********************'
]
```
***
Go take a look at [Build Tower](https://www.codewars.com/kata/576757b1df89ecf5bd00073b) which is a more basic version :)
```py
def tower_builder(n_floors, block_size):
  w, h = block_size
  result = []
  width = (w*2)*n_floors-w
  for x in range(1, 2 * n_floors, 2):
    for y in range(0 , h):
      stars = x * ('*'*w)
      line = stars.center(width)
      result.append(line)
  return result

# Clever Solution
def tower_builder(n_floors, block_size):
  w , h = block_size
  return [str.center("*" * (i*2-1)*w, (n_floors*2-1)*w) for i in range(1, n_floors+1) for _ in range(h)]
```
# Convert a Boolean to a String
Implement a function which convert the given boolean value into its string representation.

Note: Only valid inputs will be given.
Implement a function which convert the given boolean value into its string representation.

Note: Only valid inputs will be given.

```py
boolean_to_string = str

# Clever Solution
def boolean_to_string(b):
    return str(b)
```
# Function 1 hello world
### Description:

Make a simple function called **greet** that returns the most-famous "hello world!".

### Style Points

Sure, this is about as easy as it gets. But how clever can you be to create the most creative hello world you can think of? What is a "hello world" solution you would want to show your friends?
### Description:

Make a simple function called **greet** that returns the most-famous "hello world!".

### Style Points

Sure, this is about as easy as it gets. But how clever can you be to create the most creative hello world you can think of? What is a "hello world" solution you would want to show your friends?

```py
def greet(): return 'hello world!'
```
# Invert values
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.


```
invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
```

```py
def invert(lst):
  _list = []
  for x in lst :
    if x > 0:
      _list.append(-x)
    else:
      _list.append(abs(x))
  return _list

# Clever Solution
def invert(lst):
    return [-x for x in lst]
```
# Reverse words
Complete the function that accepts a string parameter, and reverses each word in the string. **All** spaces in the string should be retained.

## Examples
Complete the function that accepts a string parameter, and reverses each word in the string. **All** spaces in the string should be retained.

## Examples
```
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
```
```py
def reverse_words(text):
  list = text.split(" ")
  _list = []
  for x in list:
    if len(x) > 1: 
      _list.append(x[::-1])
    else:
      _list.append(x)
  return " ".join(_list)

# Clever Solution
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))
```
# Detect Pangram
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant). 

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant). 

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.



```py
def is_pangram(s):`
  for x in s:
    if x.lower() in letters:
      letters.remove(x.lower())
  return True if len(letters) == 0 else False

# Clever Solution
def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True
```
# Opposites Attract
Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love. 

Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love. 

Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.
```py
def lovefunc( flower1, flower2 ):
    return True if flower1%2==0 and flower2%2 != 0 or flower2%2 == 0 and flower1%2 != 0 else False

# Clever Solution
def lovefunc( flower1, flower2 ):
  return (flower1+flower2)%2

def lovefunc(flower1, flower2):
    return flower1 % 2 != flower2 % 2
```
# Printer Errors
In a factory a printer prints labels for boxes. For one kind of boxes
the printer has to use colors which, for the sake of simplicity,
are named with letters from `a to m`. 

The colors used by the printer are
recorded in a control string. For example a "good" control string would be
`aaabbbbhaijjjm` meaning that the printer used three times color a, four times
color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" 
control string is produced e.g. `aaaxbbbbyyhwawiwjjjwwm` with letters not from `a to m`.

You have to write a function `printer_error` which given a string will return
the error rate of the printer as a **string** representing a rational whose numerator 
is the number of errors and the denominator the length of the control string.
Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters 
from `a`to `z`.

#### Examples:

In a factory a printer prints labels for boxes. For one kind of boxes
the printer has to use colors which, for the sake of simplicity,
are named with letters from `a to m`. 

The colors used by the printer are
recorded in a control string. For example a "good" control string would be
`aaabbbbhaijjjm` meaning that the printer used three times color a, four times
color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" 
control string is produced e.g. `aaaxbbbbyyhwawiwjjjwwm` with letters not from `a to m`.

You have to write a function `printer_error` which given a string will return
the error rate of the printer as a **string** representing a rational whose numerator 
is the number of errors and the denominator the length of the control string.
Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters 
from `a`to `z`.

#### Examples:

```
s="aaabbbbhaijjjm"
printer_error(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
printer_error(s) => "8/22"

```
```py
def printer_error(s):
  count = 0
  for x in s.upper():
    if ord(x) not in range(65,78):
      count += 1 
  return f'{count}/{len(s)}'

# Clever Solution
from re import sub
def printer_error(s):
  return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

def printer_error(s):
  return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))
```
# Find the unique number
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

```py
def find_uniq(arr):
  arr = sorted(arr)
  for x in range(0 , len(arr)):
    if arr[x] != arr[x+1]:
      if arr[x] != arr[x-1]:
        return arr[x]
      else: return arr[x+1]

# Clever Solution
def find_uniq(arr):
  a, b = set(arr)
  return a if arr.count(a) == 1 else b
```
# Find the unique string
There is an array of strings. All strings contains similar _letters_ except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'

```py
def find_uniq(arr):
  for x in range(0,len(arr)):
    c = set(sorted(arr[x-1].lower()))
    a = set(sorted(arr[x].lower()))
    b = set(sorted(arr[x+1].lower()))
    if a != b:
      if a!=c:
        return arr[x]
      else:
        return arr[x+1]

# Clever Solution
def find_uniq(arr):
    if set(arr[0].lower()) == set(arr[1].lower()):
        majority_set = set(arr[0].lower())
    elif set(arr[0].lower()) == set(arr[2].lower()):
        majority_set = set(arr[0].lower())
    else:
        majority_set = set(arr[1].lower())
    
    for string in arr:
        if set(string.lower()) != majority_set:
            return string
```
# Isograms
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

**Example: (Input --> Output)**
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

**Example: (Input --> Output)**
```
"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
```

```py
def is_isogram(string):
  _str = 'abcdefghijklmnopqrstuvwxyz'
  if string == "":
    return True
  for x in string.lower() :
    if string.lower().count(x.lower()) > 1 or x.isdigit():
      return False
  return True

# Clever Solution
def is_isogram(string):
    return len(string) == len(set(string.lower()))
```
# Calculate BMI
Write function bmi that calculates body mass index (bmi = weight / height<sup>2</sup>).


if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"Write function bmi that calculates body mass index (bmi = weight / height<sup>2</sup>).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
```py
def bmi(weight, height):
    if weight/height**2 <= 18.5:
      return 'Underweight'
    if weight/height**2 <= 25.0:
      return 'Normal'
    if weight/height**2 <= 30.0:
      return 'Overweight'
    if weight/height**2 > 30:
      return 'Obese'

# Clever Solution
def bmi(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]
```
# Shortest Word
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

```py
def find_short(s):
  mini = 100
  for x in s.split():
    if len(x) < mini:
      mini = len(x)
  return mini 

# Clever Solution
def find_short(s):
    return min(len(x) for x in s.split())
```
