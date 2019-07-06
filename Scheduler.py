import math
import csv
import pdb
import pandas as pd 
import numpy as np 
from math import radians, sin, cos, acos

def distanceCalculator(latitude1,longitude1,latitude2,longitude2):
        slat = radians(latitude1)
        slon = radians(longitude1)
        elat = radians(latitude2)
        elon = radians(longitude2)
        dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
        return dist

df = pd.read_csv("venueData.csv",header=None)
df.columns=['name','latitude','longitude','district','block']

df2 = pd.read_csv("mtdata.csv",header=None)
df2.columns = ['name','location','latitude','longitude','subject']


teacher = pd.read_csv("teachers.csv")

teacher.head()

df.head()

teacher['Latitude'] = teacher['Latitude'].apply(lambda x: x.rstrip(",") if type(x)  == str else x )
teacher['Longitude'] = teacher['Longitude'].apply(lambda x: x.rstrip(",") if type(x)  == str else x )


listEmpty = []

dictionaryTeacher = {}




for i,ex in teacher.iterrows():
    
    
    lat1 = ex['Latitude']
    lon1 = ex['Longitude']
    
    Id = i 
    
    
    for b,c in df.iterrows():
        
        
        lat2 = c['latitude']
        lon2 = c['longitude']
        
        nameVen = c['name']
        
        
        listEmpty.append((distanceCalculator(float(lat1),float(lon1),float(lat2),float(lon2)),Id,b))
        
        
        
    demian = []    
        
        
    listEmpty.sort()
    
    
    
    demian = listEmpty[0]
    
    
    dictionaryTeacher[ex['Name']] = demian
    
    listEmpty = []
    
    demian = []

DataTeacher = pd.DataFrame(columns=['Teacher','Distance','Venue','Eng','Hindi','Maths','TeacherId'])

number = 3 

for ex in dictionaryTeacher:
    
    
    DataTeacher= DataTeacher.append({'Teacher':ex,'Distance':dictionaryTeacher[ex][0],'Venue':df.loc[dictionaryTeacher[ex][2]]['name'],'Eng':teacher.loc[dictionaryTeacher[ex][1]]['Eng'],'Hindi':teacher.loc[dictionaryTeacher[ex][1]]['Hindi'],'Maths':teacher.loc[dictionaryTeacher[ex][1]]['Maths'],'TeacherId':dictionaryTeacher[ex][1]},ignore_index=True)

days = pd.read_csv("days.csv")

days.columns = ['January', 'January:Days', 'February', 'Feburary:Days', 'March',
       'March:Days', 'April', 'April:Days', 'May', 'May:Days', 'June',
       'June:Days', 'July', 'July:Days', 'August', 'August:Days',
       'September', 'September:Days', 'October', 'October:Days', 'November',
       'November:Days', 'December', 'December:Days']

df.columns=['name','latitude','longitude','district','block']

df['name'] = df['name'].apply(lambda x: x.rstrip())

df2['name'] =df2['name'].apply(lambda x: x.rstrip())

venue = {}

for i,k in enumerate(df['name']):
    
    
    if (k not in venue):
        
        venue[k] = {'January': 0 ,'February':0 , 'March': 0 , 'April':0, 'May':0,'June ':0 ,'July':0 , 'August':0,'September':0,'October':0,'November':0,'December':0}

teacher = {}

for i,k in enumerate(df2['name']):
    
    
    if (k not in teacher):
        
        teacher[k] = {'January': 0 ,'February':0 , 'March': 0 , 'April':0, 'May':0,'June ':0 ,'July':0 , 'August':0,'September':0,'October':0,'November':0,'December':0}

teacher['Ajmal']


dictionary = {}
liste = []





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
        

        liste.append((distanceCalculator(lat1,lon1,lat2,lon2),i,id2))
        
        
    
    liste.sort()
    
    dictionary[ex['name']] = liste[0:3]
    
    liste = []
    
Data = pd.DataFrame(columns=['Trainer','Venue','Distance','Subjects','Location','VenDistrict','VenBlocks'])

for ex in dictionary:
    
    for i , k in enumerate(dictionary[ex]):
        
        
        Data = Data.append({'Trainer':ex ,'Venue': df.loc[dictionary[ex][i][2]]['name'],'Distance': dictionary[ex][i][0],'Subjects':df2.loc[dictionary[ex][i][1]]['subject'],'Location':df2.loc[dictionary[ex][i][1]]['location'],'VenDistrict':df.loc[dictionary[ex][i][2]]['district'],'VenBlocks':df.loc[dictionary[ex][i][2]]['block']},ignore_index=True)

