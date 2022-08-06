from utilities import *


# ---------------- EVERY TIME ADD NEW KATA AT END OF URLS LIST --------------- #

urls = [
  'https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3', # Abbreviate a Two Word Name
  'https://www.codewars.com/kata/550498447451fbbd7600041c', # Are they the same
  'https://www.codewars.com/kata/57356c55867b9b7a60000bd7', # Basic Mathematical Operations
  'https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39', # Calculating with Functions
  'https://www.codewars.com/kata/5265326f5fda8eb1160004c8', # Convert a Number to a String
  'https://www.codewars.com/kata/544675c6f971f7399a000e79', # Convert a String to a Number
  'https://www.codewars.com/kata/517abf86da9663f1d2000003', # Convert string to camel case
  'https://www.codewars.com/kata/54edbc7200b811e956000556', # Counting sheep
  'https://www.codewars.com/kata/52fba66badcd10859f00097e', # Disemvowel Trolls
  'https://www.codewars.com/kata/53da3dbb4a5168369a0000fe', # Even or Odd
  'https://www.codewars.com/kata/54da5a58ea159efa38000836', # Find the odd int
  'https://www.codewars.com/kata/563b662a59afc2b5120000c6', # Growth of a Population
  'https://www.codewars.com/kata/554b4ac871d6813a03000035', # Highest and Lowest
  'https://www.codewars.com/kata/526dbd6c8c0eb53254000110', # Not very secure
  'https://www.codewars.com/kata/57eae20f5500ad98e50002c5', # Remove String Spaces
  'https://www.codewars.com/kata/515bb423de843ea99400000a', # PaginationHelper
  'https://www.codewars.com/kata/5552101f47fc5178b1000050', # Playing with digits
  'https://www.codewars.com/kata/54d512e62a5e54c96200019e', # Primes in numbers
  'https://www.codewars.com/kata/52e1476c8147a7547a000811', # Regex Password Validation
  'https://www.codewars.com/kata/513e08acc600c94f01000001', # RGB To Hex conversion
  'https://www.codewars.com/kata/530e15517bc88ac656000716', # Rot13
  'https://www.codewars.com/kata/578aa45ee9fd15ff4600090d', # Sort the odd
  'https://www.codewars.com/kata/546e2562b03326a88e000020', # Square Every Digit
  'https://www.codewars.com/kata/57a0e5c372292dd76d000d7e', # String repeat
  'https://www.codewars.com/kata/55fd2d567d94ac3bc9000064', # Sum of odd numbers
  'https://www.codewars.com/kata/54da539698b8a2ad76000228', # Take a Ten Minutes Walk
  'https://www.codewars.com/kata/556deca17c58da83c00002db', # Tribonacci Sequence
  'https://www.codewars.com/kata/5656b6906de340bd1b0000ac', # Two to one
  'https://www.codewars.com/kata/54e6533c92449cc251001667', # Unique In Order
  'https://www.codewars.com/kata/52774a314c2333f0a7000688', # Valid Parentheses
  'https://www.codewars.com/kata/54ff3102c1bad923760001f3', # Vowel Count
  'https://www.codewars.com/kata/523a86aa4230ebb5420001e1', # Where my anagrams at
  'https://www.codewars.com/kata/5266876b8f4bf2da9b000362', # Who likes it
  'https://www.codewars.com/kata/55f2b110f61eb01779000053', # Beginner Series #3 Sum of Numbers
  'https://www.codewars.com/kata/576757b1df89ecf5bd00073b', # Build Tower
  'https://www.codewars.com/kata/57675f3dedc6f728ee000256', # Build Tower Advanced
  'https://www.codewars.com/kata/551b4501ac0447318f0009cd', # Convert a Boolean to a String
  'https://www.codewars.com/kata/523b4ff7adca849afe000035', # Function 1 - hello world
  'https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad', # Invert values
  'https://www.codewars.com/kata/5259b20d6021e9e14c0010d4', # Reverse words
  'https://www.codewars.com/kata/545cedaa9943f7fe7b000048', # Detect Pangram
  'https://www.codewars.com/kata/555086d53eac039a2a000083', # Opposites Attract
  'https://www.codewars.com/kata/56541980fa08ab47a0000040', # Printer Errors
  'https://www.codewars.com/kata/585d7d5adb20cf33cb000235', # Find the unique number
  'https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3', # Find the unique string
  'https://www.codewars.com/kata/54ba84be607a92aa900000f1', # Isograms
  'https://www.codewars.com/kata/57a429e253ba3381850000fb', # Calculate BMI
  'https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9', # Shortest Word
  'https://www.codewars.com/kata/57eae65a4321032ce000002d', # Fake Binary
]

# ------------------------------ ONLY SEND 1 URL ----------------------------- #
print('Select From List Below:')
print('1 - Create Challenge Flile')
print('2 - Add Solution To `Codewars.md`')
print('3 - ReCreate The `Codewars.md`')
match input('Enter the number: '):
  case '1' :
    data = getJson(urls[-1])
    createSolutionFile(data['name'])
  case '2' :
    writer(urls[-1])
  case '3' :
    reset()
    for url in urls:
      writer(url)
