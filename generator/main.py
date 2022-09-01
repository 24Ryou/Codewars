import sys , os
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '')))
from tools.utilities import *
from tools.tools import *

# --------------------------------- DUMP JSON -------------------------------- #

# urls = open(Path('generator/link.txt')).read().splitlines()
# urls = [x.split(', # ')[0] for x in urls]
# datas = []
# for url in urls :
#   datas.append(getJsonByURL(url))
# for data in datas:
#   dumper(data['slug']+'.json' , data , 'data')


# ----------------------------- CATEGORIZE KATAS ----------------------------- #

# datas = []
# names = []
# solutions = []
# pfs = getAllFiles('json' , 'json')
# for pf in pfs:
#   datas.append(json.load(open(pf)))

# for data in datas:
#   names.append(slugify_sanitize(data['name'] , False))

# for name in names:
#   name = name + '.py'
#   p = Path('katas') / name
#   solutions.append(open(p).read())

# p = Path('katas')
# for data , solution in zip(datas , solutions):
#   createFileForce(p / data['rank']['name'] /data['slug'] / 'solution.py' , solution)

# for data in datas:
#   des = getDescription(data['description'])
#   createFileForce(p / data['rank']['name'] /data['slug'] / 'description.md' , des)

# -------------------------------- CODEWARS.MD ------------------------------- #

# files = [x for x in os.walk('katas')]
# print(files)

# ----------------------------------- MAIN ----------------------------------- #

handler()