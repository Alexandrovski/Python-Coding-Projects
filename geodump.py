import sqlite3
import json
import codecs

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0

for row in cur :
    data = str(row[1].decode())
    #convert to string and then parse
    try: js = json.loads(str(data))
    #skip if anyting is wrong with json
    except: continue

    #check for status
    if not('status' in js and js['status'] == "OK") : continue

    #results is an array
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 : continue

    #take the actual address out of the formatted address
    where = js["results"][0]['formatted_address']

    #get rid of single quotes
    where = where.replace("'", "")

    try :
        print(where, lat, lng)

        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+", "+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue
