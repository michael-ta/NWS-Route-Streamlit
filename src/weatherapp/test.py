import urllib
import urllib.request
import urllib.parse
import time
import json
import os

coords = {'Ludlow,KY': (39.094712, -84.544654),
          'Louisville,KY':(38.254311, -85.760994),
          'Nashville,TN': (36.166067, -86.777802),
          'Memphis,TN': (35.149086, -90.052717),
          'Little Rock,AR': (34.748809, -92.275649),
          'Texarkana,TX': (33.421140, -94.045561)}

coords = {'Ludlow,KY': (39.094712, -84.544654),
          'Indianapolis,IN': (39.767926, -86.154394),
          'St. Louis,MO': (38.627631, -90.199087),
          'Springfield,MO': (37.216975, -93.292412),
          'Tulsa,OK': (36.155046, -95.989553),
          'Plano,TX': (33.021829, -96.699255)}

BASEURL = {'NWS':  'https://api.weather.gov/',
           'PS': 'http://api.positionstack.com/v1/forward'}

POSITIONSTACK_API_KEY = os.environ.get("POSITIONSTACK_API_KEY")

def get_longlat(place: str) -> json:
  global BASEURL, POSITIONSTACK_API_KEY
  params = {'access_key': POSITIONSTACK_API_KEY,
            'query': place}
  url = BASEURL['PS'] + '?' + urllib.parse.urlencode(params)
  return url

def get_forecast_endpoint(coord):
  global BASEURL
  endpoint = 'points/'
  url = BASEURL + endpoint + f'{coord[0]},{coord[1]}'
  resp = urllib.request.urlopen(url)
  if resp.status == 200:
    return json.loads(resp.read())
  else:
    raise Exception(f'Error could not retrieve forecast for {coord}')   

def get_forecast(url):
  resp = urllib.request.urlopen(url)
  if resp.status == 200:
    return json.loads(resp.read())
  else:
    raise Exception(f'Error could not retrieve forecast')

def wrap_text(t, n=80, indent=''):
  split_t = t.split(' ')
  count = 0
  tmp_line = []
  line = []
  for w in split_t:
    if count + len(w) > n:
      if len(tmp_line) > 0:
        line.append(' '.join(tmp_line))
        tmp_line = [w]
      else:
        line.append(w)
        tmp_line = []
      count = 0
    else:
      count += len(w)
      tmp_line.append(w)
  
  line.append(' '.join(tmp_line))
  return f'\n{indent}'.join(line)
