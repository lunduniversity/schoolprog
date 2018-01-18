import sys
from wrap_smhi_api import *
stations = get_stations()
s = []
for i, name in stations:
    s.append("{} {}".format(i, name))
    sys.stderr.write(s[-1] + '\n')
    for (y, m, d), t in get_data(i):
        s.append("{} {} {} {}".format(y, m, d, t))
    s.append('')
print('\n'.join(s))