teacher['Akalmash']


Data['Month'] = -1

for i,ex in Data.iterrows():
    
    Train = ex['Trainer']
    Venue = ex['Venue']
    
    for ex in teacher[Train]:
        
        if(teacher[Train][ex]==0):
            
            if(venue[Venue][ex] == 0):
                
                teacher[Train][ex] = 1
                venue[Venue][ex] = 1
                
                Data.loc[i,"Month"] = ex
                break
    

days[days["January"][:].str.contains("Tue")]['January'].index

strings = " "

for ex in days[days["January"][:].str.contains("Tue")]['January'].index:
    strings += ","+ str(ex)

strings = strings.rstrip(",")

strings = strings.lstrip()

#days = days.apply(lambda x : x.rstrip())

Data['Month'] = Data['Month'].apply(lambda x : x.rstrip())

listeDays = []
Cal = 0 

num = 0 
strings = ""

for i,ex in Data.iterrows():
    
    
    ay = ex['Month']
    
    indexOfDays = days[days[ay][:].str.contains("Mon") |  days[ay][:].str.contains("Tue") | days[ay][:].str.contains("Wed") | days[ay][:].str.contains("Thu") | days[ay][:].str.contains("Fri")][ay].index
    
    
    for ex in days[days[ay][:].str.contains("Mon") |  days[ay][:].str.contains("Tue") | days[ay][:].str.contains("Wed") | days[ay][:].str.contains("Thu") | days[ay][:].str.contains("Fri")][ay]:
        
        num = indexOfDays[Cal]
        
        num +=1
        Cal +=1
        
        strings += str(num) + "," + ex + ","

    Data.loc[i,"Days"] = strings
    num = 0 
    Cal = 0 
    
    strings = ""


Data['Month'] = Data['Month'].apply(lambda x: x.rstrip())

Data['Days'] = Data['Days'].apply(lambda x : x.replace("\n",","))

#Data.drop("Month",axis=1,inplace=True)

DfSub = pd.read_csv("backupMasterTrainers.csv")

copyDfSub = DfSub

ab = DfSub.sample(n=1)

ab.columns = ['Name',"Location","Latitude","Longitude","Subject"]

#ab.loc[10,"Name"]
    
#Data.columns

Id = ""
VenID = 0 
newName = ""

dist = ""

VenLat =""
VenLot =""

newLat = ""
newLon = ""
newSub = ""
newLoc = ""

for i,ex in Data.iterrows():
    
    name = ex['Trainer']
    month = ex['Month']
    lecture = ex['Subjects']
   
    print(name,"Do you want to give ",lecture,"in this month :",month)
    answer = input("For Yes : Y For No N") 
    
    
    if answer == 'Y' or answer == 'y':
        
        pass
  
    elif answer == 'N' or answer =='n':
        ab = copyDfSub.sample(n=1)
        ab.columns = ['Name',"Location","Latitude","Longitude","Subject"]
        
        Id = ab.index[0]
        
        newName = ab.loc[Id,"Name"]
        newLat = ab.loc[Id,"Latitude"]
        newLon = ab.loc[Id,"Longitude"]
        newSub = ab.loc[Id,"Subject"]
        newLoc = ab.loc[Id,"Location"]
        
        VenueName = ex['Venue']
        
        for z,b in df.iterrows():
            
            if(VenueName in b['name']):
                
                VenID = z 
        
        VenLat = ven['Latitude'][z]
        VenLon = ven['Longitude'][z]
        
        dist = distanceCalculator(newLat,newLon,VenLat,VenLon)

        Data.loc[i,"Trainer"] = newName
        Data.loc[i,"Distance"] = dist
        Data.loc[i,"Subjects"] = newSub
        Data.loc[i,"Location"] = newLoc
        
        
        copyDfSub.drop(Id,inplace=True)
        copyDfSub.reset_index(drop=True,inplace=True)

df5 = pd.merge(Data,DataTeacher,on="Venue",how='inner')

df5.groupby("Teacher")

teachers = pd.read_csv("teachers.csv")

teachers.groupby(['Name','Location'],as_index=False).agg({'Distance_x': 'count'})

TeachDictMon = {}



for i,ex in teachers.iterrows():
    
    NameTeach = ex['Name']
    
    
    if NameTeach not in TeachDictMon:
        
        TeachDictMon[NameTeach] = {'January':0,'February':0,'March':0,'April':0,'May':0,'June':0,'July':0,'August':0,'September':0,'October':0,'November':0,'December':0}

TeachDictMon


