from urllib.request import urlopen
import json
from time import sleep

DUMP1090DATAURL = "http://localhost:8080/data.json"

class FlightData():
    def __init__(self, data_url = DUMP1090DATAURL):

        self.data_url = data_url

        self.refresh()

    def refresh(self):
        #open the data url
        self.req = urlopen(self.data_url)

        #read data from the url
        self.raw_data = self.req.read()

        #encode the data
        encoding = self.req.headers.get_content_charset()

        #load in the json
        self.json_data = json.loads(self.raw_data.decode(encoding))

        self.aircraft = AirCraftData.parse_flightdata_json(self.json_data)

    def _refresh(self):

        data_file = open("data.json")
        
        #load in the json
        self.json_data = json.load(data_file)

        self.aircraft = AirCraftData.parse_flightdata_json(self.json_data)

class AirCraftData():
    def __init__(self,
                 dhex,
                 squawk,
                 flight,
                 lat,
                 lon,
                 validposition,
                 altitude,
                 vert_rate,
                 track,
                 validtrack,
                 speed,
                 messages,
                 seen,
                 mlat):
        
        self.hex = dhex
        self.squawk = squawk
        self.flight = flight
        self.lat = lat
        self.lon = lon
        self.validposition = validposition
        self.altitude = altitude
        self.vert_rate = vert_rate
        self.track = track
        self.validtrack = validtrack
        self.speed = speed
        self.messages = messages
        self.seen = seen
        self.mlat = mlat

    @staticmethod
    def parse_flightdata_json(json_data):
        aircraft_list = []
        for aircraft in json_data:
            aircraftdata = AirCraftData(
                aircraft["hex"],
                aircraft["squawk"],
                aircraft["flight"],
                aircraft["lat"],
                aircraft["lon"],
                aircraft["validposition"],
                aircraft["altitude"],
                aircraft["vert_rate"],
                aircraft["track"],
                aircraft["validtrack"],
                aircraft["speed"],
                aircraft["messages"],
                aircraft["seen"],
                aircraft["mlat"])
            aircraft_list.append(aircraftdata)
        return aircraft_list

    def __hash__(self):
        return hash(self.hex)

    def __eq__(self, other):
        if other is None:
            return False
        else:
            return (self.hex == other.hex)
            
#test    
if __name__ == "__main__":
    
    #create FlightData object
    myflights = FlightData()
    while True:
        #loop through each aircraft found
        for aircraft in myflights.aircraft:
            
            #print the aircraft's data
            print(aircraft.hex)
            print(aircraft.squawk)
            print(aircraft.flight)
            print(aircraft.lat)
            print(aircraft.lon)
            print(aircraft.validposition)
            print(aircraft.altitude)
            print(aircraft.vert_rate)
            print(aircraft.track)
            print(aircraft.validtrack)
            print(aircraft.speed)
            print(aircraft.messages)
            print(aircraft.seen)
            print(aircraft.mlat)

        sleep(1)

        #refresh the flight data
        myflights.refresh()

