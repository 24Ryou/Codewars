# https://dev.codewars.com/#code-challenges-api (wiki - codewars-api)

import os
import re
import unicodedata
import requests
import sys
from pathlib import Path

# add challenges path at end of sys.path => sys.path[-1]
sys.path.append('''d:\\Ali\\Projects\\_Study\\Codewars\\challenges''')

# ------------------------- SANIITZE THE NAME OF FILE ------------------------ #

def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """

    # change value.lower() -> value #1
    # change sub('-').strip('-_') -> sub(' ').strip(' _') #2
    
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value) #1
    return re.sub(r'[-\s]+', ' ', value).strip(' _') #2

# ----------------------------- GET DATA FROM API ---------------------------- #

def getJson(url):
  """
  It takes a url as an argument, makes a request to that url, and returns the json response
  
  :param url: The URL of the subreddit you want to scrape
  :return: A JSON object
  """
  response_API = requests.get(url+'.json')
  print(response_API.status_code , url)
  return response_API.json()

# -------------------------- GET SOLUTION FROM FILE -------------------------- #

def getSolution(name : str):
  """
  It takes a string, `name`, and returns a string, `result`, which is the solution to the challenge
  with the name `name`
  
  :param name: The name of the challenge you want to get the solution for
  :type name: str
  :return: The solution to the challenge
  """
  try:
    q = Path('challenges') / f'{slugify(name)}.py'
    raw = q.open(encoding='utf-8').read().split('#')
    if len(raw) < 7:
      result  ='```py' + raw[2] + '```'
    else:
      result = '```py' + raw[2] + '\n' + '# Clever Solution' + raw[4] + '```'
    return result
  except Exception as e:
    exception_type, exception_object, exception_traceback = sys.exc_info()
    filename = exception_traceback.tb_frame.f_code.co_filename
    line_number = exception_traceback.tb_lineno
    print("Exception type: ", exception_type)
    print("File name: ", filename)
    print("Line number: ", line_number)
    exit()

# ------------------------ GET PYTHON CODE DESCRIPTION ----------------------- #

def getPythonDes(description = None):
  """
  It takes a string as input and returns the python code from the string
  
  :param description: The description of the function
  :return: the description of the function.
  """
  if description != None :
    a = description.split("```python\n")
    if len(a) > 1:
      return a[1].split('```')[0]

    else :
      return a[0].replace('\n'*3 , '\n'*2)
  else:
    return None

# ------------------------ GET CODE-LESS description ------------------------ #

def getRawDes(description = None):
  """
  It takes a string and returns the first part of the string if it contains a triple backtick (
  
  :param description: The description of the issue
  :return: The first part of the description.
  """
  if description != None :
    b = description.split("```")
    if len(b) > 2:
      return b[0]
    else :
      return description
  else:
    return None

# ------------------------ GENERATE FULL description ------------------------ #

def getDescription(description = None):
  """
  It takes a string, splits it into two parts, and returns the first part
  
  :param description: The description of the post
  :return: The description of the question.
  """
  python = ''
  raw = description
  if description != None :
    a = description.split("```python\n")
    b = description.split("```")
    if len(b) > 2:
      raw = b[0]
      if len(a) > 1:
        python = a[1].split('```')[0]
        return cleaner(raw + python)
  else :
    return None
  return cleaner(raw)
# ---------------------------- GENERATE FULL KATA ---------------------------- #

def getKata(data):
  """
  It takes a dictionary of kata data, gets the solution, gets the description, and returns a markdown
  string
  
  :param data: This is the data that is passed to the function. It is a dictionary that contains the
  name of the kata, the description, and the id
  :return: A string with the markdown format of the kata.
  """
  solution = getSolution(data['name'])
  id = data['id']+'.txt'
  path = 'markdown_generator/manual_descriptions'
  description = getDescription(data['description']) if isBug(id , path) == None else getManualDescription(isBug(id , path))
  return '# ' + slugify(data['name']) + '\n' + description + '\n' + solution

# --------------------------------- WRITER -------------------------------- #

def writer(url):
  """
  It takes a url, gets the json data from the url, and writes the kata to a markdown file
  
  :param url: The url of the kata you want to add
  """
  data = getJson(url)
  open('codewars.md' , 'a' , encoding='utf-8').write(getKata(data) +'\n')
  print("Kata Added Successfully!")

# --------------------------- CREATE SOLUTION FILE --------------------------- #

def createSolutionFile(name : str):
  """
  It creates a file with the name of the challenge and the extension .py in the challenges folder
  
  :param name: The name of the challenge
  :type name: str
  """
  sample = '''import codewars_test as test
# -------------------------------- my solution ------------------------------- #
# ------------------------------ clever solution ----------------------------- #
# ----------------------------------- test ----------------------------------- #
''' 
  open(f'challenges/{slugify(name)}.py' , 'w' , encoding='utf-8').write(sample)
  print('File Created Successfully!!!')

# ----------------------------------- RESET ---------------------------------- #

def reset():
  """
  It opens the file codewars.md and writes the string __Lists of challenges__\n to it
  """
  open('codewars.md' , 'w').write('__Lists of challenges__\n')

# ---------------------------- CLEAN DESCERIPTION ---------------------------- #

def cleaner(string : str):
  """
  It takes a string, splits it into lines, and then removes any lines that contain any of the items in
  the list returned by the `getEscape()` function
  
  :param string: The string to be cleaned
  :type string: str
  :return: A list of strings.
  """
  data = getEscape()
  out = []
  for line in string.splitlines():
    if not any(item in line for item in data):
      out.append(line)
  return '\n'.join(out)

# -------------------------- SET DATA ESCAPE LIST -------------------------- #

def setEscape(string : str):
  """
  It takes a string and adds it to the escape.txt file
  
  :param string: The string you want to add to the escape.txt file
  :type string: str
  """
  r = open('markdown_generator/escape.txt' , 'a' , encoding='utf-8').write(string)
  print(f'{string} Added To escape.txt Successfully!')

# ------------------------------ GET DATA ESCAPE ----------------------------- #

def getEscape():
  """
  It reads the escape.txt file and returns a list of all the escape characters
  :return: A list of strings.
  """
  return open('markdown_generator/escape.txt' , 'r' , encoding='utf-8').read().split()

# ------------------------ ADD TO MANUAL DESCRIPTIONS ------------------------ #

def addManualDescription(filename , string) :
  """
  > It creates a file in the `manual_descriptions` folder with the name of the file you want to add a
  description to, and writes the description to that file
  
  :param filename: The name of the file you want to create
  :param string: The string you want to write to the file
  """
  open(f'markdown_generator/manual_descriptions/{filename}.txt' , 'w' , encoding='utf-8').write(string)

# -------------- CHECK IF BUG_ID IS IN MANUAL DESCRIPTION FOLDER ------------- #

def isBug(name, path):
  """
  It takes a file name and a path, and returns the full path to the file if it exists in the path
  
  :param name: The name of the file you're looking for
  :param path: The path to the directory where you want to search for the file
  :return: The path to the file.
  """
  for root, dirs, files in os.walk(path):
    if name in files:
      return os.path.join(root, name)

# -------------------------- GET MAUNAL DESCRIPTION -------------------------- #

def getManualDescription(path) :
  """
  It reads the contents of a file and returns it as a string
  
  :param path: The path to the file you want to read
  :return: the contents of the file.
  """
  return open(path , 'r' , encoding='utf-8').read()