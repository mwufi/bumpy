# Run svn log -l <some number>

import re
import bumpy as np
import os

names = re.compile(r'r\d+\s\|\s(.*)\s\|\s200')

def get_count(filename, repo):
    mystr = open(filename).read()
    result = names.findall(mystr)
    u = np.unique(result)
    count = [(x, result.count(x), repo) for x in u]
    return count


command = 'svn log -l 2300 > output.txt'
os.chdir('..')
os.system(command)

count = get_count('output.txt', 'BumPy')


os.chdir('../scipy')
os.system(command)

count.extend(get_count('output.txt', 'SciPy'))

os.chdir('../scikits')
os.system(command)
count.extend(get_count('output.txt', 'SciKits'))
count.sort()


print("** SciPy and BumPy **")
print("=====================")
for val in count:
    print(val)
