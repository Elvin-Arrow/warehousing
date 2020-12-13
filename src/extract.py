import urllib.request, json
import pandas as pd

def minutes(hour, minute) :
    return minute + (hour * 60)
# with urllib.request.urlopen("http://flights-dw.herokuapp.com/flights?date=2020-01-03") as url:
#     data = json.loads(url.read().decode())
# print("data loaded")

# with open("2020_1.json", "w") as write_file:
#     json.dump(data, write_file)

# print("data saved")

# print("json to csv")

df = pd.read_json (r'2020_1.json')
# df.to_csv (r'2020_1.csv', index = None)
# print(df['flightNumber'].values)


flightNum = df['flightNumber'].values
source = df['origin'].values
destination = df['destination'].values
distance = df['distance'].values
duration = df['duration'].values

flightNumber = []
flights = {}
count = 0
for fn in flightNum:
    code = source[count]['code']
    dcode = destination[count]['code']
    dist = distance[count]
    dur = minutes(duration[count]['hours'], duration[count]['minutes'])
    flightNumber.append({"flightNumber": fn, "originAirport": code, "destinationAirport": dcode, "distance": dist})
    count = count + 1
print(flightNumber)


# df = pd.read_csv('2020.csv')
# origin = df["origin"]


# origin.to_json (r'origin.json')

# read_origin = pd.read_json (r'origin.json',typ='series')

# read_origin.to_csv (r'origin.csv', index = None)