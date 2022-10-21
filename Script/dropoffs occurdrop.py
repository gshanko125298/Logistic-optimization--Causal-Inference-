import folium
from folium import plugins

coord=[]
for lat,lng in zip(started_delivery.lat,started_delivery.lng):
  coord.append([lat,lng])

map = folium.Map(
    location=[6.465422, 3.406448],
    tiles='Lagos, Nigeria',
    zoom_start=7,
    width='80%', 
    height='50%',
    control_scale=True)

map.add_child(plugins.HeatMap(coord))
        
map