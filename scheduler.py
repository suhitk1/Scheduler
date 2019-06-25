import math
import csv


from math import radians, sin, cos, acos


class venue:
    venueGeoLat = []
    venueGeoLon = []
    venueName = []

    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    with open('venueData.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            venueGeoLat.append(row[1])
            venueGeoLon.append(row[2])
            venueName.append(row[0])


class masterTrainer:
    
    name = None
    location = None
    subject = None
    latitude = None
    longitude = None
    distanceFromVenues = []
    nearestVenues = []
    
    def __init__(self, name, location, subject, latitude, longitude):
        masterTrainer.name = name
        masterTrainer.location = location
        masterTrainer.subject = subject
        masterTrainer.latitude = latitude
        masterTrainer.longitude = longitude
        x = 1
        y = 1
        while (x < 2):
            while (y < len(venue.venueGeoLat)):
                masterTrainer.distanceFromVenues.append(masterTrainer.distanceCalculator(float(masterTrainer.latitude),float(masterTrainer.longitude),float(venue.venueGeoLat[y]),float(venue.venueGeoLon[y])))
                y = y + 1
            x = x + 1
            
        MAX = 100000
        firstmin = MAX
        secmin = MAX
        thirdmin = MAX
        k = 0
        l = 0
        m = 0
        for i in range(0, len(masterTrainer.distanceFromVenues)):
            if masterTrainer.distanceFromVenues[i] < firstmin:
                thirdmin = secmin
                secmin = firstmin
                firstmin = masterTrainer.distanceFromVenues[i]
                k = i+1

            elif masterTrainer.distanceFromVenues[i] < secmin:
                thirdmin = secmin
                secmin = masterTrainer.distanceFromVenues[i]
            
                l = i+1

            elif masterTrainer.distanceFromVenues[i] < thirdmin:
                thirdmin = masterTrainer.distanceFromVenues[i]
                m = i+1
        masterTrainer.nearestVenues.append(venue.venueName[k])
        masterTrainer.nearestVenues.append(venue.venueName[l])
        masterTrainer.nearestVenues.append(venue.venueName[m])
               

    def distanceCalculator(latitude1,longitude1,latitude2,longitude2):
        slat = radians(latitude1)
        slon = radians(longitude1)
        elat = radians(latitude2)
        elon = radians(longitude2)
        dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
        return dist

    

name = []
location = []
subject = []
latitude =[]
longitude = []
with open('mtData.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        name.append(row[0])
        location.append(row[1])
        subject.append(row[4])
        latitude.append(row[2])
        longitude.append(row[3])

print(longitude)
mt1 = masterTrainer(name[0],location[0],subject[0],latitude[0],longitude[0],)
print(mt1.nearestVenues)
mt2 = masterTrainer(name[1],location[1],subject[1],latitude[1],longitude[1],)
#mt2 = masterTrainer(name[2],location[2],subject[2],latitude[2],longitude[2])
#mt[1] = masterTrainer(name[1],location[1],subject[1],latitude[1],longitude[1])
