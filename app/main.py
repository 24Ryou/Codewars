import sys , os
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '')))
# from tools.utilities import *
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

# ------------------------------- FIX SOLUTIONS ------------------------------ #

# cb1 = '# -------------------------------- my solution ------------------------------- #'
# cb2 = '# ------------------------------ clever solution ----------------------------- #'
# cb3 = '# ----------------------------------- test ----------------------------------- #'

# ca1 = '# -------------------------------- MY SOLUTION ------------------------------- #'
# ca2 = '# ------------------------------ CLEVER SOLUTION ----------------------------- #'
# ca3 = '# ----------------------------------- TEST ----------------------------------- #'

# datas = []
# solutions = []
# jsons = list(getAllFiles('json' , 'json'))
# for x in jsons:
#   datas.append(json.load(open(x)))
# for data in datas:
# #   solution = getSolution(f"{data['rank']['name']}/{data['slug']}/solution")
#   p = Path('katas') / data['rank']['name'] / data['slug'] / 'solution.py'
#   sol = open(p).read()
#   sol = sol.replace(cb1 , ca1)
#   sol = sol.replace(cb2 , ca2)
#   sol = sol.replace(cb3 , ca3)
#   open(p , 'w' , encoding='utf-8').write(sol)

# -------------------------------- CODEWARS.MD ------------------------------- #

# datas = []
# katas = []
# descriptions = []
# solutions = []
# kata = []
# jsons = list(getAllFiles('json' , 'json'))
# for x in jsons:
#   datas.append(json.load(open(x)))
# for data in datas:
#   solution = '```py\n' + getSolution(f"{data['rank']['name']}/{data['slug']}/solution") + '```'
#   solutions.append(solution)
#   description = getDescription(data['description'])
#   descriptions.append(description)
#   kata.append('# ' + data['name'])
#   kata.append(str(description))
#   kata.append(str(solution))
#   katas.append("\n".join(kata))


# open('codewars.md' , 'w' , encoding='utf-8').write("\n".join(katas)

# ----------------------------------- MAIN ----------------------------------- #

handler()