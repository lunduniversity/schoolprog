import sys
from wrap_smhi_api import *
from collections import defaultdict
stations = get_stations()
s = []
for i, name in stations:
    sys.stderr.write(name + '\n')
    fst = True
    data = list(get_data(i))
    if len(data) < 20000: continue
    for (y, m, d), t in get_data(i):
        if fst and y!=1961:
            break
        elif fst:
            fst = False
            s.append("{} {}".format(i, name))
        s.append("{} {} {} {}".format(y, m, d, t))
    if not fst:
        s.append('')
print('\n'.join(s))
