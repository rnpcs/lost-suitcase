#!/usr/bin/env python
# coding: utf-8


import requests
import xml.etree.ElementTree as ET
import math
import folium
import pandas as pd
import time
from selenium import webdriver
import os
import webbrowser

"""
def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
        else:
            ref(driver)


    wrapper.has_run = False
    return wrapper



@run_once
def openmap(driver, cwd, url2):
    driver.get('file://'+ cwd + url2)

    return


def ref(driver):
    driver.refresh()
"""

def tagging(lon_list, lat_list, name_list):

    
    dict2 = {
    'lat':lat_list,
    'lon':lon_list,
    'name':name_list
    }
    
    data = pd.DataFrame.from_dict(dict2)

    # Make an empty map
    m = folium.Map(location=[jlat, jlon ], tiles="OpenStreetMap", zoom_start=15)

 
    folium.Marker(
        location=[jlat, jlon],
        popup='You are here',
        icon=folium.Icon(color='red', icon='user', prefix='fa')
    ).add_to(m)

    folium.Circle(
        location=[jlat, jlon],
        radius=1000,
        popup='Within 1 KM',
        color='#3186cc',
        fill=True,
        #fill_color='#3186cc'
    ).add_to(m)



    # I can add marker one by one on the map
    for i in range(0,len(data)):
 
        folium.Marker([data.iloc[i]['lon'], data.iloc[i]['lat']],
         popup=data.iloc[i]['name'],
         icon=folium.Icon(icon = 'bus', prefix='fa')
    ).add_to(m)
 
    # Save it as html
    m.save('map.html')
    
    #url2=('map.html')
    #webbrowser.open(url2, new=2, autoraise=True)
    
    url2=('\map.html')
    cwd = os.getcwd() 

    driver.get('file://'+ cwd + url2)
    
    #print(driver)
 
    return 

# In[ ]:


def haversine(lat1, lon1, lat2, lon2):
    toRad = math.pi / 180
    # distance between latitudes 
    # and longitudes 
    dLat = (lat2 - lat1) * math.pi / 180
    dLon = (lon2 - lon1) * math.pi / 180
  
    # convert to radians 
    lat1 = (lat1) * math.pi / 180
    lat2 = (lat2) * math.pi / 180
  
    # apply formulae 
    a = (pow(math.sin(dLat / 2), 2) + 
         pow(math.sin(dLon / 2), 2) * 
             math.cos(lat1) * math.cos(lat2)); 
    rad = 6371
    c = 2 * math.asin(math.sqrt(a)) 
    return rad * c 


# In[ ]:


def getData():
    url = 'http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22'
    resp = requests.get(url)

    with open('training2.xml', 'wb') as f:
        f.write(resp.content)


    tree = ET.parse("training2.xml")
    root = tree.getroot()

    for time in root.findall('time'):
        currTime=time.text
        
    print("+++++++++++++++++++++++++++++++++++++++++++++")
    print("Time: " + currTime)

    for bus in root.findall('bus'):
       
        
        id_no = bus.find('id').text
        d = bus.find('pd').text
        lat = float(bus.find('lat').text)
        lon  = float(bus.find('lon').text)
        
        if d == 'Northbound':
            dis = haversine(lat, lon , jlat, jlon)
            print(("\nBus ID :%s,  %s direction \n%0.2f km from the office\n ")%(id_no, d, dis))
            
            
            if dis < 1:
                lat_list.append(lat)
                lon_list.append(lon)
                name_list.append('Bus No: ' + id_no)
            
            if dis < 1:
                tagging(lat_list, lon_list, name_list)
                
            

    return

def main():

    id_no, d,lat, lon,  dis = getData()
    
    return


driver = webdriver.Firefox()
while True:

    jlat = 41.980262
    jlon = -87.668452
    lat_list = []
    lon_list = []
    name_list = []

    getData()
    time.sleep(10)

