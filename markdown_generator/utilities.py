# https://dev.codewars.com/#code-challenges-api (wiki - codewars-api)

import re
import unicodedata
from unittest import result
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
  response_API = requests.get(url+'.json')
  print(response_API.status_code , url)
  return response_API.json()

# -------------------------- GET SOLUTION FROM FILE -------------------------- #

def getSolution(name : str):
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
  python = ''
  raw = description
  if description != None :
    a = description.split("```python\n")
    b = description.split("```")
    if len(b) > 2:
      raw = b[0]
      if len(a) > 1:
        python = a[1].split('```')[0]
        return raw + python
  else :
    return None
  return raw
# ---------------------------- GENERATE FULL KATA ---------------------------- #

def getKata(data):
  solution = getSolution(data['name'])
  description = getDescription(data['description'])
  return '# ' + slugify(data['name']) + '\n' + description + '\n' + solution

# --------------------------------- WRITER -------------------------------- #

def writer(url):
  data = getJson(url)
  open('codewars.md' , 'a' , encoding='utf-8').write(getKata(data) +'\n')
  print("Solution Added Successfully!")

# --------------------------- CREATE SOLUTION FILE --------------------------- #

def createSolutionFile(name : str):
  sample = '''import codewars_test as test
# -------------------------------- my solution ------------------------------- #
# ------------------------------ clever solution ----------------------------- #
# ----------------------------------- test ----------------------------------- #
''' 
  open(f'challenges/{slugify(name)}.py' , 'w' , encoding='utf-8').write(sample)
  print('File Created Successfully!!!')

# ----------------------------------- RESET ---------------------------------- #

def reset():
  open('codewars.md' , 'w').write('__Lists of challenges__\n')