import folium

import pandas as pd
from folium.plugins import HeatMap
from folium import plugins
import webbrowser
webbrowser.open("GREATER_NOIDA.html")

map = folium.Map(location=[28.474388, 77.503990], zoom_start=13)
data = [
    [28.474388, 77.503990, 1],
    [28.468024, 77.508675, 2]
]
heatmap_layer = HeatMap(data, name="Heatmap")
map.add_child(heatmap_layer)
folium.LayerControl().add_to(map)


locations = [
    (28.474388, 77.503990, "Central Greater Noida"),
    (28.464916, 77.511367, "Pari Chowk"),
    (28.459497, 77.507551, "Alpha 1"),
    (28.482559, 77.481839, "Knowledge Park"),
    
]
for lat, lon, label in locations:
    
    folium.Marker(
        location=[lat, lon],
        popup=label,
        icon=folium.Icon(icon='info-sign', color='blue')
    ).add_to(map)
    folium.Marker(
    [28.3652, 77.5411], 
    popup='Galgotias University',
    tooltip='Click for more info',
    icon=folium.Icon(icon='house')
    ).add_to(map)
folium.Marker(
    [28.474388, 77.503990], 
    popup='bla bla',
    tooltip='Click for more info',
    icon=folium.Icon(icon='cloud')
).add_to(map)
folium.Circle(
    radius=500,
    location=[28.474388, 77.503990],
    popup='Central Park',
    color='crimson',
    fill=True,
    fill_color='crimson'
).add_to(map)
minimap = plugins.MiniMap()
map.add_child(minimap)
map.save('GREATER_NOIDA.html')