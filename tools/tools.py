import os
from pathlib import *
import re
import shutil
import unicodedata
import requests
import json


code_response = 100 # everything run successfully!

def createFolder(path):
  """
  Get a path contains (path_parrent/foldername)
  If the path doesn't exist, create it
  
  :param path: The path to the folder you want to create
  """
  try:
    if not os.path.exists(Path(path)):
      os.mkdir(Path(path))
  except:
    code_response = 201 # createFolder failed
    return code_response

def transferFiles(filelist , distination , method = 'copy'):
  """
  It takes a list of files and moves them to a destination folder
  
  :param filelist: a list of files to move contains (parentPath / filesname.filetype) exp: root/hello.txt
  :param distination: The folder you want to move the files to
  """
  try:
    if method == 'move':
      for f in filelist:
        shutil.move(f, distination)
    if method == 'copy':
      for f in filelist:
        shutil.copy(f, distination)

  except:
    code_response = 202 # MoveFiles failed
    return code_response

def getAllFiles(directoryName , filetype):
  """
  It takes a directory name and a filetype as input and returns a list of all the files in the
  directory with the given filetype
  
  :param directoryName: The directory where the files are located
  :param filetype: The type of file you want to get
  :return: A list of all the files in the directory with the filetype specified.
  """
  try:
    return [txt_path for txt_path in Path(directoryName).glob("*."+filetype)]
  except:
    code_response = 203 # getAllFiles failed
    return code_response

def createFileForce(filename : str , data = ""):
  """
  > Create a file with the given filename, creating any necessary directories along the way
  
  :param filename: The name of the file to create (path / file.etc)
  :type filename: str
  """
  try:
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
      f.write(data)
  except:
    code_response = 204
    return code_response # createFileForce failed

def dumper(filename : str , data , location : str):
  """
  It takes a filename, some data, and a location, and writes the data to a file with the filename in
  the location
  
  :param filename: The name of the file you want to save
  :type filename: str
  :param data: The data to be dumped
  :param location: This is the location where you want to save the file
  :type location: str
  """
  try:
    match location:
      case 'review':
        path = Path('test/review')
        path = path / filename
        path.write_text(data)
      case 'data':
        path = Path('json')
        path = path / filename
        createFileForce(path)
        with open(path , 'w' , encoding='utf-8') as f:
          json.dump(data , f , indent=2)
  except:
    code_response  = 205 # dumper failed
    return code_response

def getFOF(folder = '*' , filename  = '*' , type = '*'):
  """
  It returns a list of all the files in the current directory and all its subdirectories that match
  the given folder, filename and type
  :param folder: The folder name you want to search for, defaults to * (optional)
  :param filename: The name of the file you want to find, defaults to * (optional) , is a selector for mrthod to retrun folders path only (select 'dir') defaulr is none for files
  :param type: the file type you want to search for, defaults to * (optional)
  :return:
    getFOF(slug , 'dir' , '*') return path/slug
    getFOF(slug , 'a' , '*') return path/slug/a.*
    getFOF(slug , 'a' , 'py') return path/slug/a.py
  """
  try:
    if filename == 'dir':
      return Path('.').glob(f'**/{folder}')
    else :
      return Path('.').glob(f'**/{folder}/{filename}.{type}')
  except:
    code_response = 206 # getFOF failed
    return code_response

def getJsonByURL(url):
  """
  It takes a url as an argument, makes a request to that url, and returns the json response
  
  :param url: The URL of the subreddit you want to scrape
  :return: A JSON object
  """
  try:
    response_API = requests.get(url+'.json')
    print(response_API.status_code , url)
    return response_API.json()
  except:
    code_response = 207 # getJsonByUrl failed
    return code_response

def slugify_sanitize(value, slug=True , allow_unicode=False):
  """
  It takes a string, removes all non-alphanumeric characters, and replaces spaces with dashes depend on slug param
  
  :param value: The string to be slugified
  :param allow_unicode: If True, then non-ASCII characters will be allowed. If False, all non-ASCII
  characters will be removed, defaults to False (optional)
  :param slug: True or False, default to `True` (optional) sanitized slug value `False` return sanitized value with space
  :return: A string that is lowercase, has no special characters, and has no spaces.
  """
  """
  Taken from https://github.com/django/django/blob/master/django/utils/text.py
  Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
  dashes to single dashes. Remove characters that aren't alphanumerics,
  underscores, or hyphens. Convert to lowercase. Also strip leading and
  trailing whitespace, dashes, and underscores.
  """
  try:
    value = str(value)
    if allow_unicode:
      value = unicodedata.normalize('NFKC', value)
    else:
      value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    match slug:
      case False:
        value = re.sub(r'[^\w\s-]', '', value)
        return re.sub(r'[-\s]+', ' ', value).strip(' _')
      case True:
        value = re.sub(r'[^\w\s-]', '', value.lower())
        return re.sub(r'[-\s]+', '-', value).strip('-_')
  except:
    code_response = 208 # slugify_sanitize failed
    return code_response

def getPythonSolution(path : str):
  """
  It reads the text of the file at the given path, splits it into two parts at the first occurrence of
  the string '# -------------------------------- my solution ------------------------------- #', and
  then splits the second part into two parts at the first occurrence of the string '#
  ----------------------------------- test ----------------------------------- #'. The function
  returns the first part of the second part
  
  :param path: the path to the file you want to read
  :type path: str
  :return: The solution to the problem.
  """
  try:
    a = Path(path)
    c1 = '# -------------------------------- my solution ------------------------------- #'
    c2 = '# ----------------------------------- test ----------------------------------- #'
    return a.read_text().split(c1)[1].split(c2)
  except:
    code_response = 209 # getPythonSolution failed
    return code_response

