import os
from pathlib import *
import re
import shutil
import unicodedata
import requests

def createFolder(path):
  """
  Get a path contains (path_parrent/foldername)
  If the path doesn't exist, create it
  
  :param path: The path to the folder you want to create
  """
  if not os.path.exists(Path(path)):
    os.mkdir(Path(path))

def MoveFiles(filelist , distination):
  """
  It takes a list of files and moves them to a destination folder
  
  :param filelist: a list of files to move contains (parentPath / filesname.filetype) exp: root/hello.txt
  :param distination: The folder you want to move the files to
  """
  for f in filelist:
    shutil.move(f, distination)
  
def getAllFiles(directoryName , filetype):
  """
  It takes a directory name and a filetype as input and returns a list of all the files in the
  directory with the given filetype
  
  :param directoryName: The directory where the files are located
  :param filetype: The type of file you want to get
  :return: A list of all the files in the directory with the filetype specified.
  """
  return [txt_path for txt_path in Path(directoryName).glob("*."+filetype)]

def getJsonByURL(url):
  """
  It takes a url as an argument, makes a request to that url, and returns the json response
  
  :param url: The URL of the subreddit you want to scrape
  :return: A JSON object
  """
  response_API = requests.get(url+'.json')
  print(response_API.status_code , url)
  return response_API.json()

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

def getPythonSolution(path : str):
  a = Path(path)
  c1 = '# -------------------------------- my solution ------------------------------- #'
  c2 = '# ----------------------------------- test ----------------------------------- #'
  return a.read_text().split(c1)[1].split(c2)