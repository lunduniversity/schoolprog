import json, re
import os.path
from urllib import request

def __base():
    return 'https://opendata-download-metobs.smhi.se/api/version/latest'

def __getjson(url):
    return json.loads('\n'.join(__getraw(url)))

def __getraw(url):
    try:
        os.stat('cache')
    except:
        os.mkdir('cache')
    path = 'cache/' + url.replace(__base(), 'latest').replace('/', '.')
    if os.path.isfile(path):
        with open(path, 'r') as f:
            content = [l.replace('\n', '') for l in f.readlines()]
    else: 
        data = request.urlopen(url).read().decode('utf-8')
        with open(path, 'w') as f:
            f.write(data)
        content = data.split('\n')
    return content

def __parameters():
    apidump = __getjson(__base() + '.json')
    rs = apidump['resource']
    for r in sorted(rs, key=lambda x: int(x['key'])):
        yield (int(r['key']), r['summary'])

def __get_stations(param):
    stationurl = __base() + '/parameter/'+ str(param) + '.json'
    stationpage = __getjson(stationurl)
    stations = stationpage['station']
    return [(s['id'], s['name']) for s in sorted(stations, key=lambda x: x['name'])]

def get_stations():
    return __get_stations(2)

def __get_raw_data(station_id, parameter):
    url = ''.join([
        __base(),
        '/parameter/',
        str(parameter),
        '/station/',
        str(station_id),
        '/period/corrected-archive/data.csv'])
    return __getraw(url)

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
