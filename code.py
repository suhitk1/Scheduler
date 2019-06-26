import math
import csv
import pdb
import pandas as pd 
import numpy as np 
from math import radians, sin, cos, acos

pd.options.display.max_rows = 150


df = pd.read_csv("venueData.csv",header=None)

df2 = pd.read_csv("mtData.csv",header=None)

df2.columns = ['name','location','latitude','longitude','subject']

df.columns=['name','latitude','longitude']

dictionary = {}
liste = []
def distanceCalculator(latitude1,longitude1,latitude2,longitude2):
        slat = radians(latitude1)
        slon = radians(longitude1)
        elat = radians(latitude2)
        elon = radians(longitude2)
        dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
        return dist

for i,ex in df2.iterrows():
    
    nameT = ex['name']
    lat1  = ex['latitude']
    lon1  = ex['longitude']
    sub   = ex['subject'] 
    Id = i 
        
    for b , x in df.iterrows():
        
        nameM = x['name']
        lat2  = x['latitude']
        lon2  = x['longitude']
        id2 = b
        
        liste.append((distanceCalculator(lat1,lon1,float(lat2),float(lon2)),i,id2))
            
    liste.sort()
    
    dictionary[ex['name']] = liste[0:3]
    
    liste = []

Data = pd.DataFrame(columns=['Trainer','Venue','Distance','Subjects','Location'])

for ex in dictionary:
    
    for i , k in enumerate(dictionary[ex]):
        
        
        Data = Data.append({'Trainer':ex ,'Venue': df.loc[dictionary[ex][i][2]]['name'],'Distance': dictionary[ex][i][0],'Subjects':df2.loc[dictionary[ex][i][1]]['subject'],'Location':df2.loc[dictionary[ex][i][1]]['location']},ignore_index=True)

dfMonth = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}

dfMonth

Data['Month'] = -1

for i,ex in enumerate(Data['Month']):
    
    if(i % 3 == 0):
        Data.loc[i,"Month"] = 'January'
        
    elif(i%3 == 1):
        Data.loc[i,"Month"] = 'February'
        
    elif(i%3 == 2):
        Data.loc[i,"Month"] = 'March'
    
Data