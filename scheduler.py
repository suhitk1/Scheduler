

import math
import csv
import pdb

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
        i = 1
        j = 1
        while (i < 2):
            while (j < len(venue.venueGeoLat)):
                masterTrainer.distanceFromVenues.append(masterTrainer.distanceCalculator(float(masterTrainer.latitude),float(masterTrainer.longitude),float(venue.venueGeoLat[j]),float(venue.venueGeoLon[j])))
                j = j + 1
            i = i + 1
            
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
                k = i

            elif masterTrainer.distanceFromVenues[i] < secmin:
                thirdmin = secmin
                secmin = masterTrainer.distanceFromVenues[i]
                l = i

            elif masterTrainer.distanceFromVenues[i] < thirdmin:
                thirdmin = masterTrainer.distanceFromVenues[i]
                m = i
        masterTrainer.nearestVenues.append(venue.venueName[k+1])
        masterTrainer.nearestVenues.append(venue.venueName[l+1])
        masterTrainer.nearestVenues.append(venue.venueName[m+1])


    def distanceCalculator(latitude1,longitude1,latitude2,longitude2):
        slat = radians(latitude1)
        slon = radians(longitude1)
        elat = radians(latitude2)
        elon = radians(longitude2)
        dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
        return dist

    

name = list()
location = list()
subject = list()
latitude = list()
longitude = list()
with open('mtData.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        name.append(row[0])
        location.append(row[1])
        subject.append(row[4])
        latitude.append(row[2])
        longitude.append(row[3])

masters = list()
i = 0
while (i<len(name)):
    mt[i] = masterTrainer(name[i],location[i],subject[i],latitude[i],longitude[i])
    masters.append(mt)
    i = i+1
