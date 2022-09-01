import codewars_test as test
# -------------------------------- MY SOLUTION ------------------------------- #
class RomanNumerals:
  sym = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
  num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

  def to_roman(number):
    result = ''
    pointer = 0
    while number:
      div = number // RomanNumerals.num[pointer]
      number %= RomanNumerals.num[pointer]
      while div:
        result += RomanNumerals.sym[pointer]
        div -= 1
      pointer += 1
    return result

  def from_roman(roman_numeral):
    result = 0
    for idx, val in enumerate(roman_numeral):
      first_num = RomanNumerals.num[RomanNumerals.sym.index(val)]
      second_num = RomanNumerals.num[RomanNumerals.sym.index(roman_numeral[idx + 1])] if idx + 1 != len(
        roman_numeral) else -1
      if first_num >= second_num:
        result += first_num
      else:
        result -= first_num
    return result
# ------------------------------ CLEVER SOLUTION ----------------------------- #
import string
from collections import OrderedDict

class RomanNumerals:
  @classmethod
  def to_roman(self, num):
    conversions = OrderedDict([('M',1000), ('CM',900), ('D', 500), ('CD',400), ('C',100), ('XC',90), ('L',50), ('XL',40),
                               ('X',10), ('IX',9), ('V',5), ('IV',4), ('I',1)])
    out = ''
    for key, value in conversions.items():
      while num >= value:
        out += key
        num -= value
    return out
  
  @classmethod
  def from_roman(self, roman):
    conversions = OrderedDict([('CM',900), ('CD',400), ('XC',90), ('XL',40), ('IX',9), ('IV',4), ('M',1000), ('D',500),
                               ('C',100), ('L',50), ('X',10), ('V',5), ('I',1)])
    out = 0
    for key, value in conversions.iteritems():
      out += value * roman.count(key)
      roman = string.replace(roman, key, "")
    return out
# ----------------------------------- TEST ----------------------------------- #
@test.describe('sample_tests')
def sample_tests():
    @test.it('to roman')
    def sample_tests_to():
        test.assert_equals(RomanNumerals.to_roman(1000), 'M', '1000 should == "M"')
        test.assert_equals(RomanNumerals.to_roman(4), 'IV', '4 should == "IV"')
        test.assert_equals(RomanNumerals.to_roman(1), 'I', '1 should == "I"')
        test.assert_equals(RomanNumerals.to_roman(1990), 'MCMXC', '1990 should == "MCMXC"')
        test.assert_equals(RomanNumerals.to_roman(2008), 'MMVIII', '2008 should == "MMVIII"')
    @test.it('from roman')
    def sample_tests_from():
        test.assert_equals(RomanNumerals.from_roman('XXI'), 21, 'XXI should == 21')
        test.assert_equals(RomanNumerals.from_roman('I'), 1, 'I should == 1')
        test.assert_equals(RomanNumerals.from_roman('IV'), 4, 'IV should == 4')
        test.assert_equals(RomanNumerals.from_roman('MMVIII'), 2008, 'MMVIII should == 2008')
        test.assert_equals(RomanNumerals.from_roman('MDCLXVI'), 1666, 'MDCLXVI should == 1666')