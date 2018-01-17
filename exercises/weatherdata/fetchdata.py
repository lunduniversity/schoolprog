import json, re
from urllib import request
base = 'https://opendata-download-metobs.smhi.se/api/version/latest'

def __get(url):
    return json.loads(__getraw(url))

def __getraw(url):
    return request.urlopen(url).read()

def __parameters():
    apidump = __get(base + '.json')
    rs = apidump['resource']
    for r in sorted(rs, key=lambda x: int(x['key'])):
        yield (int(r['key']), r['summary'])

def __get_stations(param):
    stationurl = base + '/parameter/'+ str(param) + '.json'
    stationpage = __get(stationurl)
    stations = stationpage['station']
    return [(s['id'], s['name']) for s in sorted(stations, key=lambda x: x['name'])]

def get_stations():
    return __get_stations(2)

def __get_raw_data(station_id, parameter):
    url = ''.join([
        base,
        '/parameter/',
        str(parameter),
        '/station/',
        str(station_id),
        '/period/corrected-archive/data.csv'])
    return __getraw(url).decode('utf-8').split('\n')


def get_data(station_id):
    data_points = []
    digit = "[0-9]"
    pattern = re.compile(digit*4 + '-' + digit*2 + '-' + digit*2)
    for l in __get_raw_data(station_id, 2):
        a = l.split(';')
        if len(a) > 3 and pattern.match(a[2]):
            y, m, d = map(int, a[2].split('-'))
            data_points.append(((y, m, d), float(a[3])))
    return sorted(data_points)

stations = get_stations()
print(stations[0])
data = get_data(stations[1][0])
for i in range(10):
    print(data[i])
