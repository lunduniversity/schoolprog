from fetchdata import *

stations = get_stations()
for i, name in stations[:10]:
    print(i, name)
    print(get_data(i)[:10])
