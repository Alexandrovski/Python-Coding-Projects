import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/geojson?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

#caching geo geodata
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

#ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data")
count = 0
for line in fh:
    if count > 200 :
        print("Retrieved 200 locations, restart to retrieve more")
        break

    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print("Foundin database ", address)
        continue
    except:
        pass
    parms = dict()
    parms["query"] = address
    if api_key is not False: parms["key"] = api_key
    #url encode adds the + and ?, etc.
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retreiving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    # try to parse the json database
    try:
        js = json.loads(data)
    except:
        print(data) #we print in case unicode causes an error
        continue
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('=== Failure to Retrieve ===')
        print(data)
        break
    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ?)''', (memoryview(address.encode()), memoryview(data.encode())))
    conn.commit()
    if count % 10 == 0 :
        print('Pasuing for a bit...')
        time.sleep(5)
print("Run geodump.py to read the data form the database so you can visualize it on a map` ")
