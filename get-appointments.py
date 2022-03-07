import requests
url = 'https://pass-og-id.politiet.no/qmaticwebbooking/rest/schedule/branches/'

def getStations(url):
  response = requests.get(url)
  data = response.json()
  return data

def getDates(url, id):
  response = requests.get(url + id + '/dates') #Exception when fetching dates for multiple services and people
  data = response.json()
  return data

def getTimes(url, id, date):
  response = requests.get(url + id + '/dates/' + date + '/times') #Probably: Exception when fetching dates for multiple services and people
  data = response.json()
  return data

stations = getStations(url)
station_dates = []
for station in stations:
  station_dates.append(station['id'])
  dates = getDates(url, station['id'])
  for date in dates:
    station_dates[station['id']].append(date)
    times = getTimes(url, station['id'], date)
    for time in times:
      station_dates[station['id']][date].append(time)

print(station_dates)
