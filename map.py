import folium
from folium import plugins
import webbrowser
webbrowser.open("GREATER_NOIDA.html")

map = folium.Map(location=[28.474388, 77.503990], zoom_start=13)
data = [
    [28.474388, 77.503990, 1],
    [28.468024, 77.508675, 2]
]
plugins.Geocoder().add_to(map)

map


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
    folium.Marker([28.488531387204894, 77.51407584674739],
              popup="<h1>Omaxe Mall</h1><img src='omaxe.jpg' width = 400px",
              tooltip="Omaxe",
              icon=folium.Icon(icon='star',icon_color='red', color='beige')).add_to(map)
    folium.Marker([28.474936098997734, 77.51768441805312],
              popup="<h1>Swimming pool</h1><img src='pool.jpg' width = 400px",
              tooltip="pool",
              icon=folium.Icon(icon='star',icon_color='red', color='beige')).add_to(map)
    folium.Marker([28.452543984662142, 77.5263006709383],
              popup="<h1>The Grand Venice Mall</h1><img src='venice.jpg' width = 400px",
              tooltip="venice",
              icon=folium.Icon(icon='star',icon_color='red', color='beige')).add_to(map)
    folium.Marker([28.365047694940156, 77.5410147397398],
              popup="<h1>Galgotias University</h1><img src='galgotias.jpg' width = 400px",
              tooltip="Galgotias University",
              icon=folium.Icon(icon='book',icon_color='red', color='beige')).add_to(map)
    folium.Marker([28.43230535063263, 77.50315389877728],
              popup="<h1>Aditya Randi</h1><img src='nimbus2.jpg' width = 400px",
              tooltip="i1-206",
              icon=folium.Icon(icon='heart',icon_color='red', color='beige')).add_to(map)
    folium.Marker([28.478509381766518, 77.51536600603345],
              popup="<h1>Deepasnhu's Residence</h1><img src='Deepu.jpg' width = 400px",
              tooltip="DEEPU",
              icon=folium.Icon(icon='heart',icon_color='red', color='beige')).add_to(map)

minimap = plugins.MiniMap()
map.add_child(minimap)
map.save('GREATER_NOIDA.html')