df5= pd.merge(Data,DataTeacher,on='Venue',how='inner')

df5['Subjects'] = df5['Subjects'].apply(lambda x : x.title())

df5.columns = ['Trainer', 'Venue', 'Distance_x', 'Subjects', 'Location', 'VenDistrict',
       'VenBlocks', 'Month', 'Days', 'Teacher', 'Distance_y', 'Eng', 'Hindi',
       'Math', 'TeacherId']

df5.head()

dfNew = pd.DataFrame(columns=["Venue","Batches","Month","Block","District","Subjects","Date"])

dictBat = {}
BatchPoint = 0 

for i,ex in df5.iterrows():
    
    
    
    teacherId = ex['TeacherId']   
    train = ex['Trainer']
    ven = ex['Venue']
    sub = ex['Subjects']
    month = ex['Month']
    
    a = df5[(df5['Trainer']==train) & (df5['Venue'] == ven) & (df5['Subjects'] == sub)]
    
    con = a.count()
    
    BatchPoint = len(con)
    
    
    for c,b in a.iterrows():
        
        teacherId = b['TeacherId']   
        train = b['Trainer']
        ven = b['Venue']
        suber = b['Subjects']
        sub = a.loc[c][suber]
         
        if(sub not in dictBat):
            dictBat[sub] = []
            dictBat[sub].append(teacherId)
                
                
                
        else:
            
            dictBat[sub].append(teacherId)
            
            
    
    dfNew = dfNew.append({'Venue':ven,'Batches':dictBat,'Month':month,"District":ex['VenDistrict'],'Subjects':ex['Subjects'],'Blocks':ex['VenBlocks'],'Date':ex['Days']},ignore_index=True)
    dictBat = {}
    df5.drop(a.index,inplace=True)


a = dfNew[dfNew['Batches'] == {}].index

dfNew.head()

dfNew.drop("Block",axis=1,inplace=True)

dfNew.drop(a,inplace=True)
dfNew.reset_index(drop=True,inplace=True)

dfNew.head()

len(dfNew["Batches"][0]['G1'])

list(dfNew.loc[0,"Batches"].keys())[0]

Output = pd.DataFrame(columns=['S', 'Date', 'Subject', 'Group', 'Trained', 'District', 'Block',
       'Venue', 'Month'])

GroupName = ""
string = ""
num = 0 

count = 0 

for i,ex in dfNew.iterrows():
    
    Ven = ex['Venue']
    Batch = ex['Batches']
    Month = ex['Month']
    Block = ex['Blocks']
    Dist = ex['District']
    Sub = ex['Subjects']
    Date = ex['Date']
   
    num = len(Batch)
        
        
        
    for x in range(num):
            
        
        if x == 0:
            trained = len(Batch[list(dfNew.loc[i,"Batches"].keys())[x]])
            string = Date.split(",")
                
            s = str(list(dfNew.loc[i,"Batches"].keys())[x])
                
                
                
            s= s[1]
                
            Output=Output.append({'S':s,'Date':str(string[x:x+4]),'Subject':Sub,'Group':list(dfNew.loc[i,"Batches"].keys())[x],'Trained':trained,'District':Dist,'Block':Block,'Venue':Ven,'Month':Month},ignore_index=True)
            
            
            
            
        else:
            trained = len(Batch[list(dfNew.loc[i,"Batches"].keys())[x]])
            s = str(list(dfNew.loc[i,"Batches"].keys())[x])
            s = s[1]
            
                
            Output=Output.append({'S':s,'Date':str(string[x*4:x*4+4]),'Subject':Sub,'Group':list(dfNew.loc[i,"Batches"].keys())[x],'Trained':trained,'District':Dist,'Block':Block,'Venue':Ven,'Month':Month},ignore_index=True)


Output

Td=TeachDictMon

Output = pd.DataFrame(columns = ["S","Date","Subject","Group","Trained","District","Block","Venue","Month"])


Output


df5['Subjects'] = df5['Subjects'].apply(lambda x : x.title())


a=df5[(df5['Subjects'] == 'Eng') & (df5['Venue'] == 'Gobind pura')]

numOfMonth = 0 

for i,ex in df5.iterrows():
    
    TrainerName = ex['Trainer']
    Venue = ex['Venue']
    VenBlock = ex['VenBlocks']
    Month = ex['Month']
    

df5.columns = ['Trainer', 'Venue', 'Distance_x', 'Subjects', 'Location', 'VenDistrict',
       'VenBlocks', 'Month', 'Days', 'Teacher', 'Distance_y', 'Eng', 'Hindi',
       'Math', 'TeacherId']