def getDescription(text : str) :
  """
  It takes a string and returns a string.
  
  :param text: The text to be parsed
  :type text: str
  :return: The description of the command.
  """
  try:
    if '```python' in text:
      c1 = '```python'
      c2 = '```'
      if '```lua' in text:
        py = text.split(c1)[1].split(c2)[0]
        c3 = '```lua'
        full = text.split(c3)[0] + py
      else :
        py = text.split(c1)[1].split(c2)[0]
        c3 = '```javascript'
        full = text.split(c3)[0] + py
    else : full = text
    return full
  except:
    code_response = 210 # getDescription failed
    return code_response

def getSolution(slug : str):
  """
  It takes the slug of a kata, finds the solution file, and returns the solution code
  
  :param slug: the name of the kata
  :type slug: str
  :return: The solution to the kata.
  """
  try:
    solpath = list(getFOF('katas' , slug , 'py'))
    c1 = '# -------------------------------- MY SOLUTION ------------------------------- #'
    c2 = '# ------------------------------ CLEVER SOLUTION ----------------------------- #'
    c3 = '# ----------------------------------- TEST ----------------------------------- #'
    txt = open(solpath[0]).read()
    if c2 in txt:
      txt = txt.split(c1)[1].split(c3)[0].replace(c2 , '# clever solution')
    return txt
  except:
    code_response = 211 # getSolution failed
    return code_response

def remover(slug):
  """
  It removes the folder and the file that are associated with the slug
  
  :param slug: The name of the file you want to remove
  """
  try:
    cf = list(getFOF(slug))
    df = list(getFOF('json' , slug , 'json'))
    shutil.rmtree(cf[0])
    os.remove(df[0])
  except:
    code_response = 212 # remover failed
    return code_response

def save(slug : str):
  """
  It takes a slug, creates a folder, moves a file, and creates a markdown file
  
  :param slug: the name of the kata
  :type slug: str
  """
  try:
    data = json.load(open(f'json/{slug}.json'))
    katapath = Path('katas') / data['rank']['name'] / slug
    createFolder(katapath)

    file = [Path('generator/kata.py')]
    transferFiles(file , katapath / 'solution.py')
    txt = "# " + data['name']

    f = list(getFOF('json' , slug , 'json'))[0]
    data = json.load(open(f))

    des = getDescription(data['description'])
    # sol = getSolution(slug)

    # txt += '\n' + des + '\n' + '```py' + sol + '```'
    txt += '\n' + des
    createFileForce(str(katapath / 'description.md') , txt)
  except:
    code_response = 213 # save failed
    return code_response

def load(slug : str):
  """
  It creates a file called kata.py in the generator folder, and writes the following text to it:
  
  {slug}

  import codewars_test as test

  -------------------------------- MY SOLUTION -------------------------------

  ------------------------------ CLEVER SOLUTION -----------------------------

  ----------------------------------- TEST -----------------------------------
  
  The {slug} part is replaced with the slug of the kata you're working on
  
  :param slug: the slug of the kata you want to load
  :type slug: str
  """
  try:
    c1 = '# -------------------------------- MY SOLUTION ------------------------------- #'
    c2 = '# ------------------------------ CLEVER SOLUTION ----------------------------- #'
    c3 = '# ----------------------------------- TEST ----------------------------------- #'
    txt = "\n".join([f'# {slug}' , 'import codewars_test as test' ,  c1 ,c2 , c3])
    Path('generator/kata.py').write_text(txt)
  except:
    code_response = 214 # load failed
    return code_response

def linkSorter():
  """
  It sorts the links in the link.txt file
  """
  try:
    p = Path('generator/link.txt')
    links = open(p).read().splitlines()
    np = 'generator/temp.txt'
    createFileForce('generator/temp.txt' , "".join(sorted(links)))
    links = open(np).read()
    open(p).write(links)
  except:
    code_response = 215 # linkSorter failed
    return code_response

def linkSaver(url , name):
  """
  It takes a url and a name, and appends it to a text file
  
  :param url: The url of the link
  :param name: The name of the link
  """
  try:
    p = Path('generator/link.txt')
    link = url + ', # ' + name
    open(p , 'a').write("\n"+link)
    linkSorter()
  except:
    code_response = 216 # linkSaver failed
    return code_response

def getNameKata():
  """
  It opens the file `generator/kata.py`, reads the first line, splits it into two parts at the `# `,
  and returns the second part
  :return: The name of the kata
  """
  try:
    slug = open('generator/kata.py').read().splitlines()[0].split('# ')[1]
    return json.load(open(f'json/{slug}.json'))['name']
  except:
    code_response = 217 # getNameKata failed
    return code_response

def handler():
  print('Select From List Below:')
  print('0 - Exit')
  print('1 - Load')
  print('2 - Save')
  print('3 - Remove')
  print('4 - Get name of kata')
  match input("Enter the number: "):
    case '0':
      exit()
    case '1':
      url = input('Enter url: ')
      name = input('Enter name: ')
      linkSaver(url , name)
      data = getJsonByURL(url)
      load(data['slug'])
      # p = Path('json') / f"{data['slug']}.json"
      dumper(f"{data['slug']}.json" , data , 'data')
    case '2':
      slug = open('generator/kata.py').read().splitlines()[0].split('# ')[1]
      save(slug)
    case '3':
      remover(input('Enter the slug of kata: '))
    case '4':
      print(getNameKata())
