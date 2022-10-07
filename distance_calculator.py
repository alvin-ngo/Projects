
import math
from geopy.geocoders import Nominatim

geocoder = Nominatim(user_agent = 'distance_calc')


def getcoord():
    input1 = geocoder.geocode(input(f"Enter Location 1: "))
    input2 = geocoder.geocode(input(f"Enter Location 2: "))
    lat1 = math.radians(input1.latitude)
    lat2 = math.radians(input2.latitude)
    long1 = math.radians(input1.longitude)
    long2 = math.radians(input2.longitude)

    dis =  3958.8 * math.acos((math.sin(lat1) * math.sin(lat2)) + math.cos(lat1) * math.cos(lat2) * math.cos(long2 - long1))
    #radius of earth = 3958.8 miles 

    print(f"{round(dis,1)} Miles")

getcoord()
