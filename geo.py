# import libraries
import folium
import pandas as pd
import webbrowser 

lat = -87.6729736328125
lon = 42.0178554591847
name = '1915'
jlat = -87.6683349609375
jlon = 41.980262 


lat_list = [ jlat ]
lon_list = [ jlon ]
name_list = [ 'You are here']


def tagging(lat, lon, name):

    lat_list.append(lat)
    lon_list.append(lon)
    name_list.append(name)

    dict2 = {
    'lat':lat_list,
    'lon':lon_list,
    'name':name_list
    }

    """
    # Make a data frame with dots to show on the map
    data = pd.DataFrame({
    'lat':[-87.6683349609375 ],
    'lon':[  41.980262],
    'name':[ 'Jerry\'s Office']
    })
    data
    """
    #dict2.update({'name': ['1915'], 'lon': [42.01785545918479], 'lat': [-87.6729736328125]})
    data = pd.DataFrame.from_dict(dict2)

    # Make an empty map
    m = folium.Map(location=[41.980262,-87.6683349609375 ], tiles="StamenToner", zoom_start=12.5)
     
    # I can add marker one by one on the map
    for i in range(0,len(data)):
        folium.Marker([data.iloc[i]['lon'], data.iloc[i]['lat']], popup=data.iloc[i]['name']).add_to(m)
 
    # Save it as html
    m.save('312_markers_on_folium_map1.html')
    url2=('312_markers_on_folium_map1.html')
    webbrowser.open_new(url2)

    return

tagging(lat, lon, name)


